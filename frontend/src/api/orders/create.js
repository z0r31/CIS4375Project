//Create new category
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const createOrder = (orders) => {
   //Create body
   const body = { orders }
   //Fetch
   axios.post(`${BASE_URL}/api/customerorder/add`, body)
      .then(res => {
         
      })
      .catch(err => console.log(err))
}



export default createOrder




