pragma solidity ^0.8.0;

contract WhileLoopExample {
    uint[] public evenNumbers;

    function storeEvenNumbers(uint n) public {
        delete evenNumbers;
        uint i = 1;
        while (i <=n) {
            evenNumbers.push(i*2);
            i++;
        }
    }

    function sumfirstNumbers(uint n) public pure returns (uint) {
        uint sum = 0;
        uint i = 1;
        while (i<=n){
            sum += i;
            i++;
        }
        return sum;
    }
}
