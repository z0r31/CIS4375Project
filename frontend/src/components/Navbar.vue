<template>
   <section style="z-index: 999" class="bg-prussian-blue fixed-navbar-wrapper">
     <div class="s-container dynamic-navbar-wrapper">

         <div @click="ProfileNav()" class="btn-active-label duration-300 text-gray-100 flex items-center text-xl">
               <p>Profile&ensp;</p>
         </div>

          <div @click="ProductsNav()" class="btn-active-label duration-300 text-gray-100 flex items-center text-xl">
               <p>Products&ensp;</p>
            </div>

         <div @click="CustomersNav()" class="btn-active-label duration-300 text-gray-100 flex items-center text-xl">
            <p>Customers&ensp;</p>
         </div> 

         <div @click="CategoryNav()" class="btn-active-label duration-300 text-gray-100 flex items-center text-xl">
            <p>Category&ensp;</p>
         </div> 


      </div>


   </section>
</template>

<style>

   @import "../style/components/navbar.css"

</style>

<script setup>

   import { useRouter } from 'vue-router'

    const router = useRouter()

   const ProfileNav = () => {
      setTimeout(() => {
         router.push('/profile')
      }, 500)
   }

   const ProductsNav = () => {
      setTimeout(() => {
         router.push('/')
      }, 500)
   }

   const CustomersNav = () => {
      setTimeout(() => {
         router.push('/customer')
      }, 500)
   }

     const CategoryNav = () => {
      setTimeout(() => {
         router.push('/category')
      }, 500)
   }


</script>
