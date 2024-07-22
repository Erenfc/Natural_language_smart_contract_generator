import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5000',
});

export const generateContract = (userInput: string) => {
    return api.post('/generate_contract', { user_input: userInput });
};
