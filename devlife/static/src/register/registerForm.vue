<style lang="scss" scoped>
  .register-form{
    margin-top: 50px;
    margin-bottom: 50px;
  }
</style>

<template>
  <div>
    <div class="row">
      <div class="col-md-3"></div>
        <div class="col-md-6 register-form">
          <h1 class="text-center">Register Here</h1>
          <form action="">
            <div class="form-group">
              <label for="email">Email</label>
              <input class="form-control" type="text" id="email" placeholder="Email">
            </div>
            <div class="form-group">
              <label for="password">Password</label>
              <input class="form-control" type="password" id="password" placeholder="Password">
            </div>
            <div class="form-group">
              <label for="confirm_password">Confirm Password</label>
              <input class="form-control" type="password" id="confirm_password" placeholder="Password">
            </div>
            <button class="btn btn-primary" type="submit">Register</button>
          </form>
        </div>
      <div class="col-md-3"></div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>
