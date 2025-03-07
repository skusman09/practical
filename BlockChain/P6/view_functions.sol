pragma solidity ^0.8.20;

contract ViewFunctionsExample {
    uint private number;
    address private owner;
    string private message;

    constructor(uint _number, string memory _message) {
        number = _number;
        owner = msg.sender;
        message = _message;
    }
    function getNumber() public view returns (uint) {
        return number;
    }
    function getOwner() public view returns (address) {
        return owner;
    }
    function getMessage() public view returns (string memory) {
        return message;
    }
    function getCurrentBlockTimestamp() public view returns (uint) {
        return block.timestamp;
    }
    function getCurrentBlockNumber() public view returns (uint) {
        return block.number;
    }
    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }
}