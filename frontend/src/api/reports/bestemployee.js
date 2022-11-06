//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const bestemployee = callback => {
   axios.get(`${BASE_URL}/reports/best_employee`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default bestemployee