<template>
  <v-app>
    <div>
      <v-row>
        <!-- align-center won't work, this pushes everything down -->
        <v-card height="225px"></v-card>
      </v-row>
      <v-row class="justify-center">
        <v-col cols="10" sm="4">
          <img class="mx-auto mb-n2" height="225px" src="~/assets/images/horizontal.png" />
        </v-col>
      </v-row>

      <v-row>
        <v-spacer></v-spacer>
        <v-col class="px-10 px-sm-0" cols="12" sm="6" lg="4">
          <v-card class flat>
            <v-card-title class="justify-center mt-lg-n4">Join the Community</v-card-title>
          </v-card>
          <v-form>
            <div v-if="errorMsg" class="error--text">{{ errorMsg }}</div>
            <v-text-field
              outlined
              v-model="form.username"
              label="Username"
              :error-messages="errors.username"
              name="username"
              type="text"
            />
            <v-text-field
              outlined
              v-model="form.email"
              label="Email"
              :error-messages="errors.email"
              name="email"
              type="text"
            />
            <v-text-field
              outlined
              v-model="form.password"
              label="Password"
              :error-messages="errors.password"
              name="password"
              type="password"
              :rules="rules.password"
            />
          </v-form>
          <v-btn
            class="primary--text outlined"
            width="100%"
            color="#4d2600"
            dark
            @click.stop="register"
          >
            <h1 class="white--text">Register</h1>
          </v-btn>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
      <v-card flat>
        <v-card-title class="justify-center text-caption text-sm-subtitle-2 text-lg-subtitle-1">
          <v-checkbox
            v-model="agreeTerms"
            :error-messages="errors.checkbox"
            :rules="rules.checkbox"
          />I Agree to Melacast's Terms of Service and Privacy Policy
        </v-card-title>
        <v-card-subtitle class="text-center">
          <b class="black--text">Already have an account?</b>
          <a :href="`/login`">Log In</a>
        </v-card-subtitle>
      </v-card>
    </div>
  </v-app>
</template>


<script>
import Navigation from "~/components/Navigation";
export default {
  middleware: "guest",
  components: {
    Navigation
  },
  data: () => ({
    agreeTerms: false,
    errors: {},
    form: {
      username: null,
      email: null,
      password: null
    },
    rules: {
      password: [
        v =>
          (v && v.length > 8) || "The password must be longer than 8 characters"
      ],
      checkbox: [v => !!v || "You Must Agree to the Site's Terms to Continue!"]
    }
  }),
  computed: {
    errorMsg() {
      const errors = this.errors.non_field_errors;
      return errors && errors.length ? errors[0] : null;
    }
  },
  methods: {
    register() {
      this.errors = {};
      const formData = { ...this.form };
      this.$axios
        .post("/auth/users/", formData)
        .then(response => {
          this.$router.push("/registration/awaiting_confirmation/");
        })
        .catch(err => {
          this.$auth.logout();
          this.errors = err.response.data;
          this.errors.email = this.errors.username;
        });
    },
    preLoad() {
      this.$axios.get("/api/v1/actors").then(response => {
        this.$router.push("/registration/awaiting_confirmation/");
      });
    }
  }
};
</script>