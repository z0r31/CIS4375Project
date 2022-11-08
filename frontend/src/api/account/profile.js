//Get info profile to server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const profile = (callback ) => {

   axios.get(`${BASE_URL}/profile`, {})
      .then(res => {
         callback(res)
      })
      .catch(err => {
         console.log(err)
      })
}

export default profile