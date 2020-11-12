import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

import router from './router'

// import AudioRecorder from 'vue-audio-recorder'

import VueRecord from '@codekraft-studio/vue-record'

Vue.use(VueRecord)


// Vue.use(AudioRecorder)

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(Vuex)
console.log(process.env.ENTRYPOINT)
let baseURL = 'http://localhost:5000/api' //  'http://localhost:5000'  http://34.69.196.81/api  //Change depending on what you use
console.log(baseURL)

Vue.use({
  install (Vue){
    Vue.prototype.$api= axios.create({
      baseURL: baseURL
    })
  }
})

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {
    image: null
  },
  mutations: {
    replaceImage (state, newImage) {
      state.image = newImage
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
