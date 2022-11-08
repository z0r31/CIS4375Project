//BASE_URL
import BASE_URL from '../BASE_URL.js'
//AXIOS
import axios from 'axios'

// TOKEN API HANDLER
const login = (body, callback) => {
   //create connection to server
   callback(data)
   axios.post(`${BASE_URL}/token`, body)
      .then(res => {
         // response handler using callback
         const data = res.data
         
      })
      .catch(err => {
         console.error(err)
      }) 
}

export default login