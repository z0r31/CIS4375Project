import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import './index.css'
import PrimeVue from 'primevue/config';
import DataTable from 'primevue/datatable';
import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions';
import Column from 'primevue/column';
import Button from 'primevue/button';


import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "./index.css";


const app = createApp(App);

app.use(store)
app.use(router)
app.use(PrimeVue)
app.component('Column', Column);
app.component('DataTable', DataTable)
app.component('DataView', DataView)
app.component('DataViewLayoutOptions', DataViewLayoutOptions)
app.component('Button', Button)
app.mount('#app')