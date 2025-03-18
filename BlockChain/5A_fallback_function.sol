pragma solidity ^0.8.20;

contract FallbackExample {
    event Recieved(address sender, uint amount);
    event FallbackTriggered(address sender, uint amount, bytes data);

    fallback() external payable {
        emit FallbackTriggered(msg.sender, msg.value, msg.data);
    }

    receive() external payable {
        emit Recieved(msg.sender, msg.value);
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
