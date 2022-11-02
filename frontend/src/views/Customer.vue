<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Customers</h1>
      </template>
   </Navbar>
   <section class="show-slide mt-20 s-container">

      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">All customers</p>
            <Button label="+ Add New Customer" @click="addnewcustomer()"/>
         </div>
         <div class="mt-5">
            <DataTable :value="categoryArr" class="p-datatable-sm" responsiveLayout="scroll" dataKey="CustomerID">
               <Column field="CustomerFirstName" header="First Name"></Column>
               <Column field="CustomerLastName" header="Last Name"></Column>
               <Column field="CustomerPhoneNumber" header="Mobile"></Column>
               <Column field="CustomerAddress" header="Address"></Column>
               <Column headerStyle="width:10rem">
                  <template #body="slotProps">
                     <button @click="editnewcustomer(slotProps.data)"
                        class="btn-active-icon duration-300  w-2/12 rounded-xl justify-center items-center"
                        type="button">
                        <i class="fa fa-edit"></i>
                     </button>
                     <button @click="btnDeleteCustomer(slotProps.data.CustomerID)"
                        class="btn-active-icon duration-300   w-2/12 rounded-xl justify-center items-center"
                        type="button">
                        <i class="fa fa-trash"></i>
                     </button>  
                  </template>
               </Column>
            </DataTable>
         </div>

      </div>
      <!-- Create new category -->
   </section>
</template>

<style scoped>
.form-wrapper .btn-form:active {
   letter-spacing: 1.5px;
}

.form-wrapper .btn-form:disabled {
   opacity: .5;
}



.btn-active-icon:active {
   transform: scale(.85);
}
</style>

<script setup>

import { onMounted, ref, watch } from 'vue'
import Navbar from '../components/Navbar.vue'
import customers from '../api/customer/customers.js'
import deleteCustomer from '../api/customer/delete.js'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()


const categoryArr = ref('')
const getCustomers = (status, res) => {
   if (status) {
      categoryArr.value = res.data
   }
}

onMounted(() => {
   //Get category from server
   customers(getCustomers)
})

//Button delete
const btnDeleteCustomer = (CustomerID) => {
   setTimeout(() => {
      deleteCustomer(CustomerID, customers, getCustomers)
   }, 500)
}

const addnewcustomer = () => {
   router.push({ name: 'add-customer' });
}
const editnewcustomer = (data) => {
   store.commit('updateCustomer', data)
   router.push({ path: 'add-customer', query: { customerid: data.CustomerID }})
}

</script>