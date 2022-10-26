//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const materials = callback => {
   //Get TOKEN
   const headers = { headers: { token: localStorage.getItem('TOKEN') } }
   
   axios.get(`${BASE_URL}/materials`, headers)
      .then(res => {
         //Success
         if ( res.status === 200 ) callback(true, res)
      })
      .catch(err => console.log(err))
}

export default materials