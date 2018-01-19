<style lang="scss" scoped>
  .task {
    border: solid 0.1rem #e6e600;
    padding: 0.5rem;
    background-color:#ffffe6;
    border-radius: 0.3rem;
  }

  .no-line-break {
    margin-top: 0.3rem;
    line-height: 0.3rem;
  }
</style>

<template>
  <div class="task">
    <div class="row">
      <div class="col-md-9 col-xs-9 no-line-break">
        <p><strong>Title: </strong> here you go the titles</p>
        <p><strong>Due Date: </strong> 01/02/2017. <strong>Status: </strong> pending</p>
        <p><strong>Description: </strong> here the description goes.....</p>
      </div>
      <div class="col-md-3 col-xs-3 text-right">
        <button class="btn btn-primary"><i class="fa fa-pencil-square-o fa-lg" aria-hidden="true"></i></button>
        <button class="btn btn-danger"><i class="fa fa-trash-o fa-lg" aria-hidden="true"></i></button>
        <button class="btn btn-success"><i class="fa fa-check-circle fa-lg" aria-hidden="true"></i></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>
