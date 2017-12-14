<style lang="scss" scoped>
  .register-form{
    margin: 4rem 2rem 4rem 2rem;
    padding: 1rem;
    background: #ededed;
  }
</style>

<template>
  <div class="card card-outline-secondary register-form">
    <h1 class="text-center">Register Here</h1>
    <form @submit.prevent="register" action="">
      <div class="form-group">
        <label for="username">Username</label>
        <input 
          class="form-control" 
          type="text" 
          id="username" 
          placeholder="Enter your Username here"
          v-model="username"
          ref="registerInput"
        >
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input 
          class="form-control" 
          type="text" 
          id="email" 
          placeholder="Enter your email here"
          v-model="email"
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
      <div class="alert alert-danger" v-show="error">
        {{ error }}
      </div>
      <div class="text-right">
        <button 
          class="btn btn-primary" 
          type="submit"
        >
          Register
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
      error: null,
    }
  },
  mounted() {
    this.$refs.registerInput.focus()
  },
  methods: {
    register() {
      this.error=''
      if(!this.username || !this.email || !this.email || !this.password1 || !this.password2){
        this.error = 'Please, fill up all fields!'
      }   
    }
  }  
}
</script>
