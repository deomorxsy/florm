import { createRouter, createWebHistory } from 'vue-router';

import { useAuthStore, useAlertStore } from '@/stores';
import { HomeView } from '@/views';
import Ping from '../components/Ping.vue'
import accountsRoutes from './account.routes';
import userRoutes from './user.routes';
import { prependOnceListener } from 'process';


// export const router
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: 'active',
    routes: [
        //...
        { path: '/', name: 'home', component: HomeView },
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
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/policy',
            name: 'policy',
            component: Policy
        },
        {
            path: '/contact',
            name: 'contact',
            component: Contact
        },
        {
            path: '/register',
            name: 'register',
            component: HomeView
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
