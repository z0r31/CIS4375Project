//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const categorys = callback => {
   //Get TOKEN
   axios.get(`${BASE_URL}/categorys`)
      .then(res => {
         //Success
         if ( res.status === 200 ) callback(true, res)
      })
      .catch(err => console.log(err))
}

export default categorys