//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const valuedcustomer = callback => {
   axios.get(`${BASE_URL}/reports/valued_customer`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default valuedcustomer