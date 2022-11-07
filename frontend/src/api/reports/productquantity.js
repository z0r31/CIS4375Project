//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const productquantity = callback => {
   axios.get(`${BASE_URL}/reports/product_quantity`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default productquantity