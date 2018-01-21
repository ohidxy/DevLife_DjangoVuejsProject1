<style lang="scss" scoped>
  .all-task {
    margin: 1rem 0 0 0;
  }
</style>

<template>
  <div class="all-task">

      <single-task
        v-for="(task,index) in task_data" :key="index"
        :title="task.title"
        :description="task.description"
        due-date="12/05/2018"
        status="task.status"
      >
      </single-task>

  </div>
</template>

<script>
  import axios from 'axios'
  import SingleTask from './singleTask.vue'
  
  export default {
    components: {
      SingleTask,
    },
    data() {
      return {
        task_data: null,
        no_task: true,
      }
    },
    props: {
      apiUrl: {
        type: String,
        required: true
      }
    },
    mounted(){
      this.get_all_data()
    },
    methods: {
      get_all_data() {
        axios.get(this.apiUrl)
        .then((res) => {
          this.task_data = res.data
          if (this.task_data.length===0){
            this.no_task = true
          }else {
            this.no_task = false
          }
        })
        .catch((err) => {
          //yet to finish
        });
      }
    },
  }
</script>

