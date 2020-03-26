<template>
  <div class=container>
    <!-- NavBar -->
    <NavBar></NavBar>
    <hr>
    <br>
    <br>
    <div class="row">
      <div class="col-2"></div>
      <div class="col-8">
        <b-form @submit="login" @reset="onReset" v-if="show" action="#" submit.prevet="login">
          <b-form-group
            id="input-group-1"
            label="Email address:"
            label-for="input-1"
            description="We'll never share your email with anyone else.">

            <b-form-input
              id="email"
              v-model="form.email"
              type="email"
              required
              placeholder="Enter email"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Your Name:" label-for="name">
            <b-form-input
              id="name"
              v-model="form.name"
              required
              placeholder="Enter name"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Password:" label-for="password">
            <b-form-input
              id="password"
              type="password"
              name="password"
              v-model="form.password"
              required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
        <b-card class="mt-3" header="Form Data Result">
          <pre class="m-0">{{ form }}</pre>
        </b-card>
      </div>
      <div class="col-2"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';


export default {
  name: 'Login',
  components: {
    NavBar,
  },
  data() {
    return {
      form: {
        email: '',
        name: '',
        password: '',
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = '';
      this.form.name = '';
      this.form.password = '';
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      // BB - You don't need this to clear the form, because
      // BB - the above variables do it for you. I suspect validation state
      // BB - is someting else.
      // this.show = false;
      // this.$nextTick(() => {
      //   this.show = true;
      // });
    },
    login(evt) {
      evt.preventDefault();
      const path = 'http://172.21.14.152:5000/login';
      const payload = {
        email: this.form.email,
        password: this.form.password,
      };
      axios.post(path, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>
