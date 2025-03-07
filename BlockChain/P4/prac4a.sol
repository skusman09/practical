pragma solidity ^0.8.0;

contract StructDemo{
    struct Person{
        string name;
        uint age;
        address walletAddress;
    }

    Person[] public persons;

    mapping(address => Person) public personByAddress;

    function addPerson(string memory _name, uint _age) public{
        Person memory newPerson = Person(_name, _age, msg.sender);
        persons.push(newPerson);
        personByAddress[msg.sender] = newPerson;
    }
    function getPerson(address _walletAddress) public view returns(string memory, uint, address) {
        Person memory person = personByAddress[_walletAddress];
        return(person.name, person.age, person.walletAddress);
    }
}