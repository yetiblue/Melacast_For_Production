<template>
  <v-card class="pa-4 mb-4">
    <h2 class="title font-weight-thin">Change Password</h2>
    <p v-if="success" class="success--text">Password successfully reset.</p>

    <v-text-field
      v-model="current_password"
      :error-messages="errors.current_password"
      label="Current Password"
      type="password"
    />
    <v-text-field
      v-model="new_password"
      label="New Password"
      :error-messages="errors.new_password"
      type="password"
    />
    <v-text-field
      v-model="re_new_password"
      label="Re-type Password"
      :error-messages="errors.re_new_password"
      type="password"
    />
    <v-btn @click.stop="changePassword">Change Password</v-btn>
  </v-card>
</template>


<script>
export default {
  name: "ChangePasswordForm",
  data: () => ({
    current_password: "",
    new_password: "",
    re_new_password: "",
    reset: false,
    errors: {}
  }),
  methods: {
    changePassword() {
      this.errors = {};
      this.success = false;
      const formData = {
        current_password: this.current_password,
        new_password: this.new_password,
        re_new_Password: this.re_new_password
      };
      if (formData.new_password !== formData.re_new_password) {
        this.errors.re_new_password = "Password Must Match"; //IMPORTANT can manually set like this
        return;
      }
      this.$axios
        .post("/auth/users/set_password", formData)
        .then(response => {
          this.resetForm();
          this.success = true;
        })
        .catch(err => {
          this.errors = err.response.data;
        });
    },
    resetForm() {
      this.current_password = "";
      this.new_password = "";
      this.re_new_password = "";
    }
  }
};
</script>