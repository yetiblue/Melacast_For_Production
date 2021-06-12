<template>
  <div>
    <TopNavbar />
    <div v-if="!hasPermission">
      <SubscribeComponent />
    </div>
    <v-app>
      <v-row>
        <v-col>
          <v-card>
            <v-img
              height="500px"
              width="100vw"
              gradient="to top right, rgba(191, 191, 191, .22), rgba(191, 191, 191, .1)"
              :src="listings.poster"
            >
              <v-card-title
                style="margin-top: 190px"
                class="justify-center my-center white--text text-h5 text-sm-h4 text-lg-h2"
              >{{listings.title}}</v-card-title>
              <v-card-text
                class="text-center my-center white--text mt-sm-4 text-subtitle-1 text-sm-h6 text-lg-h5"
              >Director: {{listings.director_name}} | {{listings.city_location}}, {{listings.location}} | {{listings.start_date}} - {{listings.end_date}}</v-card-text>
            </v-img>
          </v-card>
        </v-col>
        <v-col cols="12" sm="8">
          <v-card flat class="ml-12 ml-md-16 pl-md-16">
            <div :style="descriptionPaddingLeft">
              <v-card-title>Project Description {{rolesForForm}}</v-card-title>
              <v-card-text>{{listings.overview}}</v-card-text>
              <v-card-subtitle>Casting Info:</v-card-subtitle>
              <div v-for="role in roles" :key="role.id">
                <v-card-text class="brown--text">{{role.role_name}}</v-card-text>
                <v-card-text class="mt-n6">{{role.character_name}}</v-card-text>
                <v-card-text class="mt-n6">{{role.description}}</v-card-text>
              </div>
            </div>
          </v-card>
        </v-col>
        <lightBoxGallery
          :applicationForm="applicationForm"
          v-show="modalVisible"
          @close="closeModal"
        >
          <template #submitApplicationSlot>
            <v-card class="px-16 px-sm-0" v-if="!secondCard" dark>
              <v-card-title
                class="text-caption text-sm-h6"
              >The Directors Will Be Able to View Your Profile Also</v-card-title>
              <v-form @submit.prevent="submitApplication()">
                <v-row class="pl-lg-9 px-sm-10">
                  <v-col cols="12">
                    <v-select v-model="form.role" :items="role_names" label="Select a Role"></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field v-model="form.name" label="Enter Your Full Name"></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      v-model="form.company"
                      label="Your Representation (if applicable)"
                    ></v-text-field>
                  </v-col>

                  <v-col class="mb-lg-8" cols="12">
                    <v-btn type="submit" block text class="brown mt-3">Submit!</v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-card>
            <v-card class="px-16 px-sm-0" v-if="secondCard" dark>
              <v-card-title>
                Submitted Successfully! You Can View The Decision On Your
                <br />
                <a :href="'/myapps'">Applications Page</a>
              </v-card-title>
              <v-row>
                <v-spacer></v-spacer>
                <v-col cols="2">
                  <v-btn
                    block
                    class="text-center brown mt-3"
                    type="submit"
                    @click="closeModal"
                    text
                  >Close</v-btn>
                </v-col>
              </v-row>
            </v-card>
          </template>
        </lightBoxGallery>
        <v-col cols="12" sm="4">
          <v-card flat class="ml-12 ml-sm-16 mt-5">
            <v-btn :width="buttonWidth" @click="showModal" class="ml-3 brown white--text">Apply Now</v-btn>
            <v-card-title class="text-subtitle-1">Crew Needed:</v-card-title>
            <v-card-title class="text-sm-subtitle-2 text-md-subtitle-1">Production</v-card-title>
            <v-card-text
              v-for="splitCrew in splitCrewPositions"
              :key="splitCrew.id"
              class="mt-n2 mb-n8 text-subtitle-2"
            >-{{splitCrew}}</v-card-text>
            <v-card-title class="mt-4 text-sm-subtitle-2 text-md-subtitle-1">Post Production</v-card-title>
            <v-card-text
              v-for="splitPost in  splitPostProductionPositions"
              :key="splitPost.id"
              class="mt-n2 mb-n8 text-subtitle-2"
            >-{{splitPost}}</v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-app>
    <FooterComponent />
  </div>
