<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Retuned Products</h1>
      </template>
   </Navbar>
   <section class="show-slide mt-20 s-container">

      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">Valued Customer</p>
         </div>
         <div class="mt-5">
            <DataTable :value="categoryArr" class="p-datatable-sm" responsiveLayout="scroll">
               <Column field="CustomerName" header="Customer Name"></Column>
               <Column field="Numberofpurchases" header="Number of purchases"></Column>
               <Column field="CustomerEmail" header="Customer Email"></Column>
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
import Navbar from '../../components/Navbar.vue'
import valuedcustomer from '../../api/reports/valuedcustomer.js'


const categoryArr = ref('')
const getCustomers = (res) => {
      categoryArr.value = res.data.results
}

onMounted(() => {
   //Get category from server
   valuedcustomer(getCustomers)
})




</script>