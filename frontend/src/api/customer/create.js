//create new product

import axios from 'axios'
import BASE_URL from '../BASE_URL.js'

const createCustomer = (body,mode) => {
    if(mode=="edit"){
        axios.put(`${BASE_URL}/api/customer/update`, body, {
            headers: {
             
            }
        })
            .then(res => {
                callback(true, res)
            })
            .catch(err => {
                console.log(err)
            })
    }else{
        axios.post(`${BASE_URL}/api/customer/add`, body, {
            headers: {
               
            }
        })
            .then(res => {
                callback(true, res)
            })
            .catch(err => {
                console.log(err)
            })
    }
    //Create fetch
  
}

export default createCustomer