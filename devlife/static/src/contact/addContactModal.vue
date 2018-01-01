<style lang="scss" scoped>
  
</style>

<template>
  <div class="container">
    <!-- Modal -->
    <div class="modal fade" id="addContactModal" tabindex="-1" role="dialog" aria-labelledby="addContactModalLongTitle" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addContactModalLongTitle">Add Contact</h5>
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
                  placeholder="First Name *"
                  v-model="first_name"
                  ref="contactInput"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Last Name *" 
                  v-model="last_name"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Email *" 
                  v-model="email"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="HP No (Handphone No)"
                  v-model="hp_no"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Twitter (URL)"
                  v-model="twitter"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Github (URL)"
                  v-model="github"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Company (Optional)"
                  v-model="company"
                >
              </div>

              <div class="alert alert-success text-center" v-if="addContactSuccess">
                You have successfully added a contact!
              </div>
              <div class="alert alert-danger" v-show="errors.length">
                <div v-for="error in errors" :key="error">
                  {{error}}
                </div>
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
            <p class="text-center">* - mandatory field</p>
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
      addContactSuccess: false,
      errors: [],
    }
  },
  props: {
    apiUrl: {
      type: String,
      required: true
    }
  },
  mounted () {
    this.$refs.contactInput.focus()
  },
  methods: {
    submitContact() {
      this.errors = [] //reset the error in every submit
      this.addContactSuccess = false
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
      .then((res) => {
        this.addContactSuccess = true
        this.clearFields()   //Clears the fields on success
      })
      .catch((err) => {
        let errData = err.response.data
        let errTypeData = ''
        for (let errType in errData) {
          // console.log(errType, ': ')
          for (let value in errData[errType]){
            errTypeData = errType.toUpperCase().replace('_', ' ')
            this.errors.push(errTypeData + ': ' + errData[errType][value]) 
          }
        } 
      });
    },

    clearFields() {
      // This method for clearing the fields on success
      this.first_name = ''
      this.last_name = ''
      this.email = ''
      this.hp_no = ''
      this.twitter = ''
      this.github = ''
      this.company = ''
    }
  }
}
</script>
