//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const countries = callback => {
  
   
   axios.get(`${BASE_URL}/api/country`)
      .then(res => {
         callback(true, res)
      })
      .catch(err => console.log(err))
}

export default countries