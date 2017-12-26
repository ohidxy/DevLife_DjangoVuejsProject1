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
      <div id="status">
        <div class="alert alert-danger" v-show="errors.length">
          <p v-for="(error, index) in errors" :key="index">
            {{ error }}
          </p>
        </div>
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
import axios from 'axios'
// TODO further customise axios instance for DRY-ness
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
      errors: [],
    }
  },
  props: {
    registrationUrl: {
      type: String,
      required: true,
    },
  },
  mounted() {
    this.$refs.registerInput.focus()
  },
  methods: {
    register() {
      this.errors = []
      if(!this.username || !this.email || !this.password1 || !this.password2){
        this.errors.push('Please, fill up all fields!')
        return
      } 
      const {username, email, password1, password2} = this
      axios.post(this.registrationUrl,{
        username,
        email,
        password1,
        password2,
      }).then(res => {
        console.log('Registration Successful!')
      }).catch(err => {
        // console.log('There is error!')
        let errData = err.response.data
        console.log(errData)
        for (let errorType in errData) {
          for (let error of errData[errorType]) {
            this.errors.push(error)
          }
        }
      }) 
    }
  }  
}
</script>
