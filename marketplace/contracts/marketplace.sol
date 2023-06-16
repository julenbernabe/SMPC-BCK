// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;


import "./token/Token.sol";

contract marketplace {

    /* -------------------------------------- OTHER CONTRACT IMPORTATION -------------------------------------- */


    Token private token;
                                                                                                                                         
                                                        
    // ------------------------------------------------------------CONSTRUCTOR------------------------------------------------------------


    constructor(address tokenaddress) {
        last = 0;
        token = Token(tokenaddress);
    }

    // ------------------------------------------------------------STRUCTS------------------------------------------------------------


    struct CampaignData {
        uint n_players;    
        string CA;
        string mpcPath;
        uint reputation;
        uint subscribed_players;
        uint payment;
        uint tokensPerItem;
        uint MODL;
        uint current_data;
        uint ready_players;
        uint finished_players;
        uint succeeded;
        uint scientist_vote;
        uint aborted;
        uint nBins;
        uint binIndex;
        uint[] elected_list;
        mapping (address => uint) elected;
        mapping (uint => PlayerData) Players;
        FilesLoc Files;
        StateType CampaignState;
    }

    struct PlayerData {
        address account;
        string IP;
        string CRT;
        string CN;
        uint data_length;
        uint reputation;
    }

    struct FilesLoc {
        string BC;
        string SCH;
        string PREP;
        string INFO;
    }


    // ------------------------------------------------------------EVENTS------------------------------------------------------------


    event new_campaign(
        uint i,
        string info
    );

    event updated_campaign(
        uint i,
        string info
    );

    event scientist_ready(
        uint i,
        uint bin
    );

    event execution_finished(
        uint i,
        uint bin
    );
    
    event players_filled(
        uint i
    );

    event execution_ready(
        uint i,
        uint bin
    );

    event execution_successful(
        uint i,
        uint bin
    );

    event execution_failed(
        uint i,
        uint bin
    );

    // -------------------------------------------------------OTHER VARIABLES-------------------------------------------------------


    mapping (uint => CampaignData) Prog;
    mapping (address => uint) registered;
    mapping (address => uint) reputations;

    uint public last;

    enum StateType {Previous, SubscribingTime, ModelUpload, ScientistReady, ExecutionReady, Finished}      
    

    // ------------------------------------------------------- CALLDATA FUNCTIONS -------------------------------------------------------


    function getCampaignState(uint i) external view returns (StateType, string memory, string memory, uint) {
        CampaignData storage NewProg = Prog[i];
        string memory text1;
        string memory text2;
        uint number;
        if (NewProg.CampaignState == StateType.SubscribingTime) {
            text1 = "We are at subscribing time";
            text2 = "Subscribed players:";
            number = NewProg.subscribed_players;
        }
        else if (NewProg.CampaignState == StateType.ModelUpload) {
            text1 = "We are waiting for the data scientist to upload the model";
            text2 = "Subscribed players:";
            number = NewProg.subscribed_players;
        }
        else if (NewProg.CampaignState == StateType.ScientistReady) {
            text1 = "We are waiting for all players to tell they are ready.";
            text2 = "Ready players at this moment";
            number = NewProg.ready_players;
        }
        else if (NewProg.CampaignState == StateType.ExecutionReady) {
            text1 = "The network is ready to start the SMPC execution.";
            text2 = "";
            number = 0;
        }
        return (NewProg.CampaignState, text1, text2, number);
    }

    function getMPCPath(uint i) external view returns (string memory) {
        CampaignData storage NewProg = Prog[i];
        require(msg.sender == NewProg.Players[0].account, 'You are not allowed to obtain this information.');
        return NewProg.mpcPath;
    }
    
    function getPlayerData(uint n, uint i) external view returns (uint, string memory, string memory, string memory, uint) {
        CampaignData storage NewProg = Prog[i];
        require (NewProg.CampaignState == StateType.ScientistReady, "You cannot execute this function at this moment.");
        require(NewProg.elected[msg.sender] == 1, "You are not allowed to obtain this information.");
        uint index = NewProg.elected_list[n];
        uint my_n = 0;
        if (msg.sender == NewProg.Players[index].account) {
            my_n = 1;
        }
        return (index, NewProg.Players[index].IP, NewProg.Players[index].CRT, NewProg.Players[index].CN, my_n);
    }
    
    function getSubscribedPlayers(uint i) external view returns (uint) {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.ModelUpload, "You cannot execute this function at this moment.");
        require(msg.sender == NewProg.Players[0].account, "You are not allowed to obtain this information.");
        return NewProg.subscribed_players;
    }

    function getPlayerDataLength(uint n, uint i) external view returns (uint, uint, uint) {
        CampaignData storage NewProg = Prog[i];
        require(msg.sender == NewProg.Players[0].account, "You cannot call this function.");
        require (NewProg.CampaignState == StateType.ModelUpload || NewProg.CampaignState == StateType.Finished, "You cannot execute this function at this moment.");
        return (n, NewProg.Players[n].data_length, NewProg.Players[n].reputation);
    }

    function getElected(uint i) external view returns (uint) {
        CampaignData storage NewProg = Prog[i];
        return NewProg.elected[msg.sender];
    }

    function getTotalPlayers(uint i) external view returns (uint) {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.ScientistReady, "You cannot obtain this information at this moment.");
        require(NewProg.elected[msg.sender] == 1, "You are not allowed to obtain this information.");
        return NewProg.n_players;
    }

    function getInfoFileLocation(uint i) external view returns (string memory) {
        CampaignData storage NewProg = Prog[i];
        require (NewProg.CampaignState != StateType.Previous, "The file you are searching for is not uploaded yet. If you want, you can throw an operation to compute.");
        return NewProg.Files.INFO;
    }

    function getExecutionFilesLocation(uint i) external view returns (string memory, string memory, string memory) {
        CampaignData storage NewProg = Prog[i];
        require (NewProg.CampaignState == StateType.ScientistReady, "You cannot obtain this information yet.");
        require(NewProg.elected[msg.sender] == 1, "You are not allowed to obtain this information.");
        return (NewProg.Files.BC, NewProg.Files.SCH, NewProg.Files.PREP);
    }

    function getCA(uint i) external view returns (string memory) {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.SubscribingTime || NewProg.CampaignState == StateType.ScientistReady, "You cannot obtain this information at this moment.");
        return NewProg.CA;
    }

    function getPaymentPrediction(uint i) external view returns (uint, uint) {
        CampaignData storage NewProg = Prog[i];
        return (NewProg.payment, NewProg.MODL);
    }

    function getReputation() external view returns (uint) {
        return reputations[msg.sender];
    }

    function getMinimumReputation(uint i) external view returns (uint) {
        CampaignData storage NewProg = Prog[i];
        return NewProg.reputation;
    }

    function getMODL(uint i) external view returns (uint) {
        CampaignData storage NewProg = Prog[i];
        return NewProg.MODL;
    }

    function getRegistered() external view returns (uint) {
        return registered[msg.sender];
    }

    function getBalance() external view returns (uint) {
        return token.balanceOf(msg.sender);
    }


    // -------------------------------------------------------AUXILIARY FUNCTIONS-------------------------------------------------------
    

    function repeated(uint j) public view returns (uint) {
        CampaignData storage NewProg = Prog[j];
        uint result = 1;
        for (uint i = 0; i < NewProg.subscribed_players; i++) {
            if (NewProg.Players[i].account == msg.sender) {
                result = 0;
                break;
            }
        }
        return result;
    }

    // function withdraw(uint amount) external payable {
    //     token.transfer(msg.sender, amount);
    // }

    // ------------------------------------------------------- MAIN FUNCTIONS -------------------------------------------------------

    
    function register() external {
        require(registered[msg.sender] == 0, "You already registered in the marketplace.");
        registered[msg.sender] = 1;
        reputations[msg.sender] = 50;
    }

    function newCampaign(string[7] memory str_items, uint my_data_length, uint _MODL, uint min_reputation, uint tokens) external {
        // str_items = [CA, IP, CRT, CN, PREPROCESSING, INFORMATION, mpcPath]
        require(reputations[msg.sender] >= min_reputation, "You required more reputation than the one you have.");
        require(token.balanceOf(msg.sender) >= tokens, "You promised more tokens than the ones you have.");
        last = last + 1;
        CampaignData storage NewProg = Prog[last];
        NewProg.CA = str_items[0];
        NewProg.reputation = min_reputation;
        reputations[msg.sender] -= min_reputation;
        NewProg.CampaignState = StateType.SubscribingTime;
        NewProg.subscribed_players = 1;
        NewProg.MODL = _MODL;
        NewProg.payment = tokens;
        NewProg.current_data = my_data_length;
        NewProg.Players[0] = PlayerData(
            {
                account: msg.sender,
                IP: str_items[1],
                CRT: str_items[2],
                CN: str_items[3],
                data_length: my_data_length,
                reputation: min_reputation
            }
        );
        NewProg.Files.PREP = str_items[4];
        NewProg.Files.INFO = str_items[5];
        NewProg.mpcPath = str_items[6];
        // Before calling this function we need to call the approve(tokenaddress, amount) from Token.sol
        token.transferFrom(msg.sender, address(this), tokens);
        emit new_campaign(last, str_items[5]);
    }

    function subscribe(uint my_data_length, string calldata myIP, string calldata myCRT, string calldata myCN, uint i, uint _reputation) external {
        require(reputations[msg.sender] >= _reputation, "You gambled more reputation than the one you have.");
        CampaignData storage NewProg = Prog[i];
        require (NewProg.CampaignState == StateType.SubscribingTime, "The contract cannot proccess your claim in its current state.");
        require (repeated(i) == 1, "You already have signed up for this operation.");
        require (_reputation >= NewProg.reputation, "Your reputation is not enough to participate in this SMPC.");
        require (my_data_length < NewProg.MODL, "Your data length must be less than the MODL.");
        reputations[msg.sender] -= _reputation;
        NewProg.Players[NewProg.subscribed_players] = PlayerData(
            {
                account: msg.sender,
                IP: myIP,
                CRT: myCRT,
                CN: myCN,
                data_length: my_data_length,
                reputation: _reputation
            }
        );
        NewProg.subscribed_players += 1;
        NewProg.current_data += my_data_length;
        if (NewProg.current_data >= NewProg.MODL) {
            NewProg.CampaignState = StateType.ModelUpload;
            emit players_filled(i);
        }
    }

    function scientistReady(uint[] calldata elected_players, string calldata BC_hash, string calldata SCH_hash, uint i, uint n_bins, uint current_bin) external {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.ModelUpload, "You cannot call this function at this moment.");
        require(msg.sender == NewProg.Players[0].account, "You are not who made the request for this operation.");
        NewProg.CampaignState = StateType.ScientistReady;
        NewProg.tokensPerItem = NewProg.payment / NewProg.current_data;
        if (current_bin == 0) {
            NewProg.Players[0].reputation = NewProg.Players[0].reputation / n_bins;
        } else {
            NewProg.Players[0].data_length = 0;
        }
        NewProg.n_players = elected_players.length;
        NewProg.elected_list = elected_players;
        NewProg.nBins = n_bins;
        NewProg.binIndex = current_bin;
        for (uint j = 0; j < NewProg.n_players; j++) {
            NewProg.elected[NewProg.Players[NewProg.elected_list[j]].account] = 1;
        }
        NewProg.elected[msg.sender] = 1;
        NewProg.Files.BC = BC_hash;
        NewProg.Files.SCH = SCH_hash;
        emit scientist_ready(i, NewProg.binIndex);
    }

    function playerReady(uint i) external {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.ScientistReady, "You cannot call this function at this moment.");
        require(NewProg.elected[msg.sender] == 1, "You are not allowed to tell you're ready.");
        NewProg.elected[msg.sender] = 2;
        NewProg.ready_players += 1;
        if (NewProg.ready_players == NewProg.n_players) {
            emit execution_ready(i, NewProg.binIndex);
            NewProg.ready_players = 0;
            NewProg.CampaignState = StateType.ExecutionReady;
        }
    }

    function finished(uint i, uint success) external {
        CampaignData storage NewProg = Prog[i];
        require(NewProg.CampaignState == StateType.ExecutionReady, "The contract cannot proccess your claim in its current state.");
        require(NewProg.elected[msg.sender] == 2, "You are not allowed to tell you've finished.");
        if (msg.sender == NewProg.Players[0].account) {
            NewProg.scientist_vote = success;
        }
        NewProg.elected[msg.sender] = 3;
        NewProg.finished_players += 1;
        if (success == 0) {
            NewProg.aborted += 1;
        } else {
            NewProg.succeeded += 1;
        }
        if (NewProg.finished_players == NewProg.n_players) {
            emit execution_finished(i, NewProg.binIndex);
            NewProg.finished_players = 0;
            if (NewProg.succeeded > NewProg.aborted) {
                payments(i, 1);
                emit execution_successful(i, NewProg.binIndex);
            } else if (NewProg.succeeded == NewProg.aborted) {
                if (NewProg.scientist_vote == 1) {
                    payments(i, 1);
                    emit execution_successful(i, NewProg.binIndex);
                } else {
                    payments(i, 0);
                    emit execution_failed(i, NewProg.binIndex);
                }
            } else {
                payments(i, 0);
                emit execution_failed(i, NewProg.binIndex);
            }
            if (NewProg.binIndex == NewProg.nBins - 1) {
                NewProg.CampaignState = StateType.Finished;
            } else {
                NewProg.CampaignState = StateType.ModelUpload;
            }
        }
    }

    function payments(uint i, uint success) public payable {
        CampaignData storage NewProg = Prog[i];
        if (success == 1) {
            reputations[NewProg.Players[0].account] += 2 * NewProg.Players[0].reputation;
            for (uint j = 0; j < NewProg.n_players; j++) {
                if (NewProg.elected[NewProg.Players[NewProg.elected_list[j]].account] == 3) {
                    if (NewProg.Players[NewProg.elected_list[j]].account != NewProg.Players[0].account) {
                        reputations[NewProg.Players[NewProg.elected_list[j]].account] += 2 * NewProg.Players[NewProg.elected_list[j]].reputation;
                    }
                    uint amount = NewProg.tokensPerItem * NewProg.Players[NewProg.elected_list[j]].data_length;
                    token.transfer(NewProg.Players[NewProg.elected_list[j]].account, amount);
                    NewProg.elected[NewProg.Players[NewProg.elected_list[j]].account] = 4;
                }
            }
        } else {
            for (uint k = 0; k < NewProg.n_players; k++) {
                if (NewProg.elected[NewProg.Players[NewProg.elected_list[k]].account] == 3) {
                    uint amount = NewProg.tokensPerItem * NewProg.Players[NewProg.elected_list[k]].data_length;
                    token.transfer(NewProg.Players[0].account, amount);  
                    NewProg.elected[NewProg.Players[NewProg.elected_list[k]].account] = 4;                  
                }
            }
        }
    }

    function updateCampaign(uint i, string[4] memory str_items, uint my_data_length, uint _MODL, uint min_reputation, uint tokens) external {
        // str_items = [CA, IP, CRT, CN]
        require(reputations[msg.sender] >= min_reputation, "You required more reputation than the one you have.");
        require(token.balanceOf(msg.sender) >= tokens, "You promised more tokens than the ones you have.");
        require (i <= last, "There is no previous operation to update at this index.");
        CampaignData storage NewProg = Prog[i];
        require (NewProg.CampaignState == StateType.Finished, "This program has not finished yet. You cannot update it.");
        for (uint j = 0; j < NewProg.subscribed_players; j++) {
            NewProg.elected[NewProg.Players[j].account] = 0;
        }
        NewProg.CA = str_items[0];
        NewProg.reputation = min_reputation;
        reputations[msg.sender] -= min_reputation;
        NewProg.CampaignState = StateType.SubscribingTime;
        NewProg.ready_players = 0;
        NewProg.finished_players = 0;
        NewProg.aborted = 0;
        NewProg.succeeded = 0;
        NewProg.scientist_vote = 0;
        NewProg.subscribed_players = 1;
        NewProg.MODL = _MODL;
        NewProg.payment = tokens;
        NewProg.current_data = my_data_length;
        NewProg.Players[0] = PlayerData(
            {
                account: msg.sender,
                IP: str_items[1],
                CRT: str_items[2],
                CN: str_items[3],
                data_length: my_data_length,
                reputation: min_reputation
            }
        );
        // Before calling this function we need to call the approve(tokenaddress, amount) from Token.sol
        token.transferFrom(msg.sender, address(this), tokens);
        emit updated_campaign(i, NewProg.Files.INFO);
    }
}