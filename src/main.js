// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import VueCookie from 'vue-cookie'

import {apiUrl} from './config'


Vue.use(Vuetify)
Vue.use(VueCookie)
Vue.config.productionTip = false
Vue.http.options.root = apiUrl
Vue.http.interceptors.push(function (request, next) {
    request.headers.set('x-csrftoken', Vue.cookie.get('csrftoken'))
    request.credentials = 'true'
    next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
