
<template>
  <div>
    <TopNavbar />
    <div v-if="!hasPermission">
      <SubscribeComponent />
    </div>
    <v-app>
      <v-row flat justify="end">
        <SideBarComponent :actors="actor[0]" :sideHeight="sideHeight">
          <template #userDesktopProfile>
            <v-card-title>{{actor[0].firstname}} {{actor[0].lastname}}</v-card-title>
            <v-card-subtitle>{{actor[0].group}}</v-card-subtitle>
            <v-btn class="mb-2" elevation="0" block>Dashboard</v-btn>
            <v-btn class="mb-2" elevation="0" block>Applications</v-btn>
            <v-btn class="pr-2 mb-1" elevation="0" block>Edit Profile</v-btn>
          </template>

          <template #userMobileProfile>
            <v-card-title>{{actor[0].firstname}} {{actor[0].lastname}}</v-card-title>
            <v-card-subtitle>{{actor[0].group}}</v-card-subtitle>
            <v-row>
              <v-col cols="12" sm="4">
                <v-btn class="grey" elevation="0" block :to="'google.com'">Dashboard</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block :to="'google.com'">Applications</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block :to="'google.com'">Edit Profile</v-btn>
              </v-col>
            </v-row>
          </template>
        </SideBarComponent>

        <v-col class="grey mt-sm-n16 mt-lg-0" cols="12" sm="12" lg="10">
          <div v-if="isCrew">
            <GridComponent :gridWidth="gridWidth">
              <template #rowTitleOne>Recommended</template>
              <template #navButtonOne>
                <v-btn text :to="`/listings`">View All</v-btn>
              </template>

              <template #cardSlot>
                <template v-for="crewRole in randomCrewRoleOrder.slice(0,4)">
                  <v-col :key="crewRole.id" justify="end" cols="12" sm="3">
                    <v-card :height="gridHeight" outlined title>
                      <v-img
                        class="white--text align-end"
                        :height="gridHeight"
                        @click="goToListing(crewRole.listing_public_id)"
                        :src="crewRole.poster"
                      >
                        <v-card-title
                          class="mb-n4 text-lg-h5 text-subtitle-2"
                          align="end"
                        >{{filmRole.role_name}}</v-card-title>

                        <v-card-text
                          class="mb-lg-3 text-lg-h6 text-subtitle-1"
                        >{{crewRole.date_submitted}}</v-card-text>
                      </v-img>
                    </v-card>
                  </v-col>
                </template>
              </template>
            </GridComponent>
            <div v-if="appsExist">
              <GridComponent :gridWidth="gridWidth">
                <template #rowTitleOne>Sent Applications</template>
                <template #navButtonTwo>
                  <v-btn text :to="`/myapps`">View All</v-btn>
                </template>
                <template #cardSlot>
                  <template v-for="application in applications.slice(0, 8)">
                    <v-col :key="application.id" justify="end" cols="12" sm="3">
                      <v-card :height="gridHeight" outlined title>
                        <v-img
                          class="white--text align-end"
                          :height="gridHeight"
                          :src="application.listing_thumbnail"
                        >
                          <v-card-title
                            class="mb-n4 text-lg-h5 text-subtitle-2"
                            align="end"
                          >{{application.role}}</v-card-title>
                          <v-card-title
                            class="mb-n4 text-lg-h5 text-subtitle-2"
                            align="end"
                          >{{application.title}}</v-card-title>
                          <v-card-text
                            class="mb-lg-3 text-lg-h6 text-subtitle-1"
                          >{{application.date_submitted}}</v-card-text>
                        </v-img>
                      </v-card>
                    </v-col>
                  </template>
                </template>
              </GridComponent>
            </div>
            <div v-else></div>
          </div>
        </v-col>

        <!-- <v-row class="grey pb-lg-16 mb-lg-n16" justify="center" align="start"> -->

        <!-- </v-row> -->
      </v-row>
      <div v-if="!isCrew">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>Recommended</template>
          <template #navButtonOne>
            <v-btn text :to="`/listings`">View All</v-btn>
          </template>

          <template #cardSlot>
            <template v-for="filmRole in randomFilmRoleOrder.slice(0,4)">
              <v-col :key="filmRole.id" justify="end" cols="12" sm="3">
                <v-card :height="gridHeight" outlined title>
                  <v-img
                    class="white--text align-end"
                    :height="gridHeight"
                    @click="goToListing(filmRole.listing_public_id)"
                    :src="filmRole.role_thumbnail"
                  >
                    <v-card-title
                      class="mb-n4 text-lg-h5 text-subtitle-2"
                      align="end"
                    >{{filmRole.role_name}}</v-card-title>

                    <v-card-text
                      class="mb-lg-3 text-lg-h6 text-subtitle-1"
                    >{{filmRole.date_submitted}}</v-card-text>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
        <div v-if="appsExist">
          <GridComponent :gridWidth="gridWidth">
            <template #rowTitleOne>Sent Applications</template>
            <template #navButtonTwo>
              <v-btn text :to="`/myapps`">View All</v-btn>
            </template>
            <template #cardSlot>
              <template v-for="application in applications.slice(0, 8)">
                <v-col :key="application.id" justify="end" cols="12" sm="3">
                  <v-card :height="gridHeight" outlined title>
                    <v-img
                      class="white--text align-end"
                      :height="gridHeight"
                      :src="application.listing_thumbnail"
                    >
                      <v-card-title
                        class="mb-n4 text-lg-h5 text-subtitle-2"
                        align="end"
                      >{{application.role}}</v-card-title>
                      <v-card-title
                        class="mb-n4 text-lg-h5 text-subtitle-2"
                        align="end"
                      >{{application.title}}</v-card-title>
                      <v-card-text
                        class="mb-lg-3 text-lg-h6 text-subtitle-1"
                      >{{application.date_submitted}}</v-card-text>
                    </v-img>
                  </v-card>
                </v-col>
              </template>
            </template>
          </GridComponent>
        </div>
        <div v-else></div>
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
  head() {
    return {
      title: "My applications"
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
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      }
      if (this.actor[0].group == "Dancers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Dancers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      }
      if (this.actor[0].group == "Writers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Writers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      }
      if (this.actor[0].group == "Photographers") {
        this.$axios
          .get("/api/v1/filmroles/", {
            params: {
              role_type: "Photographers"
            }
          })
          .then(response => {
            this.filmRoles = response.data;
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      }
      if (this.actor[0].group == "Crew") {
        this.$axios
          .get("/api/v1/listings/")
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
      }
      if (this.actor[0].group == "Post Production") {
        this.$axios
          .get("/api/v1/listings/")
          .then(response => {
            this.crewRoles = response.data;
            this.isCrew = true;
            this.isPostProduction = true;
            // this.sortedArray(); //random array
          })
          .catch(error => {
            console.log("GET REQUEST WENT AWRY");
          });
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
    gridHeight() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "260px";
        case "sm":
          return "190px";
        case "xs":
          return "35vh";
        case "lg":
          return "270px";
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
  async asyncData({ params, $axios, store }) {
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
        console.error(error);
        return { hasPermission };
      }
    }
  },
  data() {
    return {
      gridWidth: "10",
      sideHeight: `20vh`,
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