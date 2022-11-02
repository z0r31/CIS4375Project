//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const customers = callback => {
   axios.get(`${BASE_URL}/api/customer`)
      .then(res => {
        console.log(res);
         //Success
        callback(true, res)
      })
      .catch(err => console.log(err))
}

export default customers