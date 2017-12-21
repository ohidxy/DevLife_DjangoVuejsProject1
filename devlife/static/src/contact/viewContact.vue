<style lang="scss" scoped>
  .view-contact {
    margin: 3rem 0rem 1rem 0rem;
  }
</style>

<template>
<div class="view-contact">
  <div class="text-right" style="margin-bottom:0.1rem">
    <button class="btn btn-primary">Add Contact</button>
  </div>
  <div class="text-center" >
    <table class="table table-striped table-bordered table-hover">
      <thead>
        <tr>
          <th>Full Name</th>
          <th>Email</th>
          <th>HP No</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contact in contacts_data" :key="">
          <td>{{ contact.first_name }} {{ contact.last_name }}</td>
          <td>{{ contact.email }}</td>
          <td>{{ contact.hp_no }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      contacts_data: '',
    }
  },
  props: {
    apiUrl: {
      type: String,
      required: true,
    },
  },
  mounted(){
    this.view_all_contact()
  },
  methods: {
    view_all_contact(){
      // Make a request for a user with a given ID
      axios.get(this.apiUrl)
        .then((res) => {
          this.contacts_data = res.data
          console.log(this.contacts_data)
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
}
</script>