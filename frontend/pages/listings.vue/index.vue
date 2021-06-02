<template>
  <div>
    <TopNavbar />
    <v-app>
      <v-row flat justify="end">
        <v-spacer></v-spacer>
      </v-row>
      <v-row class="mt-lg-n16 pb-lg-16 mb-lg-n16" justify="end" align="start">
        <v-col class="pt-11 pb-lg-n16 mt-sm-n16 mt-lg-0" cols="12" sm="12">
          <v-col class="mt-6">
            <v-card flat class="text-center text-lg-left ml-lg-n6">
              <v-card-title :class="[forIpad ? 'justify-center' : 'none']">
                <h3 class="mb-2 pt-4">Projects</h3>
              </v-card-title>
              <v-card-subtitle>Brief Bio Boo sdflkdsflkls</v-card-subtitle>
            </v-card>
          </v-col>
        </v-col>
      </v-row>
      <template>
        <threeColGrid
          :displayGridCount="displayGridCount"
          :gridWidth="gridWidth"
          :sortedArrayOfListings="sortedArrayOfListings"
        >
          <template #cardSlot>
            <template v-for="sortedListing in sortedArrayOfListings">
              <v-col :key="sortedListing.id" justify="end" cols="6" sm="4">
                <v-card :key="sortedListing.id" :height="gridHeight" outlined title>
                  <v-img
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="sortedListing.poster"
                    @click="navigateToPage()"
                  >
                    <v-btn
                      text
                      :to="`/listings/${sortedListing.id}/`"
                      style="color:#efefef;"
                    >LEARN MORE</v-btn>
                    <v-card-title
                      class="mb-n5"
                      align="end"
                    >{{sortedListing.title}}{{sortedListing.id}}</v-card-title>
                    <v-card-text class="mb-n5">{{sortedListing.overview}}</v-card-text>
                    <v-card-text class="mb-5">
                      {{ sortedListing.start_date }}
                      {{ sortedListing.end_date }}
                    </v-card-text>
                    <v-row align="center" justify="end"></v-row>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </threeColGrid>
      </template>
    </v-app>
    <!-- <BottomFooterComponent /> -->
  </div>
</template>
<script>
import SideBarComponent from "~/components/SideBarComponent";
import TopNavbar from "~/components/TopNavbar";
// import BottomFooterComponent from "~/components/BottomFooterComponent";
import threeColGrid from "~/components/threeColGrid";
export default {
  head() {
    return {
      title: "Listings list"
    };
  },
  components: {
    SideBarComponent,
    TopNavbar,

    threeColGrid
  },
  data() {
    return {
      sideHeight: `10vh`,
      gridWidth: "12",
      location: "",
      job_type: "",
      status: "",
      genre: "",
      grabbedListings: [],
      hasPermission: true,
      filtersApplied: false,
      relevanceFilter: null
    };
  },
  methods: {
    navigateToPage() {
      console.log("click");
      this.$router.push(`/listings/${sortedListing.id}/`);
    }
  },
  computed: {
    forIpad() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return true;

        case "sm":
          return true;
        case "xs":
          return true;
      }
    },
    displayGridCount() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return 9;
        case "sm":
          return 6;
        case "xs":
          return 4;
        case "lg":
          return 9;
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
          return "280px";
      }
    },
    sortedArrayOfListings() {
      if (this.relevanceFilter == "Newest to Oldest") {
        return this.grabbedListings
          .map(sortedListing => sortedListing)
          .sort((a, b) => b.id - a.id);
      } else if (this.relevanceFilter == "Oldest to Newest") {
        return this.grabbedListings
          .map(sortedListing => sortedListing)
          .sort((a, b) => a.id - b.id);
      } else {
        return this.grabbedListings
          .map(sortedListing => sortedListing)
          .sort((a, b) => b.id - a.id);
      }
    }
  },
  mounted() {
    this.grabListings();
  },
  methods: {
    grabListings($axios) {
      this.$axios
        .get("/api/v1/listings/")
        .then(response => {
          this.grabbedListings = response.data;
        })
        .catch(error => {
          if (error.response.status === 403) {
            this.$router.push(`/memberlistings`);
          }
        });
    },

    searchListings() {
      this.applyFilters(); //all dropdown combinations below include a POST request
      this.filtersApplied = true;
    },
    applyFilters() {
      //////////////////////// 1 Option empty ////////////////////////////////////
      if (
        this.location === "" &&
        this.status !== "" &&
        this.genre !== "" &&
        this.job_type !== ""
      ) {
        console.log("location empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              // location: this.location,
              status: this.status,
              genre: this.genre,
              job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status !== "" &&
        this.genre === "" &&
        this.job_type !== ""
      ) {
        console.log("genre empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              location: this.location,
              status: this.status,
              // genre: this.genre,
              job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status === "" &&
        this.genre !== "" &&
        this.job_type !== ""
      ) {
        console.log("status empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              location: this.location,
              // status: this.status,
              genre: this.genre,
              job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status !== "" &&
        this.genre !== "" &&
        this.job_type === ""
      ) {
        console.log("job_type empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              location: this.location,
              status: this.status,
              genre: this.genre
              // job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
      ///////////////// 3 options empty ////////////////////
      else if (
        this.location === "" &&
        this.status === "" &&
        this.genre !== "" &&
        this.job_type === ""
      ) {
        console.log("loc + status + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              genre: this.genre
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.status !== "" &&
        this.genre === "" &&
        this.job_type === ""
      ) {
        console.log("loc + genre + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              status: this.status
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status === "" &&
        this.genre === "" &&
        this.job_type === ""
      ) {
        console.log("status + genre + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              location: this.location
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.status === "" &&
        this.genre === "" &&
        this.job_type !== ""
      ) {
        console.log("status + genre + loc empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
      ///////////////////// 2 Options Empty //////////////////////////
      else if (
        this.location !== "" &&
        this.status === "" &&
        this.genre === "" &&
        this.job_type !== ""
      ) {
        console.log("status + genre  empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              job_type: this.job_type,
              location: this.location
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.status === "" &&
        this.genre !== "" &&
        this.job_type !== ""
      ) {
        console.log("status  + loc empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              job_type: this.job_type,
              genre: this.genre
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status === "" &&
        this.genre !== "" &&
        this.job_type === ""
      ) {
        console.log("status  + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              location: this.location,
              genre: this.genre
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.status !== "" &&
        this.genre !== "" &&
        this.job_type === ""
      ) {
        console.log("loc  + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              status: this.status,
              genre: this.genre
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location === "" &&
        this.status !== "" &&
        this.genre === "" &&
        this.job_type !== ""
      ) {
        console.log("genre + loc empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              status: this.status,
              job_type: this.job_type
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (
        this.location !== "" &&
        this.status !== "" &&
        this.genre === "" &&
        this.job_type === ""
      ) {
        console.log("genre + job empty");
        this.$axios
          .get(`/api/v1/listings/`, {
            params: {
              status: this.status,
              location: this.location
            }
          })
          .then(response => {
            this.listings = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
};
</script>
<style>
</style>
