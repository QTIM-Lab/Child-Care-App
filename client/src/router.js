import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from './components/HelloWorld.vue';
import Ping from './components/Ping.vue';


Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: HelloWorld,
    },
    // {
    //   path: '/ChildCareAsst/ChildCareAsst.html',
    //   name: 'ChildCareDetailsProvidedByMGH',
    //   component: ChildCareDetailsProvidedByMGH,
    // },
    // Test if backend is hooked up
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
