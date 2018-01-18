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
            class="nav-link active" data-toggle="tab" href="#home" role="tab"
            >All Tasks
          </button>
        </li>
        <li class="nav-item">
          <button 
            @click="selectedComponent = 'add-task'" 
            class="nav-link" data-toggle="tab" href="#profile" role="tab"
            >Add Task
          </button>
        </li>
      </ul>
    </div>
    
    <component :is="selectedComponent"></component>
    
    
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
    components: {
        AddTask,
        AllTasks,
    }
  }
</script>
