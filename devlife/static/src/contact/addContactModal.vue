<style lang="scss" scoped>
  
</style>

<template>
  <div class="container">
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
            <form @submit.prevent="submitContact" action="">
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="First Name"
                  v-model="first_name"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Last Name" 
                  v-model="last_name"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Email" 
                  v-model="email"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Phone Number (Hp No)"
                  v-model="hp_no"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Twitter"
                  v-model="twitter"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Github"
                  v-model="github"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Company"
                  v-model="company"
                >
              </div>
              <div class="text-right">
                <button 
                  class="btn btn-success btn-right" 
                  type="submit"
                >
                Save
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// TODO further customise axios instance for DRY-ness
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export default {
  data () {
    return {
      first_name: '',
      last_name: '',
      email: '',
      hp_no: '',
      twitter: '',
      github: '',
      company: '',
      apiUrl: 'http://localhost:8000/contact/api/',
    }
  },
  props: {

  },
  methods: {
    submitContact() {
      const {
        first_name,
        last_name,
        email,
        hp_no,
        twitter,
        github,
        company
      } = this

      axios.post(this.apiUrl, {
        first_name,
        last_name,
        email,
        hp_no,
        twitter,
        github,
        company,
      })
      .then()
      .catch((err) => {
        console.log(err)
      });
    }
  }
}
</script>
