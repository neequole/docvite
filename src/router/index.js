import Vue from 'vue'
import Router from 'vue-router'
import Resource from 'vue-resource'

import Home from '@/components/Home'
import Login from '@/components/Login'

Vue.use(Router)
Vue.use(Resource)

export default new Router({
    routes: [
        {path: '/',  component: Home},
        { path: '/login', component: Login},
        { path: '*', redirect: '/' }
    ],
    mode: 'history',
})
