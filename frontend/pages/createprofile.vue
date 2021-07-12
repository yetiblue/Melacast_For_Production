<template>
  <div>
    <v-app>
      <!-- Top Melacast logo -->
      <v-toolbar flat elevation="0">
        <div>
          <img class="mx-auto" height="200px" width="200px" src="../assets/images/horizontal.png" />
        </div>
        <v-spacer></v-spacer>
      </v-toolbar>
      <!-- Test section -->
      <v-card>
        <v-card-title v-if="showCard" id="testCard" ref="testCard">Test text here</v-card-title>
        <v-card-title v-if="!showCard" id="testCard2" ref="testCard2">The opposite</v-card-title>
      </v-card>
      <!-- Form start -->
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
              <v-text-field
                outlined
                :rules="nameRules"
                justify="center"
                v-model="form.lastname"
                label="Last Name"
              ></v-text-field>
              <v-text-field
                outlined
                justify="center"
                :rules="ageRules"
                v-model="form.age"
                label="Age"
              ></v-text-field>
              <v-select
                outlined
                v-model="form.gender"
                :rules="genderRules"
                :items="genders"
                label="Gender Identity"
              ></v-select>

              <v-text-field
                outlined
                v-model="form.languages_spoken"
                justify="center"
                label="Spoken Languages"
              ></v-text-field>
            </v-card>
            <v-card flat>
              <v-card-title :rules="raceRules" class="ml-sm-n4">What is Your Race Identity?</v-card-title>
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
              @click.prevent="submitProfile"
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
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";

export default {
  name: "Create Profile",
  components: { FooterComponent, TopNavbar },
  methods: {
    async submitProfile() {
      try {
        // wait for validation to pass before POSTing
        let response = await this.$refs.form.validate();
        if (!response) {
          console.log(response);
          console.log("Failed Validation");
        } else {
          this.$axios
            .post(`/api/v1/actors`, this.form)
            .then(response => {
              this.$router.push("/");
            })
            .catch(error => {
              if (error) {
                console.log(error, "ERROR WITH POST");
              }
            });
        }
      } catch (err) {
        console.log(err);
      }
    }
  },
  data() {
    return {
      showCard: false,
      genders: ["Female", "Male", "Non-Binary", "Prefer Not to Say"],
      unions: ["Non Union", "Union", "SAG", "Equity"],
      nameRules: [v => !!v || "Name is required"],
      email: "",
      emailRules: [v => !!v || "E-mail is required"],
      ageRules: [v => !!v || "Age is required"],
      genderRules: [v => !!v || "Gender Identity is required"],
      raceRules: [v => !!v || "Race Identity is required"],
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
