pragma solidity ^0.8.20;

contract FunctionOverloading {
    event Result(uint value);

    function add(uint a) public pure returns (uint) {
        return a + 10;
    }
    function add(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
    function add(uint a, uint b, uint8 c) public pure returns (uint) {
        return a + b + c;
    }
    function testOverloading() public pure returns (uint, uint, uint) {
        uint result1 = add(5);
        uint result2 = add(5, 10);
        uint result3 = add(5, 10, 2);
        return (result1, result2, result3);
    }
}