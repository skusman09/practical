pragma solidity ^0.8.20;

contract FallbackExample {
    event Received(address sender, uint amount);
    event FallbackTriggered(address sender, uint amount, bytes data);

    fallback() external payable {
        emit FallbackTriggered(msg.sender, msg.value, msg.data);
    }
    receive() external payable {
        emit Received(msg.sender, msg.value);
    }
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}