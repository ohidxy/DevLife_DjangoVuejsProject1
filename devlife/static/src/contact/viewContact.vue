<style lang="scss" scoped>
  .view-contact {
    margin: 0rem 0rem 1rem 0rem;
  }
  p {
    font-size: 0.9rem;
  }
</style>

<template>
<div class="view-contact">
  <div class="text-center" >
    <table class="table table-sm table-bordered table-hover">
      <thead>
        <tr>
          <th class="text-center">Full Name</th>
          <th class="text-center">Email</th>
          <th class="text-center">HP No</th>
          <th class="text-center">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contact in contacts_data" :key="contact.user">
          <td><p>{{ contact.first_name }} {{ contact.last_name }}</p></td>
          <td><p>{{ contact.email }}</p></td>
          <td><p>{{ contact.hp_no }}</p></td>
          <td class="text-center"><button class="btn btn-success btn-sm">View/Edit</button></td>
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
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
}
</script>