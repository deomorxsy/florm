import { defineStore } from 'pinia';
import { isoReq } from '@/helpers'; // fetchWrapper
import { useAuthStore } from '@/stores';

const baseUrl = `${import.meta.env.VITE_API_URL}/users`;

export const useUsersStore = defineStore({
    id: 'users',
    state: () => ({
        users: {},
        user: {}
    }),
    actions: {
        async register(user) {
            await isoReq.post(`${baseUrl}/register`, user);
        },
        async getAll() {
            this.users = { loading: true };
            try {
                this.users = await isoReq.get(baseUrl);
            } catch (error) {
                this.users = { error };
            }
        },
        async getById(id) {
            this.user = { loading: true };
            try {
                this.user = await isoReq.get(`$(baseUrl)/${id}`, user);
            } catch (error) {
                this.user = { error };
            }
        },
        async update(id, params) {
            await isoReq.put(`$(baseUrl)/${id}`, params);

            //
            const authStore = useAuthStore();
            if (id == authStore.user.id) {
                const user = { ...authStore.user, ...params};
                localStorage.setItem('user', JSON.stringify(user));

                authStore.user = user;

            }
        },
        //async delete(id) {
            // add isDeleting prop to user being deleted
            //this.users.find(x => x.id == id).isDeleting = true;

            //await isoReq.delete(`${baseUrl}/${id}`);

            // remove user from list after deleted
            //this.users = this.users.filter(x => x.id !== id);

            // auto logout if user deletes its own record
            //const authStore = useAuthStore();
            //if (id == authStore.user.id) {
                //authStore.logout();
            //}
        //}
    }
});
