<template>
  <div>
    <section class="options">
      <div class="container is-max-widescreen">
        <div class="pt-4">
          <div>
            <span class="pl-3 has-text-weight-medium">Create new form</span>
          </div>
          <router-link class="btn-opt mt-4" :to="{ name: 'detail' }">
            <i class="fas fa-plus new-form"></i>
          </router-link>
          <div class="mt-1">
            <span class="label-info">Empty</span>
          </div>
        </div>
      </div>
    </section>
    <section class="mt-4">
      <div class="container is-max-widescreen">
        <div>
          <span class="has-text-weight-medium">Recent forms</span>
        </div>
        <div class="columns is-multiline mt-4">
          <div v-for="frm in forms" :key="frm.id" class="column is-one-fifth">
            <div class="card i-form" @click="selectedForm(frm)">
              <div
                class="card-content is-flex is-justify-content-center is-align-items-center"
              >
                <i class="fas fa-list-alt"></i>
              </div>
              <footer class="card-footer">
                <p class="card-footer-item">
                  <span class="form-title has-text-weight-medium">{{
                    frm.title
                  }}</span>
                </p>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import { mapStores } from "pinia";
import useGlobalStore from "@/stores/global";

export default {
  name: "HomeView",
  computed: {
    ...mapStores(useGlobalStore),
  },
  data() {
    return {
      forms: [],
    };
  },
  methods: {
    selectedForm(item) {
      this.globalStore.idForm = item.id;
      this.$router.push({ name: "detail" });
    },
    getData() {
      let success_action = (response) => {
        if (response.status === 200) {
          this.forms = response.data.items;
        }
      };

      let error_action = (error) => {
        console.log(error);
      };

      axios
        .get("http://127.0.0.1:5000/sheet")
        .then(success_action)
        .catch(error_action);
    },
  },
  mounted() {
    this.globalStore.idForm = null;
    this.getData();
  },
};
</script>

<style scoped>
.i-form {
  cursor: pointer;
}

.form-title {
  font-size: 14px;
}

.fa-list-alt {
  font-size: 50px;
}
.options {
  min-height: 250px;
  background-color: #eff0f1;
}

.btn-opt {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 170px;
  height: 125px;
  background-color: #fff;
  border-radius: 4%;
  border: 1px solid rgb(223, 223, 223);
  cursor: pointer;
  font-size: 2.5rem;
}

.btn-opt:hover,
.i-form:hover {
  outline: 2px solid rgb(171, 168, 202);
}

.new-form,
.label-info {
  color: rgb(121, 121, 121);
}

.label-info {
  font-size: 14px;
  font-weight: 500;
}

.card-content {
  min-height: 150px;
}
.card-footer-item {
  justify-content: left;
  margin-left: 5px;
}
</style>
