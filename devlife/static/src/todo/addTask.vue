<style lang="scss" scoped>
  .add-task {
    margin: 0.5rem 0rem 1rem 0rem;
  }
</style>

<template>
  <div class="add-task">
    <div class="row">
      <div class="col-md-8">
        <form>
          <div class="form-group">
            <input id="title" class="form-control" type="text" placeholder="Task Title (Max 255 characters)">
          </div>
          <div class="form-group">
            <textarea id="description" class="form-control" type="text" placeholder="Task Description here..">
            </textarea>
          </div>
          <div class="form-group">
            <label for="due_date">Due Date:</label>
            <input id="due_date" class="form-control" type="date">
          </div>
          <div class="form-group">
            <label for="status">Task Status</label>
            <select class="form-control" name="" id="status">
              <option value="">Pending</option>
              <option value="">Done</option>
            </select>
          </div>
          <div class="form-group text-right">
            <button class="btn btn-success">Save</button>
          </div>
        </form>
      </div>
    </div>
    
  </div>
</template>

<script>
  export default {
    
  }
</script>
