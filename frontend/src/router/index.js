import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'
import BASE_URL from '../api/BASE_URL.js'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'
import UpdateProduct from '../views/UpdateProduct.vue'
import NewProduct from '../views/NewProduct.vue'
import Category from '../views/Category.vue'
import Customer from '../views/Customer.vue'
import addEditCustomer from '../views/add-edit-customer.vue'
import orders from '../views/orders.vue'
import popularproduct from '../views/reports/popularproduct.vue'
import productinvoice from '../views/reports/productinvoice.vue'
import returnproducts from '../views/reports/returnproducts.vue'
import bestemployee from '../views/reports/bestemployee.vue'
import valuedcustomer from '../views/reports/valuedcustomer.vue'
import productquantity from '../views/reports/productquantity.vue'
import importingdays from '../views/reports/importingdays.vue'
import weeklyreturn from '../views/reports/weeklyreturn.vue'
const routes = [
	{
		path: '/',
		name: 'home',
		component: Home
	},
	{
	   path: '/login',
	   name: 'login',
	   component: Login
	},
	{
	   path: '/profile',
	   name: 'profile',
	   component: Profile
	},
	{
	   path: '/update',
	   name: 'update',
	   component: UpdateProduct
	},
	{
	   path: '/new',
	   name: 'new',
	   component: NewProduct
	},
	{
	   path: '/category',
	   name: 'category',
	   component: Category
	},
	{
	   path: '/customer',
	   name: 'customer',
	   component: Customer
	},
	{
	   path: '/add-customer',
	   name: 'add-customer',
	   component: addEditCustomer
	},
	{
		path: '/edit-customer',
		name: 'edit-customer',
		component: addEditCustomer
	 },
	{
		path: '/orders',
		name: 'orders',
		component: orders
	 },
	{
		path: '/popularproduct',
		name: 'popularproduct',
		component: popularproduct
	 },
	{
		path: '/productinvoice',
		name: 'productinvoice',
		component: productinvoice
	 },
	{
		path: '/returnproducts',
		name: 'returnproducts',
		component: returnproducts
	 },
	{
		path: '/bestemployee',
		name: 'bestemployee',
		component: bestemployee
	 },
	 {
		path: '/valuedcustomer',
		name: 'valuedcustomer',
		component: valuedcustomer
	 },
	 {
		path: '/productquantity',
		name: 'productquantity',
		component: productquantity
	 },
	 {
		path: '/importingdays',
		name: 'importingdays',
		component: importingdays
	 },
	 {
		path: '/weeklyreturn',
		name: 'weeklyreturn',
		component: weeklyreturn
	 }
]
//createRouter
const router = createRouter({ history: createWebHistory(process.env.BASE_URL), routes })

//Navigation Guard
router.beforeEach((to, from, next) => {
   
   // create body
   const body = { TOKEN: null }
   localStorage.setItem('TOKEN','5befc834-62f4-4281-a71b-35c9067d8686')
   //Get token
   //From local storage if exist
   if ( localStorage.getItem('TOKEN') ) {
      body.TOKEN = localStorage.getItem('TOKEN')
   }
   next()
   //Authentication actions
//    axios.post(`${BASE_URL}/token`, body)
//       .then(res => {
//          if ( to.name !== 'login' && res.data.status !== 200 ) next({ name: 'login' })
//          else next()
//       })
//       .catch(err => {
//          console.log('error', err)
//       })
})

export default router