<template>
  <div>
    <TopNavbar />
    <v-app id="bigGrid">
      <div v-if="!mobile"></div>

      <v-row>
        <v-spacer></v-spacer>
        <v-col lg="6" sm="8">
          <v-card class="mb-lg-10 ml-lg-16 pl-lg-16" elevation="0">
            <v-card-title class="justify-start">Tell Us About Your Film</v-card-title>
            <v-card-subtitle>Add basic details to introduce this project.</v-card-subtitle>
          </v-card>
          <v-row justify="center">
            <v-col cols="12" sm="8">
              <v-text-field outlined justify="center" v-model="form.title" label="Project Title"></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                justify="center"
                v-model="form.director_email"
                label="Director's Email"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-textarea label="Bio" outlined v-model="form.overview" color="teal">
                <template v-slot:label>
                  <div>Project Logline</div>
                </template>
              </v-textarea>
            </v-col>
            <v-col outlined style="height=10vh" cols="6" sm="12">
              <v-card class="pl-lg-16 ml-lg-16" elevation="0">
                <v-card-title
                  v-if="!posterUploaded"
                  class="text-lg-subtitle-1"
                >Upload a project banner or choose one from our gallery</v-card-title>
                <v-card-title
                  v-if="!hideUploadName"
                  class="text-lg-subtitle-1"
                >{{displayPosterName}}</v-card-title>
                <v-img
                  class="mb-lg-6"
                  height="310px"
                  width="550px"
                  v-if="galleryPhotoSelected"
                  :src="selectedGalleryPhoto"
                ></v-img>
              </v-card>
            </v-col>
            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="!mobile" class="mb-6">
                <v-col class="pl-12" cols="12" sm="6">
                  <v-btn
                    class="white--text ml-16 ml-lg-n10"
                    width="15vw"
                    height="60px"
                    color="brown"
                    depressed
                    @click="inputFileClick"
                  >
                    <v-icon left>mdi-upload</v-icon>Thumbnail
                  </v-btn>
                  <input type="file" style="display: none" ref="poster" @change="createPoster" />
                </v-col>

                <v-col cols="12" class="pl-8" sm="1">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="white--text ml-sm-n4"
                        width="15vw"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="generatePosterFromComponent" />
                    </v-card>
                  </v-dialog>
                </v-col>
              </v-row>
              <v-spacer></v-spacer>
            </v-col>
            <!-- <div v-if="!galleryNotOpen">
              <GalleryThumbnailComponent @clicked="generatePosterFromComponent" />
              <button @click.prevent="closeGallery">Select</button>
              <button @click.prevent="closeGallery">Close</button>
            </div>-->
            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="mobile" class="mb-6">
                <v-col class="pl-12" cols="12" sm="6">
                  <v-btn
                    class="white--text ml-16 ml-lg-n10"
                    width="15vw"
                    height="60px"
                    color="brown"
                    depressed
                    @click="inputFileClick"
                  >
                    <v-icon left>mdi-upload</v-icon>Thumbnail
                  </v-btn>
                  <input type="file" style="display: none" ref="poster" @change="createPoster" />
                </v-col>

                <v-col cols="12" class="pl-8" sm="1">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="white--text ml-sm-n4"
                        width="15vw"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="generatePosterFromComponent" />
                    </v-card>
                  </v-dialog>
                </v-col>
              </v-row>
              <v-spacer></v-spacer>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select outlined v-model="location" :items="states" label="Location (state)"></v-select>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                v-model="city_location"
                justify="center"
                label="Location (City)"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="8">
              <v-menu
                v-model="startDateMenuOpen"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    outlined
                    label="Start Date"
                    readonly
                    :value="form.start_date"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="form.start_date"
                  no-title
                  @input="startDateMenuOpen = false"
                ></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12" sm="8">
              <v-menu
                v-model="endDateMenuOpen"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field outlined label="End Date" readonly :value="form.end_date" v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="form.end_date" no-title @input="endDateMenuOpen = false"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col outlined style="height=10vh" cols="6" sm="12">
              <v-card class="pl-lg-16 ml-lg-16" elevation="0">
                <v-card-title class="text-lg-subtitle-1 bold">
                  <b>What Best Describes Your Film?</b>
                </v-card-title>
                <v-card-subtitle>Check One</v-card-subtitle>
              </v-card>
            </v-col>
            <v-col outlined style="height=10vh" cols="6" sm="5">
              <v-checkbox v-model="form.genre" label="Animation" color="green" value="Animation"></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Documentary"
                color="green"
                value="Documentary"
              ></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Experimental"
                color="green"
                value="Experimental"
              ></v-checkbox>
              <v-checkbox v-model="form.genre" label="Feature" color="green" value="Feature"></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Music Video"
                color="green"
                value="Music Video"
              ></v-checkbox>
              <v-checkbox v-model="form.genre" label="Short" color="green" value="Short"></v-checkbox>
            </v-col>
            <v-col outlined style="height=10vh" cols="4" sm="3">
              <v-checkbox v-model="form.genre" label="Student" color="green" value="Student"></v-checkbox>
              <v-checkbox v-model="form.genre" label="Television" color="green" value="Television"></v-checkbox>
              <v-checkbox
                v-model="form.tags"
                label="Virtual Reality"
                color="green"
                value="Virtual Reality"
              ></v-checkbox>
              <v-checkbox
                v-model="form.tags"
                label="Web / New Media"
                color="green"
                value="Web/New Media"
              ></v-checkbox>
              <v-checkbox v-model="form.tags" label="Theater" color="green" value="Theater"></v-checkbox>
            </v-col>
          </v-row>

          <v-row justify="center">
            <!-- <v-col cols="6"></v-col> -->
            <v-spacer></v-spacer>
            <v-col cols="4" sm="3">
              <v-btn style="margin-top: 50px;">Next</v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>

      <!-- </v-container> -->

      <!-- </v-form> -->
    </v-app>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TopNavbar from "~/components/TopNavbar";
