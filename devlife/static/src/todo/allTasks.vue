<style lang="scss" scoped>
  .all-task {
    margin: 1rem 0 0 0;
  }
</style>

<template>
  <div class="all-task">
    <single-task></single-task>
  </div>
</template>

<script>
  import SingleTask from './singleTask.vue'
  export default {
    components: {
      SingleTask,
    }
  }
</script>

