<template>
   <Navbar>
      <template v-slot:title-page>
         <h1 class="nav-title">Customer</h1>
      </template>
   </Navbar>
   
   <section class="show-slide mt-20 s-container">
      <!-- List of categorys -->
      <div class="mt-5">
         <div class="mt-3 mb-5 text-xl flex justify-between items-center">
            <p class="font-semibold">All customers</p>
            <i class="fa fa-chevron-down"></i>
         </div>
         <!-- List -->
         <template v-for="(item, index) in categoryArr" :key="index">
            <div class="show-slide flex gap-3 justify-between mb-3">
               <span class="bg-gray-300 text-prussian-blue text-xl w-10/12 px-4 rounded-xl  py-3">{{ item.ProductDescription }}</span>
               <button @click="btnDeleteCategory(item.ProductDescription, item.ProductCategoryID)" class="btn-active-icon duration-300 bg-gray-500 text-gray-100 w-2/12 rounded-xl justify-center items-center" type="button">
                  <i class="fa fa-trash"></i>
               </button>
            </div>
         </template>
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
   
   import { reactive, onMounted, ref, watch } from 'vue'
   import Navbar from '../components/Navbar.vue'
   import categorys from '../api/category/categorys.js'
   import deleteCategory from '../api/category/delete.js'
   import createCategory from '../api/category/create.js'
   import updateCategory from '../api/category/update.js'
   
   const categoryArr = ref('')
   const getCategory = (status, res)  => {
      if ( status ) {
         categoryArr.value = res.data.results
      }
   }
   
   onMounted(() => {
      //Get category from server
      categorys(getCategory)
   })
   
   //Update category
   const emptyFormUpdate = ref(['null'])
   const formUpdate = ref({
      Old: '',
      New: ''
   })
   
   //Update handler
   const btnUpdateCategory = () => {
      setTimeout(() => {
         updateCategory(formUpdate.value.Old, formUpdate.value.New, categorys, getCategory)
         formUpdate.value.New = ''
      }, 500)
   }
   
   //Form update validation
   watch(formUpdate.value, () => {
      emptyFormUpdate.value = Object.values(formUpdate.value).filter(val => val === '0' || val === '')
   })
   
   //Form create new category
   const newCategory = ref('')
   const btnCreateCategory = () => {
      setTimeout(() => {
         createCategory(newCategory.value, categorys, getCategory)
         newCategory.value = ''
      }, 500)
   }
   
   //Button delete
   const btnDeleteCategory = (category, key) => {
      setTimeout(() => {
         deleteCategory(category, key, categorys, getCategory)
      }, 500)
   }
   
</script>