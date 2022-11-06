const mutations = {
   
   setFullname (state, payload) {
		state.fullname = payload
	},
	setProducts (state, payload) {
	   state.products = payload
	},
	setAmountsOf (state, payload) {
	  state.amountsOf.product = payload.product 
	  state.amountsOf.category = payload.category 
	},
	setDeleteProduct (state, payload) {
	   state.deleteProduct.id_product = payload.id_product
	   state.deleteProduct.image_product = payload.image_product
	},
	setUpdateProduct (state, payload) {
	  const body = state.updateProduct
	  //Binding data
	  body.ProductInventoryID = payload.ProductInventoryID
	  body.product_name = payload.product_name
	  body.product_description = payload.product_description
	  body.price_product = payload.price_product
	  body.quantity = payload.quantity
	  body.category_productId = payload.category_productId
	  body.MaterialID = payload.MaterialID
	},
	setCurrentCategory (state, payload) {
	   state.currentCategory = payload
	},
	setKeyword (state, payload) {
	   state.keyword = payload
	},
	updateCustomer (state, payload) {
		const body = state.updateCustomer
		//Binding data
		body.CustomerFirstName = payload.CustomerFirstName
		body.CustomerLastName = payload.CustomerLastName
		body.CustomerAddress = payload.CustomerAddress
		body.CustomerPhoneNumber = payload.CustomerPhoneNumber
		body.CustomerEmail = payload.CustomerEmail
		body.CountryID = payload.CountryID
		body.CustomerID = payload.CustomerID
	  },
}

export default mutations