import { createRouter, createWebHistory } from 'vue-router';

import { useAuthStore, useAlertStore } from '@/stores';
import { Home } from '@/views';
import Ping from '../components/Ping.vue'
import accountsRoutes from './account.routes';
import userRoutes from './user.routes';


// export const router
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: 'active',
    routes: [
        //...
        { path: '/', name: 'home', component: Home },
        //{},
        //{},
        // landing page redirects
        { path: '/:pathMatch(.*)*', redirect: '/' },
        {
            path: '/ping',
            name: 'ping',
            component: Ping
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile
        },
        {
            path: '/user',
            name: 'user',
            component: User
        },
        {
            path: '/admin',
            name: 'admin',
            component: Admin
        }
    ],
})

// pinia state storage alert
router.beforeEach(async (to) => {
    // clear alert
    const alertStore = useAlertStore();
    alertStore.clear();
})

export default router
