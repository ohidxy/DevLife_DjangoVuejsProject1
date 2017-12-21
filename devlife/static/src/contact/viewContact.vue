<style lang="scss" scoped>
  .view-contact {
    margin: 3rem 0rem 1rem 0rem;
  }
</style>

<template>
<div class="view-contact">
  <div class="text-right" style="margin-bottom:0.1rem">
    <button class="btn btn-primary">Add Contact</button>
  </div>
  <div class="text-center" >
    <table class="table table-striped table-bordered table-hover">
      <thead>
        <tr>
          <th>Full Name</th>
          <th>Email</th>
          <th>HP No</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>John Doe</td>
          <td>john@example.com</td>
          <td>01115633567</td>
        </tr>
        <tr>
          <td>Mary Moe</td>
          <td>mary@example.com</td>
          <td>0857343533</td>
        </tr>
        <tr>
          <td>July Dooley</td>
          <td>july@example.com</td>
          <td>0156968943</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  
}
</script>