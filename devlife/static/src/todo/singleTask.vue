<style lang="scss" scoped>
  .task {
    margin: 0.5rem 0 0 0;
    padding: 0.5rem;
    border-radius: 0.3rem;
    box-shadow: 0.1rem 0.2rem #f2f2f2;
  }

  .task:hover {
    border: solid 0.1rem #b3b3b3;
    background: #f2f2f2;
    cursor: pointer;
  }

  .pending {
    border: solid 0.1rem #e6e600;
    background: linear-gradient(to right, #ffffcc, #ffffe6);
  }
  
  .done {
    border: solid 0.1rem #88cc00;
    background: linear-gradient(to right, #eeffcc, #f7ffe6);
  }

  .no-line-break {
    margin-top: 0.3rem;
    line-height: 0.3rem;
  }

  button:hover, a:hover {
    cursor: pointer;
  }
</style>

<template>
  <div class="task done">
    <div class="row">
      <div class="col-md-9 col-xs-9 no-line-break">
        <p><strong>Title: </strong> {{ title }}</p>
        <p><strong>Due Date: </strong> {{ dueDate }}. <strong>Status: </strong> {{ status }} </p>
        <p><strong>Description: </strong> {{ description }} </p>
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
    data(){
      return {
      }
    },
    props: {
      title: {
        type: String,
        required: true,
      },
      description: {
        type: String,
        required: true,
      },
      dueDate: {
        required: true,
      },
      status: {
        type: String,
        required: true,
      }
    }
  }
</script>
