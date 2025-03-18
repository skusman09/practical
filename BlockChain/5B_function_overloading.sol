pragma solidity ^0.8.20;

contract FunctionOverloading {
    event Result(uint value);

    // Function with one parameter
    function add(uint a) public pure returns (uint) {
        return a + 10;
    }

    // Overloaded function with two parameters
    function add(uint a, uint b) public pure returns (uint) {
        return a + b;
    }

    // Overloaded function with different data types
    function add(uint a, uint b, uint8 c) public pure returns (uint) {
        return a + b + c;
    }

    // Example of calling overloaded functions
    function testOverloading() public pure returns (uint, uint, uint) {
        uint result1 = add(5); // Calls add(uint)
        uint result2 = add(5, 10); // Calls add(uint, uint)
        uint result3 = add(5, 10, 2); // Calls add(uint, uint, uint8)
        return (result1, result2, result3);
    }
}
