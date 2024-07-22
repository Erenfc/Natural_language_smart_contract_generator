import React from 'react';

interface ContractDisplayProps {
    contractCode: string;
}

const ContractDisplay: React.FC<ContractDisplayProps> = ({ contractCode }) => {
    return <pre>{contractCode}</pre>;
};

export default ContractDisplay;
