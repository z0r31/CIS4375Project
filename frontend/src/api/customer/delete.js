//Delete category 
import axios from 'axios'
import BASE_URL from '../BASE_URL' 

const deleteCustomer = (key, callback, getCustomers) => {
   //Create data options
   const data = { CustomerID: key }
   
   const body = {
      CustomerID: key
   }
   
   
   //Fetch
   axios.delete(`${BASE_URL}/api/deleteCustomer`, {data})
      .then(res => {
         //Success
         if (res.data.status === 200) {
            callback(getCustomers)
         }
      })
      .catch(err => console.log(err))
}

export default deleteCustomer