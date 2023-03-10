<template>
  <div class="card">
    <div class="btn mt-3" @click="newItem">
      <i class="fa fa-plus my-float"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "ToolBar",
  emits: ["newItem"],
  methods: {
    newItem() {
      this.$emit("newItem");
    },
  },
};
</script>

<style scoped>
.card {
  text-align: center;
}
.my-float {
  position: relative;
  top: -4px;
  font-size: 12px;
}

.btn {
  text-align: center;
  margin: 0 auto;
  width: 22px;
  height: 22px;
  border-radius: 50px;
  border: 2px solid #525252;
  cursor: pointer;
}
</style>
