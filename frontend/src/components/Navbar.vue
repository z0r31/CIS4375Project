<template>
  <section style="z-index: 999" class="bg-prussian-blue fixed-navbar-wrapper">
    <div class="flex items-center"></div>
    <div class="s-container dynamic-navbar-wrapper">
      <img
        class="rounded-xl bg-prussian-blue"
        src="/icons/icon-144x144.png"
        alt="logo-stock"
        width="40"
      />
      <strong
        class="
          logo-text
          text-prussian-blue
          ml-2
          mr-5
          text-xl
          font-bold
          text-gray-100
        "
        >KPJ</strong
      >
      <div
        @click="Home()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Home&ensp;</p>
      </div>

      <div
        @click="ProductsNav()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Add Products&ensp;</p>
      </div>

      <div
        @click="CustomersNav()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Customers&ensp;</p>
      </div>

      <div
        @click="CategoryNav()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Category&ensp;</p>
      </div>
      <div
        @click="OrdersNav()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Order&ensp;</p>
      </div>
      <div
        @click="ProfileNav()"
        class="
          btn-active-label
          duration-300
          text-gray-100
          flex
          items-center
          text-xl
        "
      >
        <p>Profile&ensp;</p>
      </div>
      <Button
        type="button"
        label="Reports"
        @click="toggle"
        aria-haspopup="true"
        aria-controls="overlay_menu"
      />
      <Menu id="overlay_menu" ref="menu" :model="items" :popup="true" />
    </div>
  </section>
</template>

<style>
@import "../style/components/navbar.css";
</style>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const ProfileNav = () => {
  setTimeout(() => {
    router.push("/profile");
  }, 500);
};

const ProductsNav = () => {
  setTimeout(() => {
    router.push({ name: "new" });
  }, 500);
};

const CustomersNav = () => {
  setTimeout(() => {
    router.push("/customer");
  }, 500);
};

const CategoryNav = () => {
  setTimeout(() => {
    router.push("/category");
  }, 500);
};
const OrdersNav = () => {
  setTimeout(() => {
    router.push("/orders");
  }, 500);
};
const Home = () => {
  setTimeout(() => {
    router.push("/");
  }, 500);
};
</script>
<script>
export default {
  data() {
    return {
      items: [
        {
          label: "Popular products",
          command: () => {
            this.router.push({ name: "popularproduct" });
          },
        },
        {
          label: "Product invoice",
          command: () => {
            this.router.push({ name: "productinvoice" });
          },
        },
        {
          label: "Return Products",
          command: () => {
            this.router.push({ name: "returnproducts" });
          },
        },
        {
          label: "Best Employee",
          command: () => {
            this.router.push({ name: "bestemployee" });
          },
        },
        {
          label: "Valued Customer",
          command: () => {
            this.router.push({ name: "valuedcustomer" });
          },
        },
        {
          label: "Product Quantity",
          command: () => {
            this.router.push({ name: "productquantity" });
          },
        },
        {
          label: "Importing Days",
          command: () => {
            this.router.push({ name: "importingdays" });
          },
        },
        {
          label: "Return by Dates",
          command: () => {
            this.router.push({ name: "weeklyreturn" });
          },
        },
      ],
    };
  },
  methods: {
    toggle(event) {
      this.$refs.menu.toggle(event);
    },
    save() {
      this.$toast.add({
        severity: "success",
        summary: "Success",
        detail: "Data Saved",
        life: 3000,
      });
    },
  },
};
</script>