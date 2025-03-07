pragma solidity ^0.8.20;

contract AbsoluteDifference {
    function absDiff(uint a, uint b) public pure returns (uint) {
        return a >= b ? a - b : b - a;
    }
}