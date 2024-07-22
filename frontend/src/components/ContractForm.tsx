import React, { useState } from 'react';
import { generateContract } from '../services/api';
import { TextField, Button, Typography, CircularProgress } from '@mui/material';

const ContractForm: React.FC = () => {
    const [userInput, setUserInput] = useState('');
    const [contractCode, setContractCode] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            const response = await generateContract(userInput);
            setContractCode(response.data.contract_code);
        } catch (err) {
            setError('Failed to generate contract. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <TextField 
                    label="Contract Requirements" 
                    variant="outlined" 
                    fullWidth 
                    value={userInput} 
                    onChange={(e) => setUserInput(e.target.value)} 
                    margin="normal"
                />
                <Button type="submit" variant="contained" color="primary" disabled={loading}>
                    {loading ? <CircularProgress size={24} /> : 'Generate Contract'}
                </Button>
            </form>
            {error && <Typography color="error">{error}</Typography>}
            {contractCode && <pre>{contractCode}</pre>}
        </div>
    );
};

export default ContractForm;
