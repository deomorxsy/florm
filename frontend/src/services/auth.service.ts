import axios from 'axios';

const API_URL = 'http://localhost:8080/api/auth/';

class AuthService {
    login(user) {
        return axios.post(API_URL + 'singin', { // 1. POST {username, password}
            username: user.username,
            password: user.password
        })
        .then(response => {
            if (response.data.accessToken) { // 2. save JWT to localStorage
                localStorage.setItem('user', JSON.stringify(response.data));
            }

            return response.data;
        });
    }

    logout(){ // remove JWT from localStorage
        localStorage.removeItem('user')
    }
    register(user) { // POST {username, email, password}
        return axios.post(API_URL + 'signup', {
            username: user.username,
            email: user.email,
            password: user.password
        });
    }
}

export default new AuthService()
