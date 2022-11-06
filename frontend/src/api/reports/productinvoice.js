//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const productinvoice = callback => {
   axios.get(`${BASE_URL}/reports/products_invoice`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default productinvoice