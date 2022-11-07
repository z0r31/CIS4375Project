<template>
   <section class="mt-20 s-container">
      <slot name="caption-form"></slot>
      
      <!-- alert -->
      <div v-if="isFailed" class="px-2 py-3 bg-red-300 mb-4 rounded-xl text-gray-50">
         <p>Action failed !!</p>
      </div>
      
      <!-- Form -->
      <form v-on:submit.prevent="submitForm()" class="form-wrapper mt-10" enctype="multipart/form-data">
         <!-- Image of product -->
         <div class="show-slide mb-5 flex items-end gap-5">
            <img class="preview-item" :src="previewImg" width="100" alt="product" />
            <input ref="file" class="bg-gray-200 border border-gray-400 py-3 px-4 rounded-xl" @change="showPreview" name="file" type="file"/>
         </div>
         
         <!-- Name of product -->
         <div class="show-slide form-input mb-5">
            <input v-model="form.product_name" type="text" placeholder="Product Name" />
         </div>
         <div class="show-slide form-input mb-5">
            <input v-model="form.product_description" type="text" placeholder="Product Description" />
         </div>
         <!-- Price of product -->
         <div class="show-slide form-group mb-3 gap-3">
            <span class="btn-item bg-prussian-blue">
               <strong>USD</strong>
            </span>
            <input v-model="form.price_product" class="w-10/12" type="number" placeholder="Price per unit" />
         </div>
         <!-- Category of product -->
         <div class="show-slide mb-3">
            <select v-model="form.category_productId" class="select-form">
               <option selected="true" value="0">Chose the category</option>
               <template v-for="(item, index) in categoryArr" :key="index">
                  <option class="px-3" :value="item.ProductCategoryID">{{ item.ProductDescription }}</option>
               </template>
            </select>
         </div>
         <div class="show-slide mb-3">
            <select v-model="form.MaterialID" class="select-form">
               <option selected="true" value="0">Choose the material</option>
               <template v-for="(item, index) in MaterialArr" :key="index">
                  <option class="px-3" :value="item.MaterialID">{{ item.MaterialType }}, Karat: {{ item.Karat }} </option>
                 
               </template>
            </select>
         </div>
         <!-- Stock of product -->
         <div class="show-slide form-input mb-3">
            <input v-model="form.quantity" type="number" placeholder="Quantity" />
         </div>
        
         <div class="show-slide btn-form mt-8 mb-3 text-xl">
            <button :disabled="isFormValid.length > 0" class="bg-prussian-blue" type="submit">
               <span class="btn-active-label bg-prussian-blue duration-300 text-center rounded text-gray-100 w-5/12  px-2 py-1">
                  <template v-if="!isLoad && !loadSuccess">
                     Submit
                  </template>
                  <template v-else-if="isLoad && !loadSuccess">
                     <i class="spinner fas fa-spinner"></i>
                  </template>
                  <template v-else>
                     <i class="fa fa-check"></i>
                  </template>
            </span>
            </button>
         </div>
      </form>
   </section>
</template>

<script setup>
   
   import { ref, watch, reactive, computed, onMounted } from 'vue'
   import { useRoute,useRouter } from 'vue-router'
   import { useStore } from 'vuex'
   import upload from '../api/products/upload.js'
   import createProduct from '../api/products/create.js'
   import update from '../api/products/update.js'
   import removeFile from '../api/products/removeFile.js'
   import categorys from '../api/category/categorys.js'
   import materials from '../api/material/material.js'
   
   //Init router
   const route = useRoute()
   const router = useRouter()
   
   //Init store
   const store = useStore()
   
   //get current route name
   const currentRoute = computed(() => {
      return route.name
   })
   
   //Get state updateProduct
   const body = computed(() => {
      return store.getters.updateProduct
   })
   
   //indicator 
   const isForUpdate = ref(false)
   
   //List of category
   const categoryArr = ref('')
   const MaterialArr = ref('')
   
   onMounted(() => {
      
      //If currentRoute === 'update' , binding form with state
      if (currentRoute.value === 'update') { 
         console.log(body)
         isForUpdate.value = true
         form.value.product_name = body.value.product_name
         form.value.product_description = body.value.product_description
         form.value.price_product = body.value.price_product
         form.value.quantity = body.value.quantity
         form.value.category_productId = body.value.category_productId
         form.value.MaterialID = body.value.MaterialID
      }
      
      //Get categorys from server and render to options
      const getCategory = (status, res)  => {
         if ( status ) {
            categoryArr.value = res.data.results
            materials(getMaterial)
            // categoryArr.value.push({ category: 'uncategorys' })
         }
      }
      const getMaterial = (status, res)  => {
         if ( status ) {
            MaterialArr.value = res.data.results
         }
      }
      
      //Get category from server
      categorys(getCategory)
   })
   
   //Variabel for animated
   const isLoad = ref(false)
   const loadSuccess = ref(false)
   const isFailed = ref(false)
   
   //form use for create product
   const form = ref({
      product_name: '',
      product_description: '',
      price_product: 0,
      quantity: 0,
      category_productId: '0',
      MaterialID: '0'
   })
   
   //Form validation
   let isFormValid = ref([false])
   watch(form.value, () => {
      console.log(form.value);
      isFormValid.value = Object.values(form.value).filter(val => val === '' || val === null || val === '0')
   })
   
   //Get file
   let file = ref(null)
   
   //Image preview
   let previewImg = ref('/product.jpg')
   
   const showPreview = event => {
      
      form.value.image_product = 'true'
      
      //Init reader
      const reader = new FileReader()
      reader.onload = () => {
         previewImg.value = reader.result  
      }
      
      reader.readAsDataURL(event.target.files[0])
   }
   
   // Form actions 
   const submitForm = () => {
      
      isLoad.value = false
      loadSuccess.value = false
      setTimeout(() => {
         
         //Init FormData
         const formData = new FormData()
         formData.append('file', file.value.files[0])
         isLoad.value = true
         
         const successLoad = res => {
           router.push('/')
         }
         //Create
         const product = res => {
            if ( res.data.status === 200 ) {
               createProduct(form.value, successLoad)
            }
         }
         
         //Update
         const updateProduct = res => {
            //
            if (res.data.status === 200) {
               form.value.id_product = body.value.ProductInventoryID
               update(form.value, successLoad)               
            }
         }
         
         //upload file
         if ( !isForUpdate.value ) upload(formData ,product)
         else {
            form.value.id_product = body.value.ProductInventoryID
               update(form.value, successLoad)
         }
      
      }, 500)
   }
   
</script>

<style scoped>
   
   .preview-item {
      @apply rounded-xl border border-gray-400 ;
   }
   
</style>