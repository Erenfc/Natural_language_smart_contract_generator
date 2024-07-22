import React from 'react';
import ContractForm from './components/ContractForm';
import Header from './components/Header';

const App: React.FC = () => {
    return (
        <div className="App">
            <Header />
            <ContractForm />
        </div>
    );
};

export default App;
