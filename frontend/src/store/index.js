import { createStore } from 'vuex'
import getters from './getters.js'
import mutations from './mutations.js'
import actions from './actions.js'

const store = createStore({
	state() {
		return {
			fullname: '',
			products: '',
			amountsOf: {
			  product: 0,
			  category: 0
			},
			deleteProduct: {
			   TOKEN: localStorage.getItem('TOKEN'),
			   id_product: '',
			   image_product: ''
			},
			updateProduct: {
			  id_product: '',
			  name_product: '',
			  price_product: '',
			  stock_product: '',
			  image_product: '',
			  category_product: '',
			  stock_unit: ''
			},
			currentCategory: 'All',
			keyword: '',
			updateCustomer: {
				CustomerFirstName: '',
				CustomerLastName: '',
				CustomerAddress: '',
				CustomerPhoneNumber: '',
				CustomerEmail: '',
				CountryID: '',
				CustomerID: ''
			  },
		}
	},
	getters,
	mutations,
	actions
})

export default store