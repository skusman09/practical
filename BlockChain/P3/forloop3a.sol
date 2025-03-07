pragma solidity ^0.8.0;

contract ForLoopExample {
    uint[] public evenNumbers;


    function storeEvenNumbers(uint n) public { 
        delete evenNumbers;
        for (uint i=1; i<=n; i++) {
            evenNumbers.push(i*2);

        }     
    }

         function sumFirstNumbers(uint n) public pure returns (uint) {
         uint sum=0;
         for (uint i = 1; i<=n; i++) {
             sum +=i;

         }
         return sum;
    }
}