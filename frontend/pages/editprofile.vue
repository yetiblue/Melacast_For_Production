<template>
  <div>
    <v-app>
      <TopNavbar />
      <v-row class="justify-center align-center">
        <v-spacer></v-spacer>
        <v-col cols="6" sm="4">
          <v-card flat>
            <v-card-title>Tell Us About Yourself</v-card-title>
            <v-text-field outlined justify="center" v-model="actor[0].firstname" label="First Name"></v-text-field>
            <v-text-field outlined justify="center" v-model="actor[0].lastname" label="Last Name"></v-text-field>
            <v-text-field outlined justify="center" v-model="actor[0].age" label="Age"></v-text-field>
            <v-select outlined v-model="actor[0].gender" :items="genders" label="Gender Identity"></v-select>

            <v-text-field
              outlined
              v-model="actor[0].languages_spoken"
              justify="center"
              label="Spoken Languages"
            ></v-text-field>
          </v-card>
          <v-card flat>
            <v-card-title>What is Your Race Identity?</v-card-title>
            <v-checkbox
              v-model="actor[0].ethnicity"
              label="Native Hawaiian/Pacific Islander"
              color="brown"
              value="Native Hawaiian/Pacific Islander"
            ></v-checkbox>
            <v-checkbox
              v-model="actor[0].ethnicity"
              label="Hispanic/Latino"
              color="brown"
              value="Hispanic/Latino"
            ></v-checkbox>
            <v-checkbox v-model="actor[0].ethnicity" label="Asian" color="brown" value="Asian"></v-checkbox>
            <v-checkbox
              v-model="actor[0].ethnicity"
              label="Middle Eastern"
              color="brown"
              value="Middle Eastern"
            ></v-checkbox>
            <v-checkbox
              v-model="actor[0].ethnicity"
              label="Black/African American"
              color="brown"
              value="Black/African American"
            ></v-checkbox>
            <v-checkbox
              v-model="actor[0].ethnicity"
              label="Native American/Alaskan Native"
              color="brown"
              value="Native American/Alaskan Native"
            ></v-checkbox>
          </v-card>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
      <v-row>
        <v-col cols="8"></v-col>
        <v-col>
          <v-btn class="justify-end">Next</v-btn>
        </v-col>
      </v-row>

      <!-- second page -->
      <v-row class="justify-center align-center">
        <v-spacer></v-spacer>
        <v-col cols="6" sm="4">
          <v-card flat>
            <v-card-title>Tell Us About Your Work</v-card-title>
            <v-text-field
              outlined
              justify="center"
              v-model="actor[0].profession"
              label="Profession (i.e gaffer, photographer, key grip etc)"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="actor[0].location"
              label="Location (state)"
            ></v-text-field>
            <v-text-field
              outlined
              justify="center"
              v-model="actor[0].city_location"
              label="Location (city)"
            ></v-text-field>
            <v-select outlined v-model="actor[0].union" :items="unions" label="Union Status"></v-select>
          </v-card>
        </v-col>

        <v-spacer></v-spacer>
      </v-row>
      <v-row>
        <v-col cols="8"></v-col>
        <v-col>
          <v-btn class="justify-end">Next</v-btn>
        </v-col>
      </v-row>
      <!-- Third Page -->
      <v-row>
        <v-col sm="8">
          <v-card flat>
            <v-card-title class="ml-sm-16">Build your profile</v-card-title>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col sm="2">
          <v-btn
            class="ml-sm-16"
            elevation="0"
            x-large
            :height="uploadButtonSize"
            :width="uploadButtonSize"
            fab
            @click="triggerFileInput"
          >
            <input type="file" style="display: none" ref="headshot" @change="onHeadshotChange" />

            <v-avatar v-if="headshotExists" size="150" class="ml-2">
              <!-- for if headshot exists in database -->
              <img :src="actor[0].headshot" />
            </v-avatar>
            <v-avatar v-if="headshotUploaded" size="150" class="ml-2">
              <!-- populate this with the previewURL -->
              <img id="previewHeadshot" ref="previewHeadshot" />
            </v-avatar>
            <v-icon v-if="!headshotExists">mdi-camera</v-icon>
          </v-btn>
        </v-col>
        <v-col sm="6">
          <v-card class="ml-sm-n4" flat>
            <v-card-title>{{ actor[0].profession }}</v-card-title>
            <v-card-subtitle>{{ actor[0].firstname }}{{ actor[0].lastname }}</v-card-subtitle>
            <v-text-field
              outlined
              justify="center"
              v-model="actor[0].pronouns"
              label="Pronouns (ex. They/Them)"
            ></v-text-field>
          </v-card>
        </v-col>
        <v-col sm="10">
          <v-textarea class="ml-sm-16" label="bio" outlined v-model="actor[0].bio" color="teal">
            <template v-slot:label>
              <div>Bio</div>
            </template>
          </v-textarea>
        </v-col>
        <v-col sm="8">
          <v-card flat>
            <v-card-title>What type of projects do you want to be a part of?</v-card-title>
            <v-card-subtitle>
              This will help other members of the community find you for work
              and collaboration.
            </v-card-subtitle>
          </v-card>
        </v-col>
        <v-col sm="6">
          <!-- {{ arrayStoringProjectTypes[0].project_types}} -->
          <MakeCheckboxesCheckedComponent
            v-for="projectType in projectTypes"
            :key="projectType + id"
            :propsProjectTypes="projectType"
            :allProjectTypes="projectTypes"
            :arrayOfProjectTypes.sync="arrayStoringProjectTypes[0].project_types"
            :checked="actor[0].project_types.includes(projectType)"
          ></MakeCheckboxesCheckedComponent>
        </v-col>
        <v-col sm="10">
          <v-card flat>
            <v-card-title>Connect Social Media</v-card-title>
            <v-card-subtitle>Paste URL</v-card-subtitle>
          </v-card>
        </v-col>
        <v-col sm="4">
          <v-text-field
            outlined
            justify="center"
            prepend-inner-icon="mdi-earth"
            v-model="actor[0].website"
            label="Website"
          ></v-text-field>
          <v-text-field
            outlined
            justify="center"
            prepend-inner-icon="mdi-instagram"
            v-model="actor[0].Instagram_Handle_if_applicable"
            label="Instagram"
          ></v-text-field>
        </v-col>
        <v-col sm="4">
          <v-text-field
            outlined
            justify="center"
            prepend-inner-icon="mdi-linkedin"
            v-model="actor[0].linkedIn"
            label="linkedIn"
          ></v-text-field>
          <v-text-field
            outlined
            justify="center"
            prepend-inner-icon="mdi-youtube"
            v-model="actor[0].youtube_or_vimeo"
            label="Youtube or Vimeo"
          ></v-text-field>
        </v-col>
      </v-row>
      <FooterComponent />
    </v-app>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";
