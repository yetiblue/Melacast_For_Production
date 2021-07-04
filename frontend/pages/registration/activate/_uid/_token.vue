<template>
  <v-app>
    <v-row class="align-center justify-center">
      <v-col cols="8">
        <v-card v-if="status === 'pending'" class="pa-8 text-center">
          <p class="title">Please wait</p>
          <p class="body-1">Checking registration status...</p>
        </v-card>
        <v-card v-if="status === 'success'" class="pa-8 text-center">
          <p class="title primary--text">Activation successful</p>
          <p class="body-1">You may now log in.</p>
          <v-btn color="primary" text to="/login">Log In</v-btn>
        </v-card>
        <v-card v-if="status === 'error'" class="pa-8 text-center">
          <p class="title error--text">Invalid activation token</p>
          <p class="body-1">This token is invalid. Please try again.</p>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
// import VueRouter from "vue-router";
// import Vue from "vue";
// Vue.use(VueRouter);
export default {
  auth: false,
  data: () => ({
    status: "pending"
  }),
  mounted() {
    this.$axios
      .post("/auth/users/activation/", this.$route.params)
      .then(response => {
        this.status = "success";
      })
      .catch(() => {
        this.status = "error";
      });
  },
  methods: {
    navigateToLogin() {
      window.alert("hello");
      this.$router.push("/login");
    }
  }
};
// const router = new VueRouter({
//   router: [{ path: "/registration/activate/:uid/:token" }]
// });
</script>