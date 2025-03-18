pragma solidity ^0.8.0;

contract ArrayHandling {

    uint[] public numbers;

    function addNumber(uint _number) public {
        numbers.push(_number);
    }

    function getNumber(uint index) public view returns (uint) {
        require(index < numbers.length, "Index out of bounds");
        return numbers[index];
    }

    function getAllNumber() public view returns (uint[] memory) {
        return numbers;
    }
} 