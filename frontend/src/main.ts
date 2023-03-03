import { createApp } from 'vue'
import App from './App.vue'
import VueMapboxTs from 'vue-mapbox-ts'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { Tabs, Tab } from 'vue3-tabs-component'
import mitt from 'mitt'
const emitter = mitt()

const app = createApp(App)

app.use(VueMapboxTs)
app.component('tabs', Tabs)
app.component('tab', Tab)
app.config.globalProperties.emitter = emitter
app.mount('#app')
