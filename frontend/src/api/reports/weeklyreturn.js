//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const weeklyreturn = (body,callback) => {
   axios.post(`${BASE_URL}/reports/weekly_return`,body)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default weeklyreturn