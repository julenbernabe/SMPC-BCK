# The Marketplace Contract

This project contains all the files needed to deploy a Smart Contract for a Solidity-based Private Data Marketplace. Once you have installed this repository, refer to [the SCALE-MAMBA & Ethereum Client](https://github.com/julenbernabe/SMPC-BCK) in order to run the client for the marketplace.

## Installation

**Observation:** For the installation we will use [Truffle](https://www.trufflesuite.com/docs/truffle/getting-started/installation). Truffle is a tool to deploy and manage an Ethereum network consisting of a single node, and it is usually been used for testing purposes.

For a quick installation, run:

```bash
truffle develop
```

If it is your first time deploying the marketplace, run

```bash
migrate --to 2
```

Then, refer to the [marketplace.sol](https://github.com/julenbernabe/marketplace-eth/blob/main/contracts/marketplace.sol) file and change the token's contract address with the new one you obtained in the previous step. Once you do that, you can run

```bash
migrate --from 3
```

and you are done!

If you did the previous at least one time before, you already deployed the token's contract, so you can simply run

```bash
migrate
```
