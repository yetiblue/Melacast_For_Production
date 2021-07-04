<template>
  <section class="section" style="padding: 0;">
    <!-- <Navigation /> -->
    <div class="container">
      <div class="columns">
        <div class="column is-4 is-offset-4">
          <div id="logo">
            <img src="../assets/images/horizontal.png" />
          </div>
          <h2 class="title has-text-centered" style="margin-bottom: 40px;">Welcome back!</h2>

          <v-form>
            <div class="field">
              <div class="control">
                <v-text-field
                  v-model="form.username"
                  name="username"
                  type="text"
                  outlined
                  placeholder="Username"
                  :error-messages="errors.non_field_errors"
                />
              </div>
            </div>

            <!-- <label class="label">Password</label> -->
            <v-text-field
              v-model="form.password"
              name="password"
              type="password"
              outlined
              placeholder="Password"
              :rules="rules.password"
              :error-messages="errors.non_field_errors"
            />
          </v-form>
        </div>
        <!-- <div class="has-text-centered" style="margin-top: 20px">
          <p>
            Don't have an account?
            <nuxt-link to="/registration">Register</nuxt-link>
          </p>
        </div>-->
      </div>
    </div>
    <!-- <v-btn class="error--text outlined" width="100%" @click.stop="forgot"
      >Forgot</v-btn
    >-->
    <br />
    <div style="display:flex; justify-content:center;">
      <v-btn class="primary--text outlined" id="login" @click.stop="login">Login</v-btn>
    </div>
    <br />
    <!-- <div style="display:flex; justify-content:center;">
      <v-btn class="error--text outlined" id="facebook" @click.stop="forgot">Continue With Facebook</v-btn>
    </div>-->
    <div style="display:flex; justify-content:center">
      <nuxt-link to="/forgot" style="color:#7a2c17;">Forgot password</nuxt-link>
    </div>
    <div class="has-text-centered" style="margin-top: 20px">
      <p style="font-weight:bold;">
        New to Melacast?
        <nuxt-link to="/registration" style="color:#7a2c17;">Create an account</nuxt-link>
      </p>
    </div>

    <!-- <Footer2 /> -->
  </section>
</template>

<style scoped>
section {
}

#logo {
  margin-top: 160px;
  margin-bottom: 30px;
}

.v-text-field {
  width: 454px;
}

#login,
#facebook {
  width: 454px;
  height: 36px;
  padding: 10px 15px 10px 14px;
  border-radius: 4px;
  background-color: #4d2600;
  color: white;
}

#facebook {
  background-color: #3b5998;
  margin-bottom: 20px;
}
</style>

<script>
// import Navigation from "~/components/Navigation";
// import Footer2 from "~/components/Footer2";

export default {
  middleware: "guest",
  components: {
    // Navigation,
    // Footer2
  },

  data: () => ({
    errors: {},
    form: {
      password: null,
      username: null
    },

    rules: {
      password: [
        v => (v && v.length > 8) || "Passwords are longer than 8 characters"
      ]
    }
  }),
  computed: {
    errorMsg() {
      const errors = this.errors.non_field_errors;
      return errors && errors.length ? errors[0] : null;
    }
  },
  mounted() {
    if (this.$auth.loggedIn) {
      this.$router.push("/dashboard");
    }
  },
  methods: {
    async login() {
      this.errors = {};
      try {
        await this.$auth.loginWith("local", {
          data: this.form
        });
        this.$router.push("/dashboard");
      } catch (err) {
        this.errors = err.response.data;
      }
    },
    forgot() {
      this.$router.push("/forgot");
    }
  }
};
</script>
