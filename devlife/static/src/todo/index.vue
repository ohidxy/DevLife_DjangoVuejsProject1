<style lang="scss" scoped>

</style>

<template>
<div>
    <div class="button-panel">
      <ul class="nav nav-tabs" role="tablist">
        <li class="nav-item">
          <button class="nav-link active" data-toggle="tab" href="#home" role="tab">All Tasks</button>
        </li>
        <li class="nav-item">
          <button class="nav-link" data-toggle="tab" href="#profile" role="tab">Add Task</button>
        </li>
      </ul>
    </div>
    <add-task>
    </add-task>
    <all-tasks>
    </all-tasks>
</div>
</template>

<script>
  import AddTask from './addTask.vue'
  import AllTasks from './allTasks.vue'
  export default {
    components: {
        AddTask,
        AllTasks,
    }
  }
</script>
