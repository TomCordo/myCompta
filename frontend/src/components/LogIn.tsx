import React, { useState } from 'react';
import axios from 'axios';

const LogIn: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/login/', {
                email,
                password,
            });
            console.log(response.data);
            alert('User logged in successfully');
        } catch (error) {
            console.error(error);
            alert('Error logging in user');
        }
    };

    return (
        <div>
            <h2>Log In</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Log In</button>
            </form>
        </div>
    );
};

export default LogIn;