import MakeCheckboxesCheckedComponent from "~/components/MakeCheckboxesCheckedComponent";

export default {
  //created() is necessary since arrayStoringProjectTypes[0].property
  //won't be available upon the DOM render otherwise.
  //loading the array before, allows for id or project_types to be called without an error
  created() {
    this.arrayStoringProjectTypes = this.actor.map(({ project_types, id }) => ({
      id,
      project_types: project_types.split(",")
    }));
  },
  components: { MakeCheckboxesCheckedComponent, TopNavbar },
  name: "Create Profile",
  computed: {
    uploadButtonSize() {
      //the headshot upload button
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
    },
    headshotExists() {
      //display camera icon or the user's headshot if it exists
      if (this.actor[0].headshot !== null) {
        return true;
      }
    },
    headshotUploaded() {
      if (this.hasHeadshot == true) {
        return true;
      }
    },
    isDirector() {
      if (this.actor[0].group == "Director") {
        return true;
      }
    },
    isPhotographer() {
      if (
        this.actor[0].group == "Photographers" ||
        this.actor[0].group == "Makeup"
      ) {
        return true;
      }
    },
    isCrew() {
      if (
        this.actor[0].group == "Production" ||
        this.actor[0].group == "Post Production"
      ) {
        return true;
      }
    },
    isActorMakeupDancer() {
      if (
        this.actor[0].group == "Actors" ||
        this.actor[0].group == "Directors" ||
        this.actor[0].group == "Dancer"
      ) {
        return true;
      }
    },
    isWriter() {
      if (this.actor[0].group == "Writers") {
        return true;
      }
    }
  },
  async asyncData({ $axios, params, store }) {
    const body = store.getters.loggedInUser.id;
    try {
      const [actor, photoList, writingSampleList, reelList] = await Promise.all(
        [
          $axios.$get(`/api/v1/actors/`, {
            //user data
            params: {
              user: body
            }
          }),
          $axios.$get(`/api/v1/photos/`, {
            //pictures used for gallery or project thumbnail
            params: {
              user: body
            }
          }),
          $axios.$get(`/api/v1/writingsamples/`, {
            params: {
              user: body
            }
          }),
          $axios.$get(`/api/v1/reels/`, {
            params: {
              user: body
            }
          })
        ]
      );
      return { actor, photoList, writingSampleList, reelList };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
    }
  },
  methods: {
    onPhotoChange() {
      this.photos = this.$refs.photos.files;
      console.log(this.photos);
      this.hasPhotos = true;
    },
    onReelChange() {
      this.reel = this.$refs.reel.files;
      console.log(this.reel);
      this.hasReel = true;
      console.log(this.hasReel, "has reel");
    },
    onThumbnailChange() {
      this.thumbnail = this.$refs.thumbnail.files;
      console.log(this.thumbnail);
      this.hasReelThumbnail = true;
      console.log(this.hasReelThumbnail, "reel thumbn");
    },
    onSampleChange() {
      this.samples = this.$refs.sample.files;
      console.log(this.samples);
      this.hasSample = true;
      console.log(this.hasSample, "has reel");
    },
    onSampleThumbnailChange() {
      this.thumbnail = this.$refs.sampleThumbnail.files;
      console.log(this.thumbnail);
      this.hasSampleThumbnail = true;
      console.log(this.hasSampleThumbnail, "reel thumbn");
    },
    onResumeChange(e) {
      this.newResume = this.$refs.resume.files;
      console.log(this.newResume);
      this.hasResume = true;
    },
    onHeadshotChange() {
      this.headshot = this.$refs.headshot.files;
      console.log(this.headshot);
      this.hasHeadshot = true;
      const [file] = this.$refs.headshot.files;
      if (file) {
        this.$refs.previewHeadshot.src = URL.createObjectURL(file);
      }
    },
    triggerFileInput() {
      this.$refs.headshot.click();
    },

    async updateProfile($axios) {
      //don't need async here
      // let editedForm = this.updatedActor;
      let editedForm = this.actor[0];
      const config = {
        headers: {
          "content-type": "multipart/form-data; "
        }
      };
      let formData = new FormData();
      for (let data in editedForm) {
        formData.append(data, editedForm[data]);
      }
      //Bc headshots and resumes are files, they have to be added seperately from the main form
      //If either is selected, the existing empty or non empty field is deleted from 'Actor'
      //The first time over, both fields will be empty and will throw an error if included in this.actor
      if (this.hasHeadshot == true) {
        formData.delete("headshot");
      }
      if (this.hasResume == true) {
        formData.delete("resume");
      }
      try {
        let response = await this.$axios.$patch(
          `/api/v1/actors/${this.actor[0].id}/`,
          formData,
          config
        );
        this.submitNewHeadshot();
        this.submitNewResume();

        // this.$router.push("/profile/");
      } catch (error) {
        console.log(error);
      }
    },
    submitNewHeadshot($axios) {
      if (this.hasHeadshot == true) {
        for (var i = 0; i < this.headshot.length; i++) {
          console.log("first checkpoint");
          let headshotData = new FormData();
          let headshot = this.headshot[i];
          headshotData.append("headshot", headshot);
          console.log(headshotData, "headshotData");
          const config = {
            headers: {
              "content-type": "multipart/form-data; "
            }
          };
          this.$axios
            .patch(`/api/v1/actors/${this.actor[0].id}/`, headshotData, config)
            .then(response => {
              console.log("Successfully Submitted headshot");
            })
            .catch(error => {
              console.log(error);
            });
        }
      } else {
      }
    },

    submitNewResume(axios) {
      if (this.hasResume == true) {
        //set to true if a resume is selected in the file uploader
        for (var i = 0; i < this.newResume.length; i++) {
          let resumeData = new FormData();
          let newResume = this.newResume[i];
          resumeData.append("resume", newResume);
          const config = {
            headers: {
              "content-type": "multipart/form-data; "
            }
          };
          this.$axios
            .patch(`/api/v1/actors/${this.actor[0].id}/`, resumeData, config)
            .then(response => {
              console.log("Successfully Submitted New Resume");
            })
            .catch(error => {
              console.log(error);
            });
        }
      } else {
        //do nothing here if someone doesn't want to change resume
      }
    },
    deletePhoto(photoID, $axios) {
      let deletionID = photoID;
      this.$axios.delete(`/api/v1/photos/${deletionID}/`);
      this.$router.go();
    },
    deleteSample(sampleID, $axios) {
      let deletionID = sampleID;
      this.$axios.delete(`/api/v1/writingsamples/${deletionID}/`);
      this.$router.go();
    },
    deleteReel(reelID, $axios) {
      let deletionID = reelID;
      this.$axios.delete(`/api/v1/reels/${deletionID}/`);
      this.$router.go();
    },
    submitPhotos(axios) {
      //gathers submitted photos and posts them to the photos Endpoint
      //Allows for seperation of main form and side projects. Can submit and
      //return these photos without refreshing main page.
      console.log("submit photos");
      if (this.hasPhotos == true) {
        for (var i = 0; i < this.photos.length; i++) {
          let photoData = new FormData();
          let photo = this.photos[i];
          photoData.append("photos", photo);
          const config = {
            headers: {
              "content-type": "multipart/form-data; "
            }
          };
          this.$axios
            .post(`/api/v1/photos/`, photoData, config)
            .then(response => {
              console.log("Successfully Submitted Images");
              this.$router.go();
            })
            .catch(error => {
              console.log(error);
            });
        }
      } else {
      }
    },
    submitReel(axios) {
      //gathers submitted Reels and posts them to the photos Endpoint
      //Allows for seperation of main form and side projects. Can submit and
      //return these reels without refreshing main page.
      console.log("submit reels");
      if (this.hasReel == true && this.hasReelThumbnail == true) {
        for (var i = 0; i < this.reel.length; i++) {
          console.log("first checkpoint");
          let reelData = new FormData();
          let reel = this.reel[i];
          let thumbnail = this.thumbnail[i];
          reelData.append("reel", reel);
          reelData.append("thumbnail", thumbnail);
          console.log(reelData, "reelData");
          const config = {
            headers: {
              "content-type": "multipart/form-data; "
            }
          };
          this.$axios
            .post(`/api/v1/reels/`, reelData, config)
            .then(response => {
              console.log("Successfully Submitted reels");
              this.$router.go();
            })
            .catch(error => {
              console.log(error);
            });
        }
      } else {
      }
    },
    submitSample(axios) {
      //gathers submitted writing samples and posts them to the photos Endpoint
      //Allows for seperation of main form and side projects. Can submit and
      //return these samples without refreshing main page.
      console.log("submit reels");
      if (this.hasSample == true && this.hasSampleThumbnail == true) {
        for (var i = 0; i < this.samples.length; i++) {
          console.log("first checkpoint");
          let sampleData = new FormData();
          let sample = this.samples[i];
          let thumbnail = this.thumbnail[i];
          sampleData.append("samples", sample);
          sampleData.append("thumbnail", thumbnail);
          console.log(sampleData, "sampleData");
          const config = {
            headers: {
              "content-type": "multipart/form-data; "
            }
          };
          this.$axios
            .post(`/api/v1/writingsamples/`, sampleData, config)
            .then(response => {
              console.log("Successfully Submitted samples");
              this.$router.go();
            })
            .catch(error => {
              console.log(error);
            });
        }
      } else {
      }
    }
  },

  data() {
    return {
      genders: ["Female", "Male", "Non-Binary", "Prefer Not to Say"],
      unions: ["Non Union", "Union", "SAG", "Equity"],
      //SET FORM TO ACTOR AND CHANGE ABOVE TO ACTOR[0]
      actor: [],
      projectTypes: [
        "Animation",
        "Documentary",
        "Experimental",
        "Feature",
        "Music Video",
        "Short",
        "Student",
        "Television",
        "Virtual Reality",
        "Web / New Media",
        "Theater"
      ],
      arrayStoringProjectTypes: []
    };
  }
};
</script>