</template>
<script>
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";
// import Navigation from "~/components/Navigation.vue";
import lightBoxGallery from "~/components/lightBoxGallery";

import SubscribeComponent from "~/components/SubscribeComponent.vue";
export default {
  head() {
    return {
      title: "Listing Information"
    };
  },
  mounted() {
    this.generateApplicantID(32, "0123456789");
  },
  components: {
    TopNavbar,
    FooterComponent,
    SubscribeComponent,
    lightBoxGallery
  },
  async asyncData({ $axios, params, loggedInUser, store }) {
    const body = store.getters.loggedInUser.id;
    try {
      const [listings, userInfo, roles] = await Promise.all([
        $axios.$get(`/api/v1/listings/${params.id}/`),
        $axios.$get(`/api/v1/actors/`, {
          params: {
            user: body
          }
        }),
        $axios.$get(`/api/v1/filmroles/`, {
          params: {
            listing: `${params.id}`,
            role_status: "Open"
          }
        })
      ]);
      return { listings, userInfo, roles };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
    }
  },
  computed: {
    rolesForForm() {
      for (let i = 0; i < this.roles.length; i++) {
        // return this.roles[i].role_name;
        this.role_names.push(this.roles[i].role_name);
        console.log(this.role_names, "role_names");
        // console.log(this.roles[i].role_name);
      }
    },
    splitCrewPositions() {
      return this.listings.crew_positions.split(","); //seperates each word into a string
    },
    splitPostProductionPositions() {
      return this.listings.post_production_positions.split(",");
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
    // posterHeight() {
    //   switch (this.$vuetify.breakpoint.name) {
    //     case "md":
    //       return "240px";
    //     case "sm":
    //       return "190px";
    //     case "xs":
    //       return "25vh";
    //     case "lg":
    //       return "280px";
    //   }
    // },
    descriptionPaddingLeft() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "100px";
        case "sm":
          return "190px";
        case "xs":
          return "25vh";
        case "lg":
          return "150px";
      }
    },
    buttonWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "15vw";
        case "sm":
          return "15vw";
        case "xs":
          return "30vw";
        case "lg":
          return "15vw";
      }
    }
  },
  methods: {
    showSecondCard() {
      this.secondCard = !this.secondCard;
    },
    submitApplication() {
      // for resume
      this.form.date_submitted = this.currentDateTime;
      this.form.listing_url = `/listings/${this.listings.id}`; //for linking back to the listing when viewing all listings in a grid
      this.form.listing_thumbnail = this.listings.poster;
      this.form.profile_picture = this.userInfo[0].headshot;
      this.form.title = this.listings.title;
      this.$axios
        .post(`/api/v1/apps/`, this.form)
        .then(response => {
          console.log(response);
          this.showSecondCard();
        })
        .catch(error => {
          console.log(error);
        });
    },
    // populateApplicationTitleField() {
    //   console.log(this.listings.title, "title");
    //   this.form.title = this.listings.title;
    // },
    // grabRoleName() {
    //   const input = this.$refs.roleList;
    //   this.form.role = input;
    //   console.log(this.form.role, "form role");
    // },
    generateApplicantID(length, chars) {
      var result = "";
      for (var i = length; i > 0; --i) {
        result += chars[Math.round(Math.random() * (chars.length - 1))];
      }
      // return result;
      this.form.random_public_id_of_applicant = result;
      this.form.random_public_id_of_listing = this.listings.random_public_id;
      console.log(this.form.random_public_id_of_applicant);
    },
    showModal() {
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;

      this.secondCard = false;
    }
  },
  data() {
    return {
      secondCard: false,
      role_names: [],
      applicationForm: true,
      hasPermission: true,
      applicationIsHidden: false,
      listings: [],
      roles: [],
      modalVisible: false,

      form: {
        name: null,
        role: null,
        company: null,
        status: "Pending",
        listing: this.$route.params.id,
        title: null,
        date_submitted: null,
        listing_url: null,
        listing_thumbnail: null,
        random_public_id_of_listing: null,
        random_public_id_of_applicant: null,
        profile_picture: null
      }
    };
  }
};
</script>