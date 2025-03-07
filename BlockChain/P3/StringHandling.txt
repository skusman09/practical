pragma solidity ^0.8.0;

contract StringHandling {

    string public text;

    function setText(string memory _text) public {
        text = _text;
    }

    function getText() public view returns (string memory) {
        return text;
    }
}