<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Product Invoice</h1>
      </template>
   </Navbar>
   <section class="show-slide mt-20 s-container">

      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">Product Invoice</p>
         </div>
         <div class="mt-5">
            <div class="field col-12 md:col-4">
                <Calendar inputId="range" v-model="dates2" type="text" placeholder="Select Date Range"  selectionMode="range" :manualInput="false" />
                
                <Button type="button" label="Search"  @click="search()" />
            </div>
         
            <DataTable :value="categoryArr" class="p-datatable-sm" responsiveLayout="scroll">
               <Column field="CustomerName" header="Customer Name"></Column>
               <Column field="ProductName" header="Product Name"></Column>
               <Column field="Amount" header="Amount"></Column>
               <Column field="InvoiceDate" header="Invoice Date"></Column>
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
import productinvoice from '../../api/reports/productinvoice.js'


const categoryArr = ref('')
const dates2 = ref();
const getCustomers = (res) => {
      categoryArr.value = res.data.results
}
const search = (res) => {
   console.log(JSON.stringify(dates2.value[0]))
   let body={fromDate:dates2.value[0],toDate:dates2.value[1]}
   productinvoice(body,getCustomers)
}

onMounted(() => {
   //Get category from server
})
</script>