<template>
  <section class="section" style="padding: 0;">
    <Navigation />

    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h2 class="title has-text-centered" style="color: #FAE8D3;">Sign Up</h2>

        <v-form>
          <div v-if="errorMsg" class="error--text">{{ errorMsg }}</div>
          <v-text-field
            v-model="form.username"
            label="Username"
            :error-messages="errors.username"
            name="username"
            type="text"
          />
          <v-text-field
            v-model="form.email"
            label="Email"
            :error-messages="errors.email"
            name="email"
            type="text"
          />
          <v-text-field
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
          rounded
          width="100%"
          color="#4d2600"
          dark
          @click.stop="register"
        >Register</v-btn>
      </div>
    </div>

    <!-- Attempt at a two-column layout. Failed because it did not take up the whole screen -->
    <!-- <v-container>
      <v-row no-gutters>
        <v-col>
          <v-card>Placeholder</v-card>
        </v-col>
        <v-col>
          <v-card>
            <div class="container">
          <div class="columns">
            <div class="column is-4 is-offset-4">
              <h2 class="title has-text-centered">Register!</h2>
              <v-form>
                <div v-if="errorMsg" class="error--text">{{ errorMsg }}</div>
                <v-text-field
                  v-model="form.username"
                  label="Username"
                  :error-messages="errors.username"
                  name="username"
                  type="text"
                />
                <v-text-field
                  v-model="form.email"
                  label="Email"
                  :error-messages="errors.email"
                  name="email"
                  type="text"
                />
                <v-text-field
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
                rounded
                width="100%"
                color="#4d2600"
                dark
                @click.stop="register"
                >Register</v-btn
              >
            </div>
          </div>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-container>-->
  </section>
</template>


<script>
import Navigation from "~/components/Navigation";
export default {
  middleware: "guest",
  components: {
    Navigation
  },
  data: () => ({
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
      ]
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