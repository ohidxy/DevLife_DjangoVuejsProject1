<style lang="scss" scoped>
  .login-form {
    margin: 4rem 2rem 4rem 2rem;
  }
</style>

<template>
  <div @submit.prevent="login" class="login-form">
    <h1 class="text-center">Login Here</h1>
    <form action="">
      <div class="form-group" action="/rest-auth/login/">
        <label for="username">Username</label>
        <input 
          class="form-control" 
          type="text" 
          id="username" 
          placeholder="Username"
          v-model="username"
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
import axios from 'axios'
// TODO further customise axios instance for DRY-ness
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  data() {
    return {
      username: '',
      password: '',
      error: '',
    }
  },
  props: {
    loginUrl: {
      type: String,
      required: true,
    },
  },
  mounted() {
    this.$refs.loginInput.focus()
  },
  methods: {
    login() {
      if (!this.username || !this.password) {
        return
      }
      const { username, password } = this
      
      axios.post(this.loginUrl, {
        "username": username,
        "password": password
      })
      .then(response => {
        console.log(response)
        window.location.reload()
      })
      .catch(e => {
        this.errors.push(e)
        console.log(e.data)
      })
    }
  },

}
</script>

