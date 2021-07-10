<template>
  <div>
    <v-app>
      <v-toolbar flat elevation="0">
        <div>
          <img class="mx-auto" height="200px" width="200px" src="../assets/images/horizontal.png" />
        </div>
        <v-spacer></v-spacer>
      </v-toolbar>
      <!-- First page -->
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-row class="justify-center align-center">
          <v-spacer></v-spacer>
          <v-col cols="10" sm="6" md="4">
            <v-card flat>
              <v-card-title class="ml-sm-n4">Tell Us About Yourself</v-card-title>
              <v-text-field
                outlined
                justify="center"
                :rules="nameRules"
                v-model="form.firstname"
                label="First Name"
              ></v-text-field>
              <v-text-field outlined justify="center" v-model="form.lastname" label="Last Name"></v-text-field>
              <v-text-field outlined justify="center" v-model="form.age" label="Age"></v-text-field>
              <v-select outlined v-model="form.gender" :items="genders" label="Gender Identity"></v-select>

              <v-text-field
                outlined
                v-model="form.languages_spoken"
                justify="center"
                label="Spoken Languages"
              ></v-text-field>
            </v-card>
            <v-card flat>
              <v-card-title class="ml-sm-n4">What is Your Race Identity?</v-card-title>
              <v-checkbox
                v-model="form.ethnicity"
                label="Native Hawaiian/Pacific Islander"
                color="brown"
                value="Native Hawaiian/Pacific Islander"
              ></v-checkbox>
              <v-checkbox
                v-model="form.ethnicity"
                label="Hispanic/Latino"
                color="brown"
                value="Hispanic/Latino"
              ></v-checkbox>
              <v-checkbox v-model="form.ethnicity" label="Asian" color="brown" value="Asian"></v-checkbox>
              <v-checkbox
                v-model="form.ethnicity"
                label="Middle Eastern"
                color="brown"
                value="Middle Eastern"
              ></v-checkbox>
              <v-checkbox
                v-model="form.ethnicity"
                label="Black/African American"
                color="brown"
                value="Black/African American"
              ></v-checkbox>
              <v-checkbox
                v-model="form.ethnicity"
                label="Native American/Alaskan Native"
                color="brown"
                value="Native American/Alaskan Native"
              ></v-checkbox>
            </v-card>
          </v-col>

          <v-spacer></v-spacer>
        </v-row>
        <v-row>
          <v-spacer></v-spacer>
          <v-col class="mt-lg-10 mt-sm-8 mb-16" cols="6" lg="3" sm="4">
            <v-btn
              elevation="0"
              class="brown white--text"
              height="5vh"
              @submit.prevent="submitProfile"
              block
            >Submit!</v-btn>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
      </v-form>
    </v-app>
    <FooterComponent />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";

export default {
  name: "Create Profile",
  computed: {
    uploadButtonSize() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return true;
        case "sm":
          return true;
        case "xs":
          return true;
        case "lg":
          return 150;
      }
    }
  },
  components: { FooterComponent, TopNavbar },
  methods: {
    submitProfile() {
      // chaining using .then since the post request isn't dependant on the true/false returned by validate()
      this.$refs.form.validate().then(
        this.$axios
          .post(`/api/v1/actors`, this.form)
          .then(response => {
            this.$router.push("/");
          })
          .catch(error => {
            if (error) {
              console.log(error, "ERROR WITH POST");
            }
          })
      );
    }
  },
  data() {
    return {
      genders: ["Female", "Male", "Non-Binary", "Prefer Not to Say"],
      unions: ["Non Union", "Union", "SAG", "Equity"],
      nameRules: [v => !!v || "Name is required"],
      email: "",
      emailRules: [v => !!v || "E-mail is required"],
      valid: true,

      form: {
        gender: null,
        firstname: null,
        lastname: null,
        age: null,
        ethnicity: null
      }
    };
  }
};
</script>
