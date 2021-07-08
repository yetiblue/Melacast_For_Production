<template>
  <div>
    <v-app>
      <!-- First page -->
      <v-row class="justify-center align-center">
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
      <!-- Third Page -->
      <v-row
        ><v-col sm="8"
          ><v-card flat
            ><v-card-title class="ml-sm-16"
              >Build your profile</v-card-title
            ></v-card
          ></v-col
        >
      </v-row>
      <v-row>
        <v-col sm="2"
          ><v-btn
            class="ml-sm-16"
            elevation="0"
            x-large
            :height="uploadButtonSize"
            :width="uploadButtonSize"
            fab
            ><v-icon>mdi-camera</v-icon></v-btn
          ></v-col
        ><v-col sm="6"
          ><v-card class="ml-sm-n4" flat
            ><v-card-title>{{ form.profession }}</v-card-title
            ><v-card-subtitle
              >{{ form.firstname }}{{ form.lastname }}</v-card-subtitle
            >
            <v-text-field
              outlined
              justify="center"
              v-model="form.pronouns"
              label="Pronouns (ex. They/Them)"
            ></v-text-field>
          </v-card>
        </v-col>
        <v-col sm="10">
          <v-textarea
            class="ml-sm-16"
            label="bio"
            outlined
            v-model="form.bio"
            color="teal"
          >
            <template v-slot:label>
              <div>Bio</div>
            </template>
          </v-textarea></v-col
        >
        <v-col sm="8"
          ><v-card flat
            ><v-card-title
              >What type of projects do you want to be a part of?</v-card-title
            ><v-card-subtitle
              >This will help other members of the community find you for work
              and collaboration.</v-card-subtitle
            >
          </v-card></v-col
        >
        <v-col sm="6">
          <v-checkbox
            v-model="form.project_types"
            label="Animation"
            color="brown"
            value="Animation"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Documentary"
            color="brown"
            value="Documentary"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Experimental"
            color="brown"
            value="Experimental"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Feature"
            color="brown"
            value="Feature"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Music Video"
            color="brown"
            value="Music Video"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Short"
            color="brown"
            value="Short"
          ></v-checkbox
        ></v-col>
        <v-col sm="6">
          <v-checkbox
            v-model="form.project_types"
            label="Animation"
            color="brown"
            value="Animation"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Documentary"
            color="brown"
            value="Documentary"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Experimental"
            color="brown"
            value="Experimental"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Feature"
            color="brown"
            value="Feature"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Music Video"
            color="brown"
            value="Music Video"
          ></v-checkbox>
          <v-checkbox
            v-model="form.project_types"
            label="Short"
            color="brown"
            value="Short"
          ></v-checkbox
        ></v-col>
        <v-col sm="10">
          <v-card flat
            ><v-card-title>Connect Social Media</v-card-title
            ><v-card-subtitle>Paste URL</v-card-subtitle>
          </v-card></v-col
        >
        <v-col sm="4">
          <v-text-field
            outlined
            justify="center"
            v-model="form.website"
            label="Website"
          ></v-text-field>
          <v-text-field
            outlined
            justify="center"
            v-model="form.Instagram_Handle_if_applicable"
            label="Instagram"
          ></v-text-field
        ></v-col>
        <v-col sm="4">
          <v-text-field
            outlined
            justify="center"
            v-model="form.linkedIn"
            label="linkedIn"
          ></v-text-field>
          <v-text-field
            outlined
            justify="center"
            v-model="form.youtube_or_vimeo"
            label="Youtube or Vimeo"
          ></v-text-field></v-col
      ></v-row>
    </v-app>
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
        union: null,
        pronouns: null,
        bio: null,
        project_types: [],
        website: null,
        twitter: null,
        linkedIn: null,
        Instagram_Handle_if_applicable: null,
        youtube_or_vimeo: null
      }
    };
  }
};
</script>
