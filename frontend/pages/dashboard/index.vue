<template>
  <div id="dashboard">
    <TopNavbar />
    <div v-if="!hasPermission">
      <SubscribeComponent />
    </div>
    <v-app>
      <v-row flat justify="end">
        <SideBarComponent :actors="actor[0]" :sideHeight="sideHeight">
          <template #userDesktopProfile>
            <v-card-title
              >{{ actor[0].firstname }} {{ actor[0].lastname }}</v-card-title
            >
            <v-card-subtitle>{{ actor[0].group }}</v-card-subtitle>
            <v-btn class="mb-2" elevation="0" block>Dashboard</v-btn>
            <v-btn class="mb-2" elevation="0" :to="'/myapps'" block
              >Applications</v-btn
            >
            <v-btn class="pr-2 mb-1" elevation="0" :to="'/profile/edit'" block
              >Edit Profile</v-btn
            >
          </template>

          <template #userMobileProfile>
            <v-card-title
              >{{ actor[0].firstname }} {{ actor[0].lastname }}</v-card-title
            >
            <v-card-subtitle>{{ actor[0].group }}</v-card-subtitle>
            <v-row>
              <v-col cols="12" sm="4">
                <v-btn class="grey" elevation="0" block>Dashboard</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block :to="'/myapps'">Applications</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block :to="'/profile/edit'"
                  >Edit Profile</v-btn
                >
              </v-col>
            </v-row>
          </template>
        </SideBarComponent>
        <v-col>
          <v-card flat class="text-center text-lg-left ml-lg-n6">
            <v-card-title class="justify-center justify-lg-start">
              <h1 class="mb-2 pt-3 pl-lg-10 text-h4 brown--text">
                My Dashboard | {{ actor[0].group }}
              </h1>
            </v-card-title>
          </v-card>
        </v-col>
        <v-col class="mt-sm-n16 mt-lg-0" cols="12" sm="12" lg="12">
          <div v-if="isCrew">
            <GridComponent :gridWidth="gridWidth">
              <template #rowTitleOne>
                <h1 class="text-h6 ml-sm-n16 ml-md-0 pl-lg-6">
                  Recommended
                </h1>
              </template>
              <template #navButtonOne>
                <v-btn class="mt-sm-n16 mt-md-0" text :to="`/listings`"
                  >View All</v-btn
                >
              </template>
              <template #cardSlot>
                <template v-for="crewRole in randomCrewRoleOrder.slice(0, 4)">
                  <v-col :key="crewRole.id" justify="end" cols="12" sm="3">
                    <v-card :height="gridHeight" outlined title>
                      <v-img
                        class="white--text align-end"
                        :height="gridHeight"
                        @click="goToListing(crewRole.listing_public_id)"
                        :src="crewRole.poster"
                      >
                        <v-card-title
                          v-if="isPostProduction"
                          class="mb-n4 text-subtitle-2 text-sm-caption text-md-subtitle-2"
                          align="end"
                          >{{
                            crewRole.post_production_positions
                          }}</v-card-title
                        >
                        <v-card-title
                          v-else
                          class="mb-n4 text-subtitle-2 text-sm-caption text-md-subtitle-2"
                          align="end"
                          >{{ crewRole.crew_positions }}</v-card-title
                        >

                        <v-card-text
                          class="mb-lg-3 text-subtitle-2 text-sm-caption text-md-subtitle-2"
                          >{{ crewRole.date_submitted }}</v-card-text
                        >
                      </v-img>
                    </v-card>
                  </v-col>
                </template>
              </template>
            </GridComponent>
          </div>
        </v-col>

        <!-- <v-row class="grey pb-lg-16 mb-lg-n16" justify="center" align="start"> -->

        <!-- </v-row> -->
      </v-row>
      <div v-if="!isCrew">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>
            <h1 class="text-h6 ml-sm-n16 ml-md-0 pl-lg-6">Recommended</h1>
          </template>
          <template #navButtonOne>
            <v-btn class="mt-sm-n16 mt-md-0" text :to="`/listings`"
              >View All</v-btn
            >
          </template>

          <template #cardSlot>
            <template v-for="filmRole in randomFilmRoleOrder.slice(0, 4)">
              <v-col :key="filmRole.id" justify="end" cols="12" sm="3">
                <v-card :height="gridHeight" outlined title>
                  <v-img
                    class="white--text align-end"
                    :height="gridHeight"
                    @click="goToListing(filmRole.listing_public_id)"
                    :src="filmRole.role_thumbnail"
                  >
                    <v-card-title class="mb-n4 text-h6" align="end">{{
                      filmRole.role_name
                    }}</v-card-title>

                    <v-card-text
                      class="mb-lg-3 text-lg-subtitle-2 text-subtitle-2"
                      >{{ filmRole.date_submitted }}</v-card-text
                    >
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="appsExist">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>
            <h1 class="text-h6 pt-6 ml-sm-n16 ml-md-0 pl-lg-6">
              Sent Applications
            </h1>
          </template>
          <template #navButtonTwo>
            <v-btn class="mt-sm-n16 pt-md-12 mt-md-0" text :to="`/myapps`"
              >View All</v-btn
            >
          </template>
          <template #cardSlot>
            <template
              v-for="sortedApplication in sortedApplicationsOrder.slice(0, 8)"
            >
              <v-col :key="sortedApplication.id" justify="end" cols="12" sm="3">
                <v-card :height="gridHeight" outlined title>
                  <v-img
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="sortedApplication.listing_thumbnail"
                  >
                    <v-card-title
                      class="mb-n4 mt-2 text-lg-h6 text-sm-subtitle-2"
                      align="end"
                      >{{ sortedApplication.role }}</v-card-title
                    >
                    <v-card-title
                      class="mb-n4 mt-n8 text-lg-subtitle-1 text-sm-subtitle-2"
                      align="end"
                      >{{ sortedApplication.title }}</v-card-title
                    >
                    <v-card-text
                      class="mb-lg-3 mb-lg-n4 text-lg-subtitle-1 text-sm-subtitle-2"
                      >{{ sortedApplication.date_submitted }}</v-card-text
                    >
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-else>
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>
            <h1 class="text-h6 pt-6 ml-sm-n16 ml-md-0 pl-lg-6">
              Sent Applications
            </h1>
          </template>
          <template #navButtonTwo>
            <v-btn class="mt-sm-n16 pt-md-12 mt-md-0" text :to="`/myapps`"
              >View All</v-btn
            >
          </template>
          <template #cardSlot>
            <v-spacer></v-spacer>
            <v-card elevation="0" height="400px">
              <v-card-title class="pt-16"
                >No Submitted Applications Yet!</v-card-title
              >
              <v-btn class="brown white--text" block :to="'/listings'"
                >Visit Listings To Apply</v-btn
              >
            </v-card>
            <v-spacer></v-spacer>
          </template>
        </GridComponent>
      </div>
    </v-app>
    <FooterComponent />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import TopNavbar from "~/components/TopNavbar";
