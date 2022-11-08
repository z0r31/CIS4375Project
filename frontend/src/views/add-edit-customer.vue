<template>
    <Navbar>
        <template v-slot:title-page>
            <h1 class="nav-title">Add/Edit Customers</h1>
        </template>
    </Navbar>
    <section class="show-slide mt-5 s-container">
        <section class="mt-5 s-container">
            <slot name="caption-form"></slot>
            <!-- alert -->
            <div v-if="isFailed" class="px-2 py-3 bg-red-300 mb-4 rounded-xl text-gray-50">
                <p>Action failed !!</p>
            </div>
            <!-- Form -->
            <form v-on:submit.prevent="submitForm()" class="form-wrapper mt-5" enctype="multipart/form-data">
                <div class="show-slide form-input mb-5">
                    <input v-model="form.CustomerFirstName" type="text" placeholder="First Name" />
                </div>
                <div class="show-slide form-input mb-5">
                    <input v-model="form.CustomerLastName" type="text" placeholder="Last Name" />
                </div>
                <div class="show-slide form-input mb-5">
                    <input v-model="form.CustomerEmail" type="text" placeholder="Email" />
                </div>
                <!-- Price of product -->
                <div class="show-slide form-input mb-5">
                    <input v-model="form.CustomerAddress" class="w-10/12" type="text" placeholder="Address" />
                </div>
                <!-- Category of product -->
                <div class="show-slide mb-3">
                    <select v-model="form.CountryID" class="select-form">
                        <option selected="true" value="0">Chose the country</option>
                        <template v-for="(item, index) in countryArr" :key="index">
                            <option class="px-3" :value="item.CountryID">{{ item.CountryName }}</option>
                        </template>
                    </select>
                </div>
                <!-- Stock of product -->
                <div class="show-slide form-input mb-3">
                    <input v-model="form.CustomerPhoneNumber" type="text" placeholder="Phone Number" maxlength="15" />
                </div>
                <!-- Form action -->
                <div class="show-slide btn-form mt-8 mb-3 text-xl">
                    <button :disabled="isFormValid.length > 0" class="bg-prussian-blue" type="submit">
                        <span
                            class="btn-active-label bg-prussian-blue duration-300 text-center rounded text-gray-100 w-5/12  px-2 py-1">
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

import { ref, watch, reactive, computed, onMounted } from 'vue'
import Navbar from '../components/Navbar.vue'
import countries from '../api/customer/country.js'
import createCustomer from '../api/customer/create.js'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

const store = useStore()
const router = useRouter()

const body = computed(() => {
    console.log(store.getters.updateCustomer)
      return store.getters.updateCustomer
   })



let customerId = router.currentRoute.value.query.customerid;
console.log('courseId', router.currentRoute.value.query.customerid)

const countryArr = ref('')
let mode='add';
const getCountry = (status, res) => {
    if (status) {
        countryArr.value = res.data
    }
}

onMounted(() => {
    countries(getCountry)
    //Get category from server
    //Get categorys from server and render to options
    let customerId = router.currentRoute.value.query.customerid;
    if (customerId != undefined) {
        mode = 'edit'
    }
    if (mode === 'edit') { 
         form.value.CustomerFirstName = body.value.CustomerFirstName
         form.value.CustomerLastName = body.value.CustomerLastName
         form.value.CustomerAddress = body.value.CustomerAddress
         form.value.CustomerPhoneNumber = body.value.CustomerPhoneNumber
         form.value.CustomerEmail = body.value.CustomerEmail
         form.value.CountryID = body.value.CountryID
         form.value.CustomerID = body.value.CustomerID
      }
      
    
})
const isLoad = ref(false)
const loadSuccess = ref(false)
const isFailed = ref(false)

const form = ref({
    CustomerFirstName: '',
    CustomerLastName: '',
    CustomerAddress: null,
    CustomerPhoneNumber: null,
    CustomerEmail: '',
    CountryID: '0',
})

let isFormValid = ref([false])
watch(form.value, () => {
    console.log(form.value);
    isFormValid.value = Object.values(form.value).filter(val => val === '' || val === null || val === '0')
})

 // Form actions 
 const submitForm = () => {
      setTimeout(() => {
         //Init FormData
         createCustomer(form.value,mode)
         setTimeout(() => {
            router.push({ name: 'customer' });   
         }, 1000);
         
         //Update
        //  const updateProduct = res => {
        //     //
        //     if (res.data.status === 200) {
        //        form.value.image_product = res.data.results.path
        //        form.value.id_product = body.value.id_product
        //        update(form.value, successLoad)
        //     }
        //  }
         //upload file
      }, 500)
   }


</script>