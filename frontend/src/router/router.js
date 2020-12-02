import VueRouter from "vue-router";
import LogIn from "@/views/LogIn";
import NotFoundComponent from "@/views/NotFoundComponent";
import MainPage from "@/views/MainPage";

export default new VueRouter({
  routes: [
    { path: '/login', component: LogIn },
    { path: '/404', component: NotFoundComponent },
    { path: '/', component: MainPage },
    { path: '*', redirect: '/404' }
  ],
  mode: 'history'
})