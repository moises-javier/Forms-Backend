<template>
  <div class="box tab">
    <div class="columns">
      <div class="column is-6">
        <input
          :value="question"
          @input="$emit('update:question', $event.target.value)"
          class="inp border-bottom-q"
          type="text"
          placeholder="Question"
        />
      </div>
      <div class="column is-6">
        <div class="select w-100">
          <select
            :value="id_field_type"
            @change="fieldTypeChanged($event)"
            class="w-100"
          >
            <option value="1">Short answer text</option>
            <option value="2">Paragraph</option>
            <option value="3">Several Options</option>
          </select>
        </div>
      </div>
    </div>

    <div class="columns">
      <div class="column pt-0">
        <div v-if="id_field_type == 1">
          <input
            class="inp border-bottom-a"
            type="text"
            placeholder="Short answer text"
            disabled
          />
        </div>
        <div v-else-if="id_field_type == 2">
          <input
            class="inp border-bottom-a"
            type="text"
            placeholder="Paragraph"
            disabled
          />
        </div>
        <div class="several-options" v-else-if="id_field_type == 3">
          <div class="flex-center-v" v-for="(item, i) in options" :key="i">
            <span class="circle inline-block"></span>
            <input
              :value="item.option"
              @input="updateOption(item.id, $event.target.value)"
              class="inp inline-block fs-16"
              type="text"
              placeholder="Option"
            />

            <i
              @click="deleteOption(item.id)"
              class="fas fa-times fs-20 is-clickable ml-4"
            ></i>
          </div>
          <div class="mt-5 flex-center-v is-clickable" @click="addNewOption">
            <span class="circle inline-block"></span>
            <span class="ml-2 txt fs-16">Add option</span>
          </div>
        </div>
      </div>
    </div>

    <hr class="solid" />

    <div class="flex-center-v is-justify-content-end">
      <i @click="deleteQuestion" class="fas fa-trash-alt is-clickable mr-2"></i>
      <div class="vl mx-4"></div>
      <label :for="'required-' + question.id" class="mr-2 prevent-select"
        >Required</label
      >
      <label class="switch">
        <input :id="'required-' + question.id" type="checkbox" />
        <span class="slider round"></span>
      </label>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppItem",
  emits: [
    "update:question",
    "update:id_field_type",
    "updateOption",
    "deleteOption",
    "addOption",
    "deleteQuestion",
  ],
  props: ["id", "question", "id_field_type", "options"],
  methods: {
    fieldTypeChanged(e) {
      let _id = parseInt(e.target.value);
      if (_id == 3 && this.options.length === 0) {
        this.addNewOption();
      }
      this.$emit("update:id_field_type", _id);
    },
    addNewOption() {
      this.$emit("addOption", { id: this.id });
    },
    deleteOption(id) {
      this.$emit("deleteOption", { id_question: this.id, id_option: id });
    },
    updateOption(id, value) {
      this.$emit("updateOption", {
        id_question: this.id,
        id_option: id,
        option: value,
      });
    },
    deleteQuestion() {
      this.$emit("deleteQuestion", this.id);
    },
  },
};
</script>

<style scoped>
.inp {
  font-size: 18px;
}

.tab {
  border-left: 6px solid rgb(43, 115, 223);
}

.circle {
  height: 21px;
  width: 21px;
  background-color: #fff;
  border: 2px solid #bbb;
  border-radius: 50%;
  display: inline-block;
}

.flex-center-v span.txt {
  color: #9e9a9a;
}

.fs-16 {
  font-size: 16px;
}
.fs-20 {
  font-size: 20px;
}

.several-options > div:not(:first-child) {
  margin-top: 1rem;
}

hr.solid {
  border-top: 1px solid #dad7d7;
}

.vl {
  border-left: 1px solid #dad7d7;
  height: 30px;
}

.border-bottom-q {
  border-bottom: 1px solid #a5a5a5;
}

.border-bottom-a {
  background-color: transparent;
  border-bottom: 1px dotted #dad7d7;
}

/******************************************************************* */
/* The switch - the box around the slider */
.switch {
  position: relative;
  display: inline-block;
  width: 45px;
  height: 19px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 12px;
  width: 12px;
  left: 4px;
  bottom: 3.1px;
  background-color: white;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #2196f3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196f3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
