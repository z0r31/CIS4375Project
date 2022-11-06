//Get all products to server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const products = (callback) => {
   // Send Token in headers
   axios.get(`${BASE_URL}/products`, {
      headers: {  
      }}).then(res => {
         console.log(res)
         callback(res)
      })
      .catch(err => {
         console.error(err)
      })
}

export default products