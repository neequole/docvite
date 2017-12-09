// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
// import cookie from 'cookie'

Vue.use(Vuetify)
Vue.config.productionTip = false
// Vue.http.interceptors.push((request, next) => {
//     request.headers.set('x-csrftoken', cookie.parse(document.cookie)['csrftoken'])
//     next()
// })

const API_URL = 'http://localhost:8000/api'
Vue.prototype.$DOCTOR_API_URL = API_URL + '/doctors/'
Vue.prototype.$CLIENT_API_URL = API_URL + '/clients/'
Vue.prototype.$INVITATION_API_URL = API_URL + '/invitation/'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
