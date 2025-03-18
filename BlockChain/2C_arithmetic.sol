pragma solidity ^0.8.0;

contract ArithmeticOperatorsDemo
{
    uint public result;
    function add(uint a, uint b) public returns (uint)
    {
        result = a + b;
        return result;
    }
}