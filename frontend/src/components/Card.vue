<template>
   <section id="card" class="s-container">
      <!-- Section title -->
      <div class="mt-3 text-xl flex justify-between items-center">
         <p class="font-medium">Your Products</p>
         <i class="fa fa-chevron-down"></i>
      </div>
      
      <!-- State empty card -->
      <div class="mt-12" v-if="cards?.length <= 0">
         <p>Product not found, try to add new product or change the category</p>
      </div>
      
      <!-- Card wrapper -->
      <div class="card-wrapper">
         <template v-for="(card, index) in cards" :key="index">
            <div class="card flex flex-wrap flex-column flex-stretch show-slide">
               <!-- <img load="lazy" class="w-full" :src="card.image_product" :alt="card.image_product" /> -->
               <div class="pt-2 self-end pb-6 px-3 bg-white"  :class="{ 'bg-red-400': card.Quantity==0, 'text-danger': card.Quantity > 0 }">
                  <strong>{{ card.ProductName }}</strong>
                  <div class="flex mt-2">
                     <span>
                        <i class="mr-1 fas fa-dollar-sign"></i>
                        <small>{{ card.UnitPrice.toLocaleString() }}</small>
                     </span>
                     <span>
                        <i class="mr-1 fas fa-cubes ml-3"></i>
                        <small>{{ card.Quantity }}</small>
                     </span>
                  </div>
                  <div class="mt-4 w-full flex justify-between">
                     <span @click="btnUpdateProduct(
                        card.ProductInventoryID,
                        card.ProductName,
                        card.ProductDescription,
                        card.UnitPrice,
                        card.Quantity,
                        card.ProductCategoryID,
                        card.MaterialID
                     )" class="btn-active-label duration-300 block w-8/12 rounded bg-prussian-blue text-center text-sm py-1 text-gray-100">Update</span>
                     <!-- <span @click="btnDeleteProduct(card.ProductInventoryID, card.Image)" class="btn-active-icon duration-300 block w-3/12 rounded bg-gray-500 text-gray-100 flex justify-center items-center">
                        <i class="fa fa-trash text-sm"></i>
                     </span> -->
                  </div>
               </div>
            </div>
         </template>
      </div>
   </section>
</template>

<style scoped>
   
   @import "../style/components/card.css"
   
</style>

<script setup>
   
   import { reactive } from 'vue'
   import { useStore } from 'vuex'
   import { useRouter } from 'vue-router'
   
   //The props
   defineProps({
      cards: {
         default: []
      }
   })
   
   //init
   const store = useStore()
   const router = useRouter()
   const emits = defineEmits(['btnDeleteProduct'])
   
   //Save data about table name and primary key
   const deleteModalObj = reactive({
      tableName: '',
      primaryKey: ''
   })
   
   //Handler for button update
   const btnUpdateProduct = (ProductInventoryID, product_name, product_description, price_product, quantity, category_productId, MaterialID) => {
      //Save into state
      store.commit('setUpdateProduct', {
         ProductInventoryID: ProductInventoryID,
         product_name: product_name,
         product_description: product_description,
         price_product: price_product,
         quantity: quantity,
         category_productId: category_productId,
         MaterialID: MaterialID
      })
      //Push router to update views
      setTimeout(() => {
         router.push({ name: 'update' })
      }, 500)
   }
   
   //Handler for button delete
   const btnDeleteProduct = (key, file) => {
      
      //Passing data product into modal with save data into state
      store.commit('setDeleteProduct', { id_product: key, image_product: file })
      
      setTimeout(() => {
         emits('btnDeleteProduct')
      }, 500)
   }
   
</script>