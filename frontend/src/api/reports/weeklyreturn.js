//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const weeklyreturn = callback => {
   axios.get(`${BASE_URL}/reports/weekly_return`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default weeklyreturn