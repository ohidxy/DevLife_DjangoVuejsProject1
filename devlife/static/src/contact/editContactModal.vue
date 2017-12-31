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
            

              <div class="text-right">
                <button 
                  class="btn btn-success btn-right" 
                  type="submit"
                >
                Save
                </button>
              </div>
          
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

    }
  },
  props: {

  },
  methods: {
  }
}
</script>
