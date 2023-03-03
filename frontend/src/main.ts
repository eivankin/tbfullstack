import { createApp } from 'vue'
import App from './App.vue'
import VueMapboxTs from 'vue-mapbox-ts'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import { Tabs, Tab } from 'vue3-tabs-component'

const app = createApp(App)

app.use(VueMapboxTs)
app.component('tabs', Tabs)
app.component('tab', Tab)
app.mount('#app')
