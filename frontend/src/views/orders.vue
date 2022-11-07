<template>
    <Navbar>
        <template v-slot:title-page>
            <h1 class="nav-title">Add/Edit Customers</h1>
        </template>
    </Navbar>
    <section class="show-slide mt-5 s-container">
        <section class="mt-5 s-container">
           <form v-on:submit.prevent="submitForm()" class="form-wrapper mt-5" enctype="multipart/form-data">
                <div class="show-slide mb-3">
                    <select v-model="form.CustomerID" class="select-form" >
                        <option selected="true" value="0">Choose the Customer</option>
                        <template v-for="(item, index) in categoryArr" :key="index">
                            <option class="px-3" :value="item.CustomerID">{{ item.CustomerFirstName }} {{
                                    item.CustomerLastName
                            }}
                            </option>
                        </template>
                    </select>
                </div>
                
                    <div class="show-slide form-input mb-3 flex flex-row">
                            <select v-model="form.ProductInventoryID" class="select-form basis-1/3"  @change="onChange($event)">
                                <option selected="true" value="0">Choose the Product</option>
                                <template v-for="(item, index) in productsArr" :key="index">
                                    <option class="px-3" :value="item.ProductInventoryID">{{ item.ProductName }} ({{item.Quantity}}) 
                                    </option>
                                </template>
                            </select>
                        <div style="margin-left: 10px;">
                            <input v-model="form.quantity"  type="text"
                                placeholder="Quantity" class="basis-1/4">
                        </div>

                    </div>
             
                <!-- <div class="show-slide btn-forms">
                    <button @click="addExperience" type="button" class="bg-prussian-blue">+ Add Product</button>
                </div> -->

              
                <div class="show-slide btn-form mt-8 mb-3 text-xl">
                    <button  class="bg-prussian-blue" type="submit">
                        <span
                            class="btn-active-label bg-prussian-blue duration-300 text-center rounded text-gray-100 w-5/12  px-2 py-1">
                            Submit
                        </span>
                    </button>
                </div>
            </form>
        </section>
    </section>
</template>
  
<script setup>

import { onMounted, ref, watch } from 'vue'
import Navbar from '../components/Navbar.vue'
import customers from '../api/customer/customers.js';
import products from '../api/products/products.js';
import createOrderInvoice from '../api/orders/createOrderInvoice.js'

const categoryArr = ref('')
const productsArr = ref('')
let CustomerID = 0;
let customerOrderID=0
var qty=0

const getCustomers = (status, res) => {
    if (status) {
        categoryArr.value = res.data
    }
}

const getProducts = (res) => {
        productsArr.value = res.data.results.filter(x=>x.Quantity > 0)
        form.value.CustomerID= 0
    form.value.ProductInventoryID= 0
    form.value.quantity=1
}

 const getCustomerOrder = (res,orders)  => {
    customerOrderID=res.data[0]['last_insert_id()'];
     if(customerOrderID > 0){
        console.log(orders)
            createOrderInvoice(orders,customerOrderID)
     }
   }

 const onChange=($event)=> {
            qty=+productsArr._value.filter(x=>x.ProductInventoryID==form.value.ProductInventoryID)[0].Quantity;
            console.log(qty)
        }

onMounted(() => {
    //Get category from server
    customers(getCustomers)
    setTimeout(() => {
      products(getProducts);  
    }, 1000);
},
)

const form = ref({
    CustomerID: 0,
    ProductInventoryID: 0,
    quantity:1
})

const submitForm = () => {
    form.value.quantity=qty-form.value.quantity;
      createOrder(form.value)
      setTimeout(() => {
      products(getProducts);  
    }, 1000);
   }

</script>
<script>
import createOrder from '../api/orders/create.js'
export default {
    
    data: () => ({
        product: [
            {
                ProductInventoryID: 0,
                quantity: 1
            }
        ]
        
    }),
    methods: {
        addExperience() {
            this.product.push({
                ProductInventoryID: 0,
                quantity: 1
            })
        },
        submit() {
            const data = {
                product: this.product,
                CustomerID:this.CustomerID
            }
            this.orders=data;
            createOrder(data,this.getCustomerOrder)
        }
    }
};
</script>
  
 