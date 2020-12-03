import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router";
import router from "@/router/router";
import VueCookie from 'vue-cookie';

Vue.use(VueRouter)
Vue.use(VueCookie)

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
