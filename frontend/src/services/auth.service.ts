import axios from 'axios';

const API_URL = 'http://localhost:8080/api/auth/';

class AuthService {
    login(user) {
        return axios.post(API_URL + 'singin', {
            username: user.username,
            password: user.password
        })
    }
}
