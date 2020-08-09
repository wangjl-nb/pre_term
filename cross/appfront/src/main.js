import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Element from "element-ui";
import axios from "axios";
import 'element-ui/lib/theme-chalk/index.css';

axios.defaults.baseURL='http://127.0.0.1:8000'
axios.defaults.headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }

Vue.use(Element);
Vue.prototype.$axios = axios;

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
