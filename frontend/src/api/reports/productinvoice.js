//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const productinvoice = (body,callback) => {
   axios.post(`${BASE_URL}/reports/products_invoice`,body)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default productinvoice