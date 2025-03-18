pragma solidity ^0.8.0;

contract DecisionMaking {
    uint public age;
    function setAge(uint _age) public {
        age = _age;
    }

    function CheckVotingEligibility() public view returns (string memory) {
        if (age >= 18) {
            return "Eligible to vote";
        } else {
            return "Not Eligible to vote";
        }
    }
}