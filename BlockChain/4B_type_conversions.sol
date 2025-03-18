pragma solidity ^0.8.0;

contract TypeConversions {
    function convertInt(
        uint8 smallNumber
    ) public pure returns (uint256, uint8) {
        uint256 bigNumber = uint256(smallNumber);
        uint8 backToSmall = uint8(bigNumber);
        return (bigNumber, backToSmall);
    }

    function convertAddress(
        address addr
    ) public pure returns (uint160, address) {
        uint160 numericAddress = uint160(addr);
        address backToAddress = address(numericAddress);
        return (numericAddress, backToAddress);
    }

    function convertBytesToString(
        bytes32 data
    ) public pure returns (string memory) {
        return string(abi.encodePacked(data));
    }

    function convertUintToBytes(uint256 number) public pure returns (bytes32) {
        return bytes32(number);
    }

    function convertBytesToUint(bytes32 data) public pure returns (uint256) {
        return uint256(data);
    }
}
