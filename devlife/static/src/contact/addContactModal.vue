<style lang="scss" scoped>
  .add-button {
    margin: 0.3rem 0rem 0.3rem 0rem;
  }
</style>

<template>
  <div class="container">
    <!-- Button trigger modal -->
    <div class="text-right">
    <button type="button" class="btn btn-primary text-right add-button" data-toggle="modal" data-target="#exampleModalLong">
      Add Contact
    </button>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLongTitle">Add Contact</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form action="">
              <div class="form-group">
                <input class="form-control" type="text" placeholder="First Name">
              </div>
              <div class="form-group">
                <input class="form-control" type="text" placeholder="Last Name">
              </div>
              <div class="form-group">
                <input class="form-control" type="text" placeholder="Email">
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>
