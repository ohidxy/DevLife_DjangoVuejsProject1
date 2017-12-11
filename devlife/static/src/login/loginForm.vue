<style lang="scss" scoped>
  .login-form {
    margin: 4rem 2rem 4rem 2rem;
  }
</style>

<template>
  <div @submit.prevent="login" class="login-form">
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

      error: '',
    }
  },
  props: {
    loginUrl: {
      type: String,
      required: true,
    }
  },
  mounted() {
    this.$refs.loginInput.focus()
  },
  methods: {
    login() {
      if (!this.email || !this.password) {
        return
      }
      
      const { email, password } = this
      this.$http.post( 
        this.loginUrl,
        { email, password }
      ).then(res => {
        console.log("Login Success!")
      }).catch(e => {
        const data = e.response.data
        console.error(e.response)
        for (let errorType in data) {
          for (let error of data[errorType]) {
            this.error += `${error}\n`
          }
        }
      })
    }
  },

}
</script>

