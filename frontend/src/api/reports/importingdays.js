//Get all category from server
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'

const importingdays = callback => {
   axios.get(`${BASE_URL}/reports/importing_days`)
      .then(res => {
        callback(res)
      })
      .catch(err => console.log(err))
}

export default importingdays