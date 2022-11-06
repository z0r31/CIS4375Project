//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const popularproducts = callback => {
   axios.get(`${BASE_URL}/reports/popular_products`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default popularproducts