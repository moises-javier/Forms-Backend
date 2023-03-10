<template>
  <div class="wrapper">
    <div class="container is-max-desktop pt-4 px-5">
      <HeaderInfo
        v-model:title="title"
        v-model:description="description"
      ></HeaderInfo>
      <div
        v-for="(qstn, i) in questions"
        :key="qstn.id"
        class="block"
        :class="{ parent: current_id === qstn.id }"
      >
        <AppItem
          @click="selectedQuestion(questions[i].id)"
          @add-option="addNewOption"
          @update-option="updateOption"
          @delete-option="deleteOption"
          @delete-question="deleteQuestion"
          :id="questions[i].id"
          :options="questions[i].options"
          v-model:question="questions[i].question"
          v-model:id_field_type="questions[i].id_field_type"
        ></AppItem>
        <div v-if="current_id === qstn.id">
          <ToolBar @new-item="addEmptyQuestion" class="tool-bar"></ToolBar>
        </div>
      </div>

      <div
        @click="deleteForm"
        id="btn-delete"
        class="float-fixed is-clickable has-background-danger btn-float-fs"
      >
        <i class="fas fa-trash-alt"></i>
      </div>
      <div @click="save" class="float-fixed is-clickable btn-float-fs">
        <i class="fas fa-save"></i>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapStores } from "pinia";
import useGlobalStore from "@/stores/global";
import HeaderInfo from "@/components/sheet/HeaderInfo.vue";
import AppItem from "@/components/sheet/AppItem.vue";
import ToolBar from "@/components/sheet/ToolBar.vue";

export default {
  name: "AppSheet",
  computed: {
    ...mapStores(useGlobalStore),
  },
  components: {
    HeaderInfo,
    AppItem,
    ToolBar,
  },
  data() {
    return {
      id: null,
      title: "",
      description: "",
      questions: [],
      current_id: "",
    };
  },
  methods: {
    deleteQuestion(id) {
      setTimeout(() => {
        let foundIndex = this.questions.findIndex((x) => x.id == id);
        if (foundIndex > -1) {
          let i = foundIndex > 0 ? foundIndex - 1 : 0;
          this.selectedQuestion(this.questions[i].id);
          this.questions.splice(foundIndex, 1);
        }
      }, 400);
    },
    deleteOption(param) {
      let q_index = this.questions.findIndex((x) => x.id == param.id_question);
      if (q_index > -1) {
        let o_index = this.questions[q_index].options.findIndex(
          (x) => x.id == param.id_option
        );
        this.questions[q_index].options.splice(o_index, 1);
      }
    },
    addNewOption(qstn) {
      let foundIndex = this.questions.findIndex((x) => x.id == qstn.id);
      if (foundIndex > -1) {
        this.questions[foundIndex].options.push({
          id: this.makeid(3),
          option: "",
        });
      }
    },
    updateOption(param) {
      let q_index = this.questions.findIndex((x) => x.id == param.id_question);

      if (q_index > -1) {
        let o_index = this.questions[q_index].options.findIndex(
          (x) => x.id == param.id_option
        );
        if (o_index > -1) {
          this.questions[q_index].options[o_index].option = param.option;
        }
      }
    },
    selectedQuestion(id) {
      this.current_id = id;
    },
    addEmptyQuestion() {
      let id = this.makeid(4);
      this.questions.push({
        id: id,
        question: "",
        id_field_type: 0,
        options: [],
      });
      this.current_id = id;
    },
    makeid(length) {
      let result = "";
      const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
      const charactersLength = characters.length;
      let counter = 0;
      while (counter < length) {
        result += characters.charAt(
          Math.floor(Math.random() * charactersLength)
        );
        counter += 1;
      }
      return result;
    },
    loadQuestions(id) {
      let success_action = (response) => {
        if (response.status === 200) {
          let item = response.data;

          this.current_id = item.questions[item.questions.length - 1].id;
          this.id = item.id;
          this.title = item.title;
          this.description = item.description;
          this.questions = item.questions;
        }
      };

      let error_action = (error) => {
        console.log(error);
      };

      axios
        .get("http://127.0.0.1:5000/sheet/" + id)
        .then(success_action)
        .catch(error_action);
    },
    save() {
      let form = {
        title: this.title,
        description: this.description,
        id_sheet_type: 1,
        questions: this.questions.map((x) => {
          let qstn = {
            question: x.question,
            id_field_type: x.id_field_type,
          };

          if (!isNaN(x.id)) {
            qstn["id"] = x.id;
          }

          if (x.id_field_type === 3 && x.options.length > 0) {
            qstn["options"] = x.options.map((y) => {
              let optn = { option: y.option };
              if (!isNaN(y.id)) {
                optn["id"] = y.id;
              }
              return optn;
            });
          }

          return qstn;
        }),
      };

      let success_action = (response) => {
        if (response.status == 201 || response.status == 200) {
          this.$router.push({ name: "home" });
        }
      };

      let error_action = (error) => {
        console.log(error);
      };

      if (this.globalStore.idFormSelected) {
        axios
          .put("http://127.0.0.1:5000/sheet/" + this.id, form)
          .then(success_action)
          .catch(error_action);
      } else {
        axios
          .post("http://127.0.0.1:5000/sheet", form)
          .then(success_action)
          .catch(error_action);
      }
    },
    deleteForm() {
      let success_action = (response) => {
        if (response.status == 201 || response.status == 200) {
          this.$router.push({ name: "home" });
        }
      };

      let error_action = (error) => {
        console.log(error);
      };
      axios
        .delete("http://127.0.0.1:5000/sheet/" + this.id)
        .then(success_action)
        .catch(error_action);
    },
  },
  mounted() {
    if (this.globalStore.idFormSelected) {
      this.loadQuestions(this.globalStore.idFormSelected);
    } else {
      this.addEmptyQuestion();
    }
  },
};
</script>

<style scoped>
.wrapper {
  min-height: 100vh !important;
  background-color: #eaebfa !important;
  overflow: auto !important;
}

.parent {
  position: relative;
}

.btn-float-fs {
  font-size: 20px;
}
.float-fixed {
  position: fixed;
  width: 60px;
  height: 60px;
  bottom: 120px;
  right: 40px;
  background-color: #0c9;
  color: #fff;
  border-radius: 50px;
  text-align: center;
  box-shadow: 2px 2px 3px #999;
}

#btn-delete {
  bottom: 40px;
}
.float-fixed > i {
  margin-top: 20px;
}
</style>
