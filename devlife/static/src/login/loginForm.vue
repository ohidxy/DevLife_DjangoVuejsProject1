<style lang="scss" scoped>
  .login-form {
    margin-top: 50px;
  }
</style>

<template>
  <div>
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6 login-form">
        <h1 class="text-center">Login Here</h1>
        <form action="">
          <div class="form-group">
            <label for="username">Username</label>
            <input class="form-control" type="text" id="username" placeholder="Username">
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input class="form-control" type="password" id="password" placeholder="Password">
          </div>
          <button class="btn btn-primary" type="submit">Login</button>
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

