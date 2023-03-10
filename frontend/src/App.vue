<template>
  <app-header></app-header>
  <router-view></router-view>
</template>

<script>
import AppHeader from "@/components/AppHeader.vue";

export default {
  name: "App",
  components: {
    AppHeader,
  },
};
</script>

<style>
body {
  background-color: #fff;
}
</style>
