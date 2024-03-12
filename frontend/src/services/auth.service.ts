import axios from 'axios';

const API_URL = 'http://localhost:5000/auth/register';

class AuthService {
    handleSubmit = async (user: unknown): Promise<void> => {
         try {
            const response = await axios.post(API_URL, {
                username: user.username,
                password: user.password,
                first_name: user.first_name,
                last_name: user.last_name
            });
            return response.data
         } catch (error: unknown) {
             throw new Error(`Error in 'handleSubmit(${user})': ${error}`);
         }
    }

    register(user: schema) { // POST {username, email, password}
        return axios.post(API_URL + 'signup', {
            username: user.username,
            email: user.email,
            password: user.password
        });
    }
}

export default new AuthService()
