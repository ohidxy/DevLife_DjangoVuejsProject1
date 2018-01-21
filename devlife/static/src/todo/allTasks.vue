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
        status="pending"
      >
      </single-task>

  </div>
</template>

<script>
  import SingleTask from './singleTask.vue'
  export default {
    data() {
      return {
        task_data: {
          task1 : {
            title: 'this is title 1',
            description: 'this is the description of title 1'
          },
          task2 : {
            title: 'this is title 2',
            description: 'this is the description of title 2'
          }
        },
      }
    },
    props: {
      apiUrl: {
        type: String,
        required: true
      }
    },
    components: {
      SingleTask,
    }
  }
</script>

