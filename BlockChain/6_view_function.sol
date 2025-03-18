pragma solidity ^0.8.20;

contract ViewFunctionsExample {
    uint private number;
    address private owner;
    string private message;

    constructor(uint _number, string memory _message) {
        number = _number;
        owner = msg.sender; // Fixed typo from 'mse.sender' to 'msg.sender'
        message = _message;
    }

    // View function to get the stored number
    function getNumber() public view returns (uint) {
        return number;
    }

    // View function to check contract owner
    function getOwner() public view returns (address) {
        return owner;
    }

    // View function to get the stored message
    function getMessage() public view returns (string memory) {
        return message;
    }

    // View function to check the current block timestamp
    function getCurrentBlockTimestamp() public view returns (uint) {
        return block.timestamp;
    }

    // View function to check the current block number
    function getCurrentBlockNumber() public view returns (uint) {
        return block.number;
    }

    // View function to check contract balance
    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }
}
