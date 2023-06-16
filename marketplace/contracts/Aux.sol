// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

contract Aux {

    // -------------------------------------------------------OTHER VARIABLES-------------------------------------------------------

    mapping (address => uint) registered;
    mapping (address => uint) reputations;      

    // ------------------------------------------------------- CALLDATA FUNCTIONS -------------------------------------------------------

    function getRegistered(address sender) external view returns (uint) {
        return registered[sender];
    }

    function getReputation(address sender) external view returns (uint) {
        return registered[sender];
    }

    // ------------------------------------------------------- MAIN FUNCTIONS -------------------------------------------------------

    
    function register(address sender) external {
        require(registered[sender] == 0, "You already registered in the marketplace.");
        registered[sender] = 1;
        reputations[sender] = 50;
    }

    function setReputation(address sender, uint amount, uint isPositive) external {
        if (isPositive == 1) {
            reputations[sender] += amount;
        } else {
            reputations[sender] -= amount;
        }
    }
}