import SubscribeComponent from "~/components/SubscribeComponent";
import FooterComponent from "~/components/FooterComponent";
import GridComponent from "~/components/GridComponent";
import SideBarComponent from "~/components/SideBarComponent";
import GalleryThumbnailComponent from "~/components/GalleryThumbnailComponent";

export default {
  head() {
    return {
      //   title: "Create Your User Profile"
    };
  },
  mounted() {
    this.generatePublicID(32, "0123456789");
  },
  components: {
    SubscribeComponent,
    TopNavbar,
    FooterComponent,
    GridComponent,
    SideBarComponent,
    GalleryThumbnailComponent
  },
  computed: {
    ...mapGetters(["loggedInUser"]),
    memberListings() {
      return {
        title: this.form.title,
        start_date: this.form.start_date,
        genre: this.form.genre,
        poster: this.form.poster
      };
    },
    currentDateTime() {
      const current = new Date();
      const date =
        current.getMonth() +
        1 +
        "-" +
        current.getDate() +
        "-" +
        current.getFullYear();
      const dateTime = date;
      return dateTime;
    },
    mobile() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return true;
        case "sm":
          return true;
        case "xs":
          return true;
        case "lg":
          return false;
      }
    },
    buttonWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "20vw";
        case "sm":
          return "20vw";
        case "xs":
          return "90vw";
        case "lg":
          return false;
      }
    }
  },
  async asyncData({ $axios, store, params, loggedInUser }) {
    const body = store.getters.loggedInUser.id;
    try {
      let actors = await $axios.$get(`/api/v1/actors/`, {
        params: {
          user: body
        }
      });
      return { actors };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
      console.log(error);
    }
  },
  methods: {
    inputFileClick() {
      this.$refs.poster.click();
    },
    createPoster() {
      //Used if the poster is uploaded using Form File input
      this.poster = this.$refs.poster.files;
      console.log(this.poster[0]);
      this.hasPoster = true;
      this.posterUploaded = true;
      this.galleryPhotoSelected = false;
      this.displayPosterName = this.poster[0].name;
    },
    generatePosterFromComponent(thumbID) {
      //Used if the poster is chosen from the thumbnail galllery component

      //   this.$refs.testImage.src = thumbID;
      this.dialog = false;
      this.galleryPhotoSelected = true;
      this.hideUploadName = true;
      console.log(thumbID, "thumbID");
      this.selectedGalleryPhoto = thumbID;
      console.log(this.selectedGalleryPhoto, "selectedGallery");
      this.closeGallery();
    },
    onClickFromChild(thumbID) {
      //Used when selecting a thumbnail for a role
      console.log(thumbID, "thumbID");
      this.filmRoles.role_thumbnail = thumbID;
    },
    showGallery() {
      //Open thumbnail gallery
      this.galleryNotOpen = false;
    },
    closeGallery() {
      //Close Thumbnail gallery
      this.galleryNotOpen = true;
    },
    finishListing() {
      //After submitting basic information and the roles
      this.$router.push(`/applications`);
    },
    nextSection() {
      //Navigate to page 2 of 3 of the listing creation form
      this.basicInfoSectionComplete = true;
    },
    prevSection() {
      // Go back to page 1 of the listing creation form
      this.basicInfoSectionComplete = false;
    },
    getListingsAfterSubmitting(store) {
      // Retrieve all listings this user has submitted, sort for latest first, then select that one
      // The id of this listing is used for the Roles
      this.$axios
        .get(`/api/v1/listings/`, {
          params: {
            user: this.actors.id
          }
        })
        .then(response => {
          console.log("Getting the latest listing");
          this.listingThatWasJustAdded = response.data;
          this.listingThatWasJustAdded.sort((a, b) => b.id - a.id);
          console.log(this.listingThatWasJustAdded[0], "latest listing ID");
          this.addRoles();
        })
        .catch(error => {
          console.log(error);
        });
    },
    showPositions() {
      // Add Roles for the film page
      this.listingSubmitted = true;
    },
    submitForm() {
      // Submit the information on page 1 and 2 of the creation form
      this.form.date_submitted = this.currentDateTime; //currentDateTime is a computed Function
      let formAnswers = this.form;
      const config = {
        headers: {
          "content-type": "multipart/form-data; "
        }
      };
      let formData = new FormData();
      for (let data in formAnswers) {
        formData.append(data, formAnswers[data]);
      }
      if (this.hasPoster == true) {
        // if poster came from form upload input
        for (var i = 0; i < this.poster.length; i++) {
          console.log("first checkpoint");
          // let posterData = new FormData()
          let poster = this.poster[i];
          this.forMembers(poster);
          formData.append("poster", poster);
        }
        this.$axios
          .post(
            `/api/v1/listings/`,
            formData,
            config,
            this.positionsForm,
            this.form.random_public_id
          )
          .then(response => {
            console.log("Successfully Created New Listing");
            this.showPositions();
            //   this.$router.push(`/applications`);
          })
          .catch(error => {
            if (error) {
              this.showSubmitError = true;
            }
          });
      } else {
        // if poster came from the gallery component
        let img = this.selectedGalleryPhoto;
        console.log(img, "img");
        this.$axios
          .get(img, {
            responseType: "blob"
          })
          .then(response => {
            console.log(response.data);
            this.forMembers(response.data);
            formData.append("poster", response.data);
            this.$axios
              .post(
                `/api/v1/listings/`,
                formData,
                config,
                this.positionsForm,
                this.form.random_public_id
              )
              .then(response => {
                console.log("Successfully Created New Listing");
                this.showPositions();
              })
              .catch(error => {
                if (error) {
                  this.showSubmitError = true;
                }
              });
          });
      }
    },
    testSendImage(sentImage) {
      console.log(sentImage, "sentImage");
    },
    generatePublicID(length, chars) {
      // create the ID displayed in the URL for this listing
      var result = "";
      for (var i = length; i > 0; --i) {
        result += chars[Math.round(Math.random() * (chars.length - 1))];
      }
      // return result;
      this.form.random_public_id = result;
      this.filmRoles.listing_public_id = result;
      console.log(this.form.random_public_id);
      console.log(this.filmRoles.listing_public_id);
    },
    forMembers(sentImage) {
      //just grab all the fields from this.form, the extra data will just go into the void >:)
      let editedForm = this.form;
      const config = {
        headers: {
          "content-type": "multipart/form-data; "
        }
      };
      let formData = new FormData();
      for (let data in editedForm) {
        formData.append(data, editedForm[data]);
      }
      formData.append("random_public_id", this.form.random_public_id);
      formData.append("poster", sentImage);
      this.$axios
        .post(`/api/v1/memberlistings/`, formData)
        .then(response => {
          console.log("Successfully Created New Listing");
          //   this.$router.push(`/applications`);
        })
        .catch(error => {
          if (error) {
            this.showSubmitError = true;
          }
        });
    },
    displayReturnedRoles() {
      // Return all previous roles after each new role is submitted. Keeps a running list
      this.$axios
        .get(`/api/v1/filmroles/`, {
          params: {
            listing: this.listingThatWasJustAdded[0].id
          }
        })
        .then(response => {
          this.returnedFilmRoles = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteRole(roleID, $axios) {
      // Allows for deletion of a role from the returned list of all roles
      let deletionID = roleID;
      this.$axios.delete(`/api/v1/filmroles/${deletionID}/`);
      this.displayReturnedRoles();
      this.displayReturnedRoles();
    },
    addRoles($axios) {
      //  listingThatWasJustAdded array holds all listings objects. The one that was submitted before the roles
      this.filmRoles.listing = this.listingThatWasJustAdded[0].id;
      this.$axios
        .post(`/api/v1/filmroles/`, this.filmRoles)
        .then(response => {
          console.log("Successfully Submitted Role");
          this.displayReturnedRoles();
          this.filmRoles.role_name = null; // reset the fields for the role after each one is submitted
          this.filmRoles.ethnicity = null;
          this.filmRoles.role_description = null;
          this.filmRoles.role_thumbnail = null;
          this.filmRoles.listing_public_id = this.form.random_public_id;
          console.log(this.filmRoles.listing_public_id, "roles public id");
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  data() {
    return {
      hideUploadName: false,
      galleryPhotoSelected: false,
      dialog: false,
      states: [
        "",
        "Alabama",
        "Alaska",
        "American Samoa",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "District of Columbia",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Minor Outlying Islands",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Northern Mariana Islands",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "U.S. Virgin Islands",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming"
      ],
      hasPoster: false,
      selectedGalleryPhoto: null,
      hasPermission: true,
      galleryNotOpen: true,
      showSubmitError: false,
      actors: [],
      posterUploaded: false,
      displayPosterName: null,
      form: {
        title: null,
        start_date: null,
        end_date: null,
        location: null,
        overview: null,
        studio: null,
        // poster: null,
        genre: null,
        status: null,
        job_type: null,
        user: this.$store.getters.loggedInUser.id,
        post_production_positions: [],
        crew_positions: [],
        director_email: null,
        random_public_id: null,
        date_submitted: null
      },
      filmRoles: {
        role_name: null,
        ethnicity: null,
        listing: null,
        role_description: null,
        listing_public_id: null,
        role_thumbnail: null
      },
      positionsForm: {
        post_production_positions: [],
        crew_positions: []
      },
      returnedFilmRoles: [],
      listingSubmitted: false,
      listingThatWasJustAdded: [],
      basicInfoSectionComplete: false
    };
  }
};
</script>