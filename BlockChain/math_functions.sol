pragma solidity ^0.8.20;

contract MathFunctions {
    function add(uint a, uint b) public pure returns (uint) {
        return a + b;
    }
    function subtract(uint a, uint b) public pure returns (uint) {
        require(a >= b, "Underflow error");
        return a - b;
    }
    function multiply(uint a, uint b) public pure returns (uint) {
        return a * b;
    }
    function divide(uint a, uint b) public pure returns (uint) {
        require(b > 0, "Cannot divide by zero");
        return a / b;
    }
    function mod(uint a, uint b) public pure returns (uint) {
        require(b > 0, "Cannot modulo by zero");
        return a % b;
    }
    function power(uint a, uint b) public pure returns (uint) {
        return a ** b;
    }
    function sqrt(uint x) public pure returns (uint) {
        if (x == 0 || x == 1) return x;
        uint z = (x + 1) / 2;
        uint y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
        return y;
    }
}