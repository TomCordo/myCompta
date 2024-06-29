import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
});

export const signIn = (email: string, username: string, password: string) =>
    api.post('/users/', { email, username, password });

export const logIn = (email: string, password: string) =>
    api.post('/login/', { email, password });
