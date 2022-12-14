const getters = {
   
   fullname(state) {
      return state.fullname
   },
   products(state) {
     return state.products 
   },
   profile(state) {
     return {
        fullname: state.fullname,
        products: state.amountsOf.product,
        categorys: state.amountsOf.category
     } 
   },
   deleteProduct(state) {
     return state.deleteProduct
   },
   updateProduct(state) {
     return state.updateProduct 
   },
   TOKEN(state) {
     return state.deleteProduct.TOKEN
   },
   tableName(state) {
      return state.deleteModalValue.tableName
   },
   primaryKey(state) {
      return state.deleteModalValue.primaryKey
   },
   bodySearch(state) {
      return {
         keyword: state.keyword,
         category_product: state.currentCategory,
         TOKEN: localStorage.getItem('TOKEN')
      }
   },
   currentCategory(state) {
      return state.currentCategory
   },
   updateCustomer(state) {
      return state.updateCustomer 
    },
}

export default getters