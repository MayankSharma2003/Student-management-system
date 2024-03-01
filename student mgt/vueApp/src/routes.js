import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import login from './components/login.vue';
import signup from './components/signup.vue';
import admin   from './components/admin.vue';

const routes = [
    {
        path: '/',
        name: 'login',
        component: login
    },
    {
        path: '/signup',
        name: 'signup',
        component: signup
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path:'/admin', 
        name:'Admin',
        component:admin
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
