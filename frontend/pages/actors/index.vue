<template>
  <div>
    <TopNavbar />
    <v-app>
      <v-row flat justify="end">
        <v-spacer></v-spacer>
      </v-row>
      <v-row class="mt-lg-n12 pb-lg-16 mb-lg-n16" justify="end" align="start">
        <v-col class="pt-11 pb-lg-n16 mt-sm-n16 mt-lg-0" cols="12" sm="12">
          <v-col class="mt-6">
            <v-card flat class="text-center text-lg-left ml-lg-n6">
              <v-card-title class="justify-center">
                <h1 class="mt-4 mb-2 pt-6 text-h4">Our Community</h1>
              </v-card-title>
              <v-card-subtitle
                class="text-center"
              >There’s beauty in diversity. We are proud of the creatives that have built our comminity and continue to tell their stories.</v-card-subtitle>
            </v-card>
          </v-col>
        </v-col>
      </v-row>
      <v-form v-if="filterClicked" @submit.prevent="searchListings">
        <v-row class="pl-lg-9 px-sm-10">
          <v-col>
            <v-select v-model="location" :items="states" label="Location (state)"></v-select>
          </v-col>
          <v-col>
            <v-select v-model="ethnicity" :items="ethnicities" label="Race Identity"></v-select>
          </v-col>
          <v-col>
            <v-select v-model="group" :items="professions" label="Profession"></v-select>
          </v-col>
          <v-col>
            <v-select v-model="age_range" :items="ageRanges" label="Age Range"></v-select>
          </v-col>
          <v-col cols="2">
            <v-btn type="submit" text class="brown mt-3">Search</v-btn>
          </v-col>
        </v-row>
      </v-form>

      <template>
        <GridComponent :displayGridCount="displayGridCount" :gridWidth="gridWidth">
          <template #navButtonOne>
            <v-btn v-if="!filterClicked" @click="showFilters('open')" text>Filters</v-btn>
            <v-btn v-else @click="showFilters('close')" text>Close</v-btn>
          </template>
          <template #cardSlot>
            <template v-for="individualActor in sortedOldest">
              <v-col :key="individualActor .id" justify="end" cols="6" sm="4">
                <v-card
                  :key="individualActor.id"
                  :to="`/actors/${individualActor.id}/`"
                  :height="gridHeight"
                  outlined
                  title
                >
                  <v-img
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="individualActor.headshot"
                  >
                    <v-card-title
                      class="mb-n5"
                      align="end"
                    >{{individualActor.firstname}} {{individualActor.middle}} {{individualActor.lastname}}</v-card-title>
                    <v-card-text class="mb-n5">{{individualActor.group}}</v-card-text>
                    <v-card-text class="mb-5">
                      Member Since
                      {{ individualActor.date_joined }}
                    </v-card-text>
                    <v-row align="center" justify="end"></v-row>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </template>
    </v-app>
    <FooterComponent />
  </div>
</template>
<script>
import SideBarComponent from "~/components/SideBarComponent";
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";
import GridComponent from "~/components/GridComponent";
import { mapGetters } from "vuex";

