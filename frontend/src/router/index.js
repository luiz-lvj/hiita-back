import Vue from 'vue';
import VueRouter from 'vue-router';
import Index from '../views/Index.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/Home',
    name: 'Home',
    component: () => import('../views/Home.vue'),
  },
  {
    path: '/LoginRegister',
    name: 'LoginRegister',
    component: () => import('../views/LoginRegister.vue'),
  },
  {
    path: '/Profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
