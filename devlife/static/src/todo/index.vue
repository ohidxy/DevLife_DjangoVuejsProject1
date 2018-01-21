<style lang="scss" scoped>
    .todo {
      margin: 0.5rem 0rem 1rem 0rem;
    }
</style>

<template>
<div class="todo">
    <div class="button-panel">
      <ul class="nav nav-tabs" role="tablist">
        <li class="nav-item">
          <button 
            @click="selectedComponent = 'all-tasks'" 
            class="nav-link active" data-toggle="tab" role="tab"
            >All Tasks
          </button>
        </li>
        <li class="nav-item">
          <button 
            @click="selectedComponent = 'add-task'" 
            class="nav-link" data-toggle="tab" role="tab"
            >Add Task
          </button>
        </li>
      </ul>
    </div>
    
    <!-- Non-alive component as we want to refresh everytime -->
    <component :is="selectedComponent" :api-url="apiUrl"></component>
    
    
</div>
</template>

<script>
  import AddTask from './addTask.vue'
  import AllTasks from './allTasks.vue'
  export default {
    data() {
      return {
        selectedComponent: 'all-tasks',
      }
    },
    props: {
      apiUrl: {
        type: String,
        required: true,
      }
    },
    components: {
        AddTask,
        AllTasks,
    }
  }
</script>
