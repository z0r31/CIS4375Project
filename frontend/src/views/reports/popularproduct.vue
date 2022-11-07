<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Popular Products</h1>
      </template>
   </Navbar>
   <section class="show-slide mt-20 s-container">

      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">Popular Products</p>
         </div>
         <div class="mt-5">
            <DataTable :value="categoryArr" class="p-datatable-sm" responsiveLayout="scroll" dataKey="CustomerID">
               <Column field="ProductName" header="Product Name"></Column>
               <Column field="ProductDescription" header="Description"></Column>
               <Column field="MostPopularProduct" header="Most Popular Product"></Column>
               <Column field="Quantity" header="Quantity"></Column>
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
import popularproducts from '../../api/reports/popularproducts.js'

import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const router = useRouter()
const store = useStore()


const categoryArr = ref('')
const getCustomers = (res) => {
      categoryArr.value = res.data.results
}

onMounted(() => {
   //Get category from server
   popularproducts(getCustomers)
})




</script>