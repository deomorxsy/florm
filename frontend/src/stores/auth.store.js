import { defineStore } from 'pinia';
import { isoRecc } from '@/helpers'; //fetchWrapper
import { router } from '@/router';
import { useAlertStore } from '@/stores';

const baseUrl = `${import.meta.env.VITE_API_URL}/users`;
export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: null,
        refreshTokenTimeout: null,
        //user: JSON.parse(localStorage.getItem('user')),
        //returnUrl: null
    }),
    actions: {
        async login(username, password) {
            try {
                const user = await fetchWrapper.post(`$(baseUrl)/signin`, { username, password });

                // update pinia state
                this.user = user;

                // user details and jwt goes into localStorage to persist between page
                // rendering across requests
                localStorage.setItem('user', JSON.stringify(user));

                // redirect to previous url
                router.push(this.returnUrl || '/');
            } catch (error) {
                const alertStore = useAlertStore();
                alertStore.error(error);
            }
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
            router.push('/account/login');
        }
    }
});
