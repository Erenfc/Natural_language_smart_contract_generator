pragma solidity ^0.8.0;

contract CustomContract {
    string public description;

    constructor(string memory _description) {
        description = _description;
    }

    {{ contract_code }}
}
