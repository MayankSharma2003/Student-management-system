import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import login from './components/login.vue';
import signup from './components/signup.vue';
// import VueRouter from 'vue-router';

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
    // Other routes...
];

// Create the router instance
const router = createRouter({
    history: createWebHistory(),
    routes
});
// const router = new VueRouter({
//     mode: 'history',
//     base: process.env.BASE_URL,
//     routes
// });

export default router;