export default {
  head() {
    return {
      title: "Actors list"
    };
  },
  components: {
    GridComponent,
    FooterComponent
    // ProfileGrid,
    // Navigation,
    // SubscribeComponent,
    // Footer
  },
  computed: {
    ...mapGetters(["loggedInUser"]),
    sortedOldest() {
      if (this.filteredProfile == "Oldest to Newest") {
        return this.actors.sort((a, b) => a.id - b.id);
        console.log("resorted");
      } else if (this.filteredProfile == "Newest to Oldest") {
        return this.actors.sort((a, b) => b.id - a.id);
      } else {
        return this.actors.sort((a, b) => b.id - a.id);
      }
    },
    gridHeight() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "240px";
        case "sm":
          return "190px";
        case "xs":
          return "25vh";
        case "lg":
          return "480px";
      }
    }
  },
  mounted() {
    // this.sortedNewestProfiles();
    this.checkUserPermission();
  },
  async asyncData({ $axios, store, loggedInUser }) {
    try {
      const body = store.getters.loggedInUser.id;
      const [user, actors] = await Promise.all([
        $axios.$get(`/api/v1/users/${body}/`),
        $axios.$get(`/api/v1/actors/`)
      ]);
      return { user, actors };
    } catch (error) {
      //   if (error.response.status === 403) {
      //     const hasPermission = false;
      //     return { hasPermission };
      //   }
      console.log(error);
    }
  },
  data() {
    return {
      ethnicity: null,
      location: null,
      group: null,
      age_range: null,
      filterClicked: false,
      professions: [
        "",
        "Directors",
        "Actors",
        "Dancers",
        "Writers",
        "Photographer",
        "Post Production",
        "Makeup Artist",
        "Production"
      ],
      ethnicities: [
        "",
        "Hispanic/Latino",
        "Native Hawaiian/Pacific Islander",
        "Asian",
        "Black/African American",
        "Native American/Alaskan Native",
        "Middle Eastern"
      ],
      ageRanges: [
        "",
        "18-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-59",
        "60-64",
        "65-69",
        "70+"
      ],
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
      gridWidth: "12",
      actors: [],
      user: [],
      age_range: "",
      ethnicity: "",
      location: "",
      group: "",
      form: [],
      hasPermission: true,
      filteredProfile: null
    };
  },
  methods: {
    showFilters(openOrClose) {
      console.log(openOrClose);
      if (openOrClose == "open") {
        this.filterClicked = true;
      } else if (openOrClose == "close") {
        this.filterClicked = false;
      }
    },
    applyFilters() {
      this.queryWithFilters();
    },
    checkUserPermission() {
      if (this.hasPermission == false) {
        this.$router.push(`/memberprofiles`);
      }
    },
    queryWithFilters() {
      console.log(this.ethnicity);
      //////////////////////// 1 Option empty ////////////////////////////////////
      if (
        this.ethnicity === "" &&
        this.location !== "" &&
        this.age_range !== "" &&
        this.group !== ""
      ) {
        console.log("i am ethnicity");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range,
              // ethnicity: this.ethnicity,
              location: this.location,
              group: this.group
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range === "" &&
        this.location !== "" &&
        this.ethnicity !== "" &&
        this.group !== ""
      ) {
        console.log("i am age");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              // age_range: this.age_range,
              ethnicity: this.ethnicity,
              location: this.location,
              group: this.group
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.age_range !== "" &&
        this.ethnicity !== "" &&
        this.group !== ""
      ) {
        console.log("i am location");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range,
              ethnicity: this.ethnicity,
              group: this.group
              // location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.age_range !== "" &&
        this.ethnicity !== "" &&
        this.group === ""
      ) {
        console.log("i am group");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range,
              ethnicity: this.ethnicity,
              // group: this.group
              location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
        //////////////////////// 3 Options empty ////////////////////////////////////
      } else if (
        this.location === "" &&
        this.age_range === "" &&
        this.ethnicity !== "" &&
        this.group === ""
      ) {
        console.log("loc + agerange + group empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              // age_range: this.age_range,
              ethnicity: this.ethnicity
              // location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
      if (
        this.location === "" &&
        this.ethnicity === "" &&
        this.age_range !== "" &&
        this.group === ""
      ) {
        console.log("loc + ethnicity + group empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range
              // ethnicity: this.ethnicity
              // location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range === "" &&
        this.ethnicity === "" &&
        this.location !== "" &&
        this.group === ""
      ) {
        console.log("age + ethnicity + group empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              // age_range: this.age_range
              // ethnicity: this.ethnicity
              location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range === "" &&
        this.ethnicity === "" &&
        this.location === "" &&
        this.group !== ""
      ) {
        console.log("age + ethnicity + location empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              group: this.group
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
      ///////////////////////// 2 Options empty ////////////////////////////////////
      else if (
        this.age_range === "" &&
        this.ethnicity === "" &&
        this.location !== "" &&
        this.group !== ""
      ) {
        console.log("age + ethnicity empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              group: this.group,
              location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range === "" &&
        this.ethnicity !== "" &&
        this.location === "" &&
        this.group !== ""
      ) {
        console.log("age + location empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              group: this.group,
              ethnicity: this.ethnicity
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range === "" &&
        this.ethnicity !== "" &&
        this.location !== "" &&
        this.group === ""
      ) {
        console.log("age + group empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              location: this.location,
              ethnicity: this.ethnicity
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range !== "" &&
        this.ethnicity !== "" &&
        this.location == "" &&
        this.group === ""
      ) {
        console.log("group + location empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range,
              ethnicity: this.ethnicity
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range !== "" &&
        this.ethnicity === "" &&
        this.location === "" &&
        this.group !== ""
      ) {
        console.log("ethnicity + location empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              group: this.group,
              age_range: this.age_range
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.age_range !== "" &&
        this.ethnicity == "" &&
        this.location !== "" &&
        this.group == ""
      ) {
        console.log("age + location empty");
        this.$axios
          .get(`/api/v1/actors/`, {
            params: {
              age_range: this.age_range,
              location: this.location
            }
          })
          .then(response => {
            this.actors = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
      // else {
      //   this.$axios
      //     .get(`/api/v1/actors/`, {
      //       params: {
      //         // age_range: this.age_range
      //         // ethnicity: this.ethnicity
      //         // location: this.location
      //       }
      //     })
      //     .then(response => {
      //       this.actors = response.data;
      //     })
      //     .catch(error => {
      //       console.log(error);
      //     });
      // }
    }
  }
};
</script>
<style>
</style>
