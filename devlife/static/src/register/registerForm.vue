<style lang="scss" scoped>
  .register-form{
    margin-top: 50px;
    margin-bottom: 50px;
  }
</style>

<template>
  <div class="register-form">
    <h1 class="text-center">Register Here</h1>
    <form action="">
      <div class="form-group">
        <label for="email">Email</label>
        <input 
          class="form-control" 
          type="text" 
          id="email" 
          placeholder="Enter your email here"
          v-model="email"
          ref="registerInput"
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
          class="form-control" 
          type="password" 
          id="password"
          placeholder="Enter a password"
          v-model="password1"
        >
      </div>
      <div class="form-group">
        <label for="confirm_password">Confirm Password</label>
        <input 
          class="form-control" 
          type="password" 
          id="confirm_password" 
          placeholder="Enter the password again."
          v-model="password2"
        >
      </div>
      <button 
        class="btn btn-primary" 
        type="submit"
      >
        Register
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: null,
      password1: null,
      password2: null,
    }
  },
  mounted() {
    this.$refs.registerInput.focus()
  }  
}
</script>
