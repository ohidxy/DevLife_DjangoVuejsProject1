// external
import Vue from 'vue'

import App from './app.vue'

import VueResource from "vue-resource"
Vue.use(VueResource);

new Vue(App).$mount('#app')