//Remove image product from server
import axios from 'axios'
import BASE_URL from '../BASE_URL'

const removeFile = body => {
   //
   //console.log('remove file', body, callback)
   
   const data = { data: { image_product: body.image_product } }
   
   
   axios.delete(`${BASE_URL}/removeFile`, data)
      .then(res => {
         console.log(res)
      })
      .catch(err => {
         console.log(err)
      })
}

export default removeFile