<style lang="scss" scoped>

</style>

<template>
<div>
    <button-panel>
    </button-panel>
    <add-task>
    </add-task>
    <all-tasks>
    </all-tasks>
</div>
</template>

<script>
  import AddTask from './addTask.vue'
  import ButtonPanel from './buttonPanel.vue'
  import AllTasks from './allTasks.vue'
  export default {
    components: {
        ButtonPanel,
        AddTask,
        AllTasks,
    }
  }
</script>
