import { createApp } from 'vue';
//import './style.css'
import App from './App.vue';
import router from './router';
//import { store } from './stores/index';
//import store from './store';
import { createPinia } from 'pinia'

const pinia = createPinia()

createApp(App)
    .use(router)
    .use(pinia)
    .mount('#app');
