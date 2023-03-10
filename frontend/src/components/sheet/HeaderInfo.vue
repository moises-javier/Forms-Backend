<template>
  <div class="block">
    <div class="box">
      <div class="field">
        <div class="control">
          <input
            :value="title"
            @input="$emit('update:title', $event.target.value)"
            class="inp"
            type="text"
            placeholder="Form title"
          />
        </div>
      </div>
      <div class="field">
        <div class="control">
          <input
            :value="description"
            @input="$emit('update:description', $event.target.value)"
            class="inp desc"
            type="text"
            placeholder="Form description"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderInfo",
  emits: ["update:title", "update:description"],
  props: ["title", "description"],
};
</script>

<style scoped>
.block {
  border-top: 10px solid rgb(153, 88, 228);
}

.inp.desc {
  font-size: 15px;
}
</style>
