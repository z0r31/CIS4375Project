//Create new category
import BASE_URL from '../BASE_URL.js'
import axios from 'axios'


const createOrderInvoice = (orders, customerOrderID) => {
    //Create body
    const body = { orders, customerOrderID }
    //Fetch
    axios.post(`${BASE_URL}/api/orderinvoice/add`, body)
        .then(res => {
            callback(res)
        })
        .catch(err => console.log(err))
}

export default createOrderInvoice