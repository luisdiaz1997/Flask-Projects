import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'

let baseURL = process.env.VUE_APP_BASEURL

Vue.use({
  install (Vue){
    Vue.prototype.$api= axios.create({
      baseURL: baseURL
    })
  }
})

Vue.config.productionTip = false;


Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
