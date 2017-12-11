<style lang="scss" scoped>
  .login-form {
    margin-top: 50px;
    margin-bottom: 50px;
  }
</style>

<template>
  <div class="login-form">
    <h1 class="text-center">Login Here</h1>
    <form action="">
      <div class="form-group">
        <label for="username">Username</label>
        <input 
          class="form-control" 
          type="text" 
          id="username" 
          placeholder="Username"
          v-model="email"
          ref="loginInput"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
          class="form-control" 
          type="password" 
          id="password" 
          placeholder="Password"
          v-model="password"
        >
      </div>
      <button 
        class="btn btn-primary" 
        type="submit"
      >
        Login
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
    }
  },
  mounted() {
    this.$refs.loginInput.focus()
  },
}
</script>

