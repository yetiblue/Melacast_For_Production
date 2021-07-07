<template>
  <div>
    <v-app
      ><v-row class="justify-center align-center">
        <v-spacer></v-spacer
        ><v-col cols="6" sm="4"
          ><v-card flat
            ><v-card-title>
              Tell Us About Yourself
            </v-card-title>
            <v-text-field
              outlined
              justify="center"
              v-model="form.firstname"
              label="First Name"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="form.lastname"
              label="Last Name"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="form.age"
              label="Age"
            ></v-text-field>
            <v-select
              outlined
              v-model="form.gender"
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
          <v-card flat
            ><v-card-title>What is Your Race Identity?</v-card-title>
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
            <v-checkbox
              v-model="form.ethnicity"
              label="Asian"
              color="brown"
              value="Asian"
            ></v-checkbox>
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
            ></v-checkbox
          ></v-card>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
      <v-row>
        <v-col cols="8"></v-col>
        <v-col>
          <v-btn class="justify-end"> Next </v-btn>
        </v-col>
      </v-row>

      <!-- second page -->
      <v-row class="justify-center align-center">
        <v-spacer></v-spacer
        ><v-col cols="6" sm="4"
          ><v-card flat
            ><v-card-title>
              Tell Us About Your Work
            </v-card-title>
            <v-text-field
              outlined
              justify="center"
              v-model="form.profession"
              label="Profession (i.e gaffer, photographer, key grip etc)"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="form.location"
              label="Location (state)"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="form.city_location"
              label="Location (city)"
            ></v-text-field>
            <v-select
              outlined
              v-model="form.union"
              :items="unions"
              label="Union Status"
            ></v-select>
          </v-card>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
      <v-row>
        <v-col cols="8"></v-col>
        <v-col>
          <v-btn class="justify-end"> Next </v-btn>
        </v-col>
      </v-row>
      <v-row
        ><v-col sm="8"
          ><v-card
            ><v-card-title>Build your profile</v-card-title></v-card
          ></v-col
        ></v-row
      >
      <v-row>
        <v-col sm="2"
          ><v-btn fab><v-icon>mdi-camera</v-icon></v-btn></v-col
        ><v-col sm="6"
          ><v-card
            ><v-card-title>{{ form.profession }}</v-card-title
            ><v-card-subtitle
              >{{ form.firstname }}{{ form.lastname }}</v-card-subtitle
            ></v-card
          ></v-col
        ></v-row
      >
    </v-app>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";

export default {
  name: "Create Profile",
  data() {
    return {
      genders: ["Female", "Male", "Non-Binary", "Prefer Not to Say"],
      unions: ["Non Union", "Union", "SAG", "Equity"],
      form: {
        gender: null,
        firstname: null,
        lastname: null,
        languages_spoken: null,
        age: null,
        ethnicity: null,
        profession: null,
        location: null,
        city_location: null,
        union: null
      }
    };
  }
};
</script>