import SubscribeComponent from "~/components/SubscribeComponent";
import FooterComponent from "~/components/FooterComponent";
import GridComponent from "~/components/GridComponent";
import SideBarComponent from "~/components/SideBarComponent";
export default {
  name: "Dashboard",
  head() {
    return {
      title: "Dashboard"
    };
  },
  mounted() {
    // this.sortedArray();
    this.getRoles();
    this.redirectDirectors();
  },
  methods: {
    redirectDirectors(router) {
      if (this.actor[0].group == "Directors") {
        this.$router.push(`/applications`);
      }
    },
    goToListing(roleID) {
      this.$axios
        .get("/api/v1/listings/", {
          params: {
            random_public_id: roleID
          }
        })
        .then(response => {
          this.listing = response.data;
          console.log(this.listing[0].id);
          this.$router.push(`/listings/${this.listing[0].id}`);
        })
        .catch(error => {
          console.log("GET REQUEST WENT AWRY");
        });
    },
    sortedArray() {
      return this.applications.sort((a, b) => b.id - a.id);
    },
    getRoles($axios) {
      if (this.actor[0].group == "Actors") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Actors"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            console.log("Actors called");
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Dancers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Dancers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            console.log("called 2");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Writers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Writers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            console.log("called 3");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Photographers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Photographers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            console.log("called 4");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Art") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasArt: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            console.log("called 5");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Camera") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasCamera: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            console.log("called 6");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Lighting") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasLighting: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            console.log("called 7");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Sound") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasSound: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            console.log("called 8");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "HMU") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasHMU: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            console.log("called 9");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Editor") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasEditor: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            this.isPostProduction = true;
            console.log("called 10");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Color") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasEditor: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            this.isPostProduction = true;
            console.log("called 11");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "VFX") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasVFX: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            this.isPostProduction = true;
            console.log("called 12");

            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else if (this.actor[0].group == "Animator") {
        this.$axios
          .get("/api/v1/listings/", {
            params: {
              hasAnimator: "True"
            }
          })
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            this.isPostProduction = true;
            console.log("Animator called");
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      } else {
        this.isCrew = false;
        console.log("none of the above");
      }
    }
  },
  computed: {
    ...mapGetters(["loggedInUser"]),
    noProjectsYet() {
      if (
        this.sampleList == "" &&
        this.reelList == "" &&
        this.photoList == ""
      ) {
        return true;
      }
    },
    appsExist() {
      if (this.applications) {
        return true;
      }
    },
    randomFilmRoleOrder() {
      return this.filmRoles.sort(() => Math.random() - 0.5);
    },
    randomCrewRoleOrder() {
      return this.crewRoles.sort(() => Math.random() - 0.5);
    },
    sortedApplicationsOrder() {
      return this.applications
        .map(sortedApplication => sortedApplication)
        .sort((a, b) => b.id - a.id);
    },
    gridHeight() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "180px";
        case "sm":
          return "150px";
        case "xs":
          return "30vh";
        case "lg":
          return "210px";
      }
    }
  },
  components: {
    SubscribeComponent,
    TopNavbar,
    FooterComponent,
    GridComponent,
    SideBarComponent
  },
  async asyncData({ params, $axios, store, redirect }) {
    try {
      const body = store.getters.loggedInUser.id;
      const [actor, applications] = await Promise.all([
        $axios.$get(`/api/v1/actors/`, {
          params: {
            user: body
          }
        }),
        $axios.$get(`/api/v1/apps/`, {
          params: {
            user: body,
            archived: null
          }
        })
      ]);
      return { actor, applications };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        console.error("403 ERROR OOF");
        redirect("/createprofiles");

        return { hasPermission };
      } else {
      }
    }
  },
  data() {
    return {
      gridWidth: "10",
      sideHeight: `3vh`,
      hasPermission: true,
      applications: [],
      actor: [],
      filmRoles: [],
      crewRoles: [],
      isCrew: false,
      hasApps: true,
      listing: [],
      isPostProduction: false,
      archive: {
        status: "Archived"
      },
      // acceptedApplications: [],
      rejectedApplications: [],
      pendingApplications: []
    };
  }
};
</script>
