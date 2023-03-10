import { defineStore } from "pinia";

export default defineStore("global", {
  state: () => ({
    idForm: 0,
  }),
  getters: {
    idFormSelected(state) {
      return state.idForm;
    },
  },
});
