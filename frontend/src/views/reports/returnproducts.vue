<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Retuned Products</h1>
      </template>
   </Navbar>
   <section class="show-slide mt-20 s-container">

      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">Retuned Products</p>
         </div>
         <div class="mt-5">
            <DataTable :value="categoryArr" class="p-datatable-sm" responsiveLayout="scroll">
               <Column field="ProductName" header="Product Name"></Column>
               <Column field="QuantityReturned" header="Quantity Returned"></Column>
               <Column field="ReturnReason" header="Return Reason"></Column>
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
import returnproducts from '../../api/reports/returnproducts.js'


const categoryArr = ref('')
const getCustomers = (res) => {
      categoryArr.value = res.data.results
}

onMounted(() => {
   //Get category from server
   returnproducts(getCustomers)
})




</script>