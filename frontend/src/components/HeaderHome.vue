<template>
   <section class="s-container">
      <!-- Fixed Header -->
      <div class="fixed-header-wrapper">
         <!-- Dynamic Header -->
         <div class="header-home-wrapper s-container">
             <Navbar></Navbar>
            <div @click="btnUserProfile()" class="btn-active-icon duration-300 bg-prussian-blue text-gray-100 flex justify-center items-center p-3 rounded-xl">
               <i class="fa fa-user"></i>
            </div>
         </div>
      </div>
      <div class="show-slide mt-5 text-2xl text-prussian-blue">
         <p>Welcome to <strong>KPJ Inventory Management App</strong> ,</p>
         <p>{{ fullname }}</p>
      </div>
   </section>
</template>

<style>

   @import "../style/components/header-home.css"
   
</style>

<script setup>
   
   import { useRouter } from 'vue-router'
   import Navbar from '../components/Navbar.vue'
   
   //The props
   defineProps({
      fullname: {
         type: String,
         default: 'Username'
      }
   })
   
   //Event handler for button profile
   const router = useRouter()
   const btnUserProfile = () => {
      setTimeout(() => {
         router.push({ name: 'profile' })
      }, 350)
   }
   
</script>