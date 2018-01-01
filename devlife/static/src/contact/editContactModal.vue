<style lang="scss" scoped>
  
</style>

<template>
 <div class="container">
    <!-- Modal -->
    <div class="modal fade" id="editContactModal" tabindex="-1" role="dialog" aria-labelledby="editContactModalLongTitle" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editContactModalLongTitle">Edit Contact</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form action="">
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="First Name *"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Last Name *" 
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Email *"
                  required
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="HP No (Handphone No)"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Twitter (URL)"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Github (URL)"
                >
              </div>
              <div class="form-group">
                <input 
                  class="form-control" 
                  type="text" 
                  placeholder="Company (Optional)"
                >
              </div>

              <div class="text-right">
                <button 
                  class="btn btn-success btn-right" 
                  type="submit"
                >
                Save
                </button>
                <button 
                  class="btn btn-danger btn-right" 
                  type="submit"
                >
                Delete
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
      single_contact_data: null,
      first_name: null,
      last_name: null,
      email: null,
    }
  },
  props: {
    apiUrl: {
      type: String,
      required: true
    }
  },
  methods: {
    view_single_contact(){
      // Make a request for a user with a given ID
      axios.get(this.apiUrl)
        .then((res) => {
          this.single_contact_data = res.data
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }
}
</script>
