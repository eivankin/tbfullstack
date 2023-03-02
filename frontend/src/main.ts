import { createApp } from 'vue'
import App from './App.vue'
import VueMapboxTs from 'vue-mapbox-ts'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const app = createApp(App)

app.use(VueMapboxTs)

app.mount('#app')
