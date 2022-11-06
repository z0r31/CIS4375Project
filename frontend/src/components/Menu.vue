<template>
   <ul class="flex show-slide s-container mb-6 mt-20" id="menu">
      <li class="flex-1 mr-2">
         <div @click="btnNewProduc()" class="text-center block border border-blue-100 rounded py-2 px-4  hover:bg-blue-200 text-black">New product</div>
      </li>
      <li class="flex-1 mr-2">
         <div @click="btnManageCategory()" class="text-center block border border-blue-100 rounded py-2 px-4  hover:bg-blue-200 text-black">Manage category</div>
      </li>
      <li class="flex-1 mr-2">
         <div @click="btnCustomers()" class="text-center block border border-blue-100 rounded py-2 px-4  hover:bg-blue-200 text-black">Customers</div>
      </li>
      <li class="flex-1 mr-2">
         <div @click="btnOrders()" class="text-center block border border-blue-100 rounded py-2 px-4  hover:bg-blue-200 text-black">Order</div>
      </li>
   </ul>
   <hr />
</template>

<script setup>

import { useRouter } from 'vue-router'

const router = useRouter()

//Handler for new item menu
const btnNewProduc = () => {
   setTimeout(() => {
      router.push({ name: 'new' })
   }, 500)
}

//Handler for manage category menu
const btnManageCategory = () => {
   setTimeout(() => {
      router.push({ name: 'category' })
   }, 500)
}

const btnCustomers = () => {
   setTimeout(() => {
      router.push({ name: 'customer' })
   }, 500)
}
const btnOrders = () => {
   setTimeout(() => {
      router.push({ name: 'orders' })
   }, 500)
}

</script>

<style>
#menu .label {
   @apply flex items-center justify-center w-2/12 text-gray-100 px-3 py-4 rounded-xl;
}

#menu .label-wrapper {
   @apply flex items-center gap-3 duration-300;
}
</style>