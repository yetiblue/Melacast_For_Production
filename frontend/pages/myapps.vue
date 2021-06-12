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
            <v-btn class="mb-2" elevation="0" :to="'/dashboard'" block>Dashboard</v-btn>
            <v-btn class="mb-2" elevation="0" block>Applications</v-btn>
            <v-btn class="pr-2 mb-1" elevation="0" :to="'/profile/edit'" block>Edit Profile</v-btn>
          </template>

          <template #userMobileProfile>
            <v-card-title>{{actor[0].firstname}} {{actor[0].lastname}}</v-card-title>
            <v-card-subtitle>{{actor[0].group}}</v-card-subtitle>
            <v-row>
              <v-col cols="12" sm="4">
                <v-btn class="grey" elevation="0" block :to="'/dashboard'">Dashboard</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block>Applications</v-btn>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn elevation="0" block :to="'/profile/edit'">Edit Profile</v-btn>
              </v-col>
            </v-row>
          </template>
        </SideBarComponent>

        <v-col v-if="hasApps" cols="12" lg="10">
          <v-card flat class="text-center text-lg-left ml-lg-n6">
            <v-card-title class="justify-center justify-lg-start">
              <h1 class="mb-2 pt-3 pl-lg-10 text-h4 brown--text">Applications</h1>
            </v-card-title>
          </v-card>
          <v-row class="pr-lg-16 px-auto">
            <v-col cols="3">
              <v-btn text @click="getAcceptedApplications" elevation="0" block>Accepted</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn text @click="getRejectedApplications" elevation="0" block>Pending</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn text @click="getPendingApplications" elevation="0" block>Declined</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn text @click="getArchivedApplications" elevation="0" block>Archived</v-btn>
            </v-col>
          </v-row>
          <v-divider inset-right class="px-16"></v-divider>
          <v-row>
            <v-spacer></v-spacer>
            <v-col
              class="mr-lg-n4 mr-sm-16 ml-sm-n6 ml-lg-10 text-caption"
              cols="3"
              sm="2"
              md="4"
              lg="2"
            >
              <p>Role Name</p>
            </v-col>
            <v-spacer></v-spacer>
            <v-col class="ml-lg-16 mr-md-n16 ml-md-n16 text-caption" cols="3" sm="5" md="6" lg="6">
              <p>Date Submitted</p>
            </v-col>

            <v-spacer></v-spacer>
          </v-row>
          <v-list-item
            :to="applicant.listing_url"
            v-for="applicant in applications"
            :key="applicant.name"
          >
            <v-list-item-avatar>
              <v-img :src="applicant.listing_thumbnail"></v-img>
            </v-list-item-avatar>
            <!-- extra space for when there's 4 columns -->

            <v-list-item-content>
              <v-list-item-text class="pl-lg-16 pl-2">{{applicant.role}}</v-list-item-text>
            </v-list-item-content>

            <v-list-item-content>
              <v-list-item-text class="pl-lg-n4 pl-10" v-text="applicant.date_submitted"></v-list-item-text>
            </v-list-item-content>

            <v-list-item-action class="pr-lg-7 mr-lg-16 mr-0">
              <v-btn
                v-if="!isMobile"
                class="brown--text mb-5 mr-lg-10"
                text
                :x-small="$vuetify.breakpoint.xs"
                elevation="0"
                :to="applicant.listing_url"
              >View Project</v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-col>
        <v-col cols="12" lg="10" v-else>
          <v-card flat class="text-center text-lg-left ml-lg-n6">
            <v-card-title class="justify-center justify-lg-start">
              <h1 class="mb-2 pt-3 pl-lg-10 text-h4 brown--text">Applications</h1>
            </v-card-title>
          </v-card>
          <v-row>
            <v-col cols="2" sm="3"></v-col>
            <v-col class="justify-center" cols="8" sm="6">
              <v-card class="mt-lg-16" elevation="0" height="400px">
                <v-card-title
                  class="align-center text-caption text-sm-h5 justify-center pt-16"
                >No Submitted Applications Yet!</v-card-title>

                <v-btn
                  block
                  height="6vh"
                  class="brown justify-center white--text text-caption text-sm-h6"
                  :to="'/listings'"
                >Visit Listings To Apply</v-btn>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
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
    this.sortedArray();
  },
  methods: {
    checkIfAppsExist() {
      if (this.applications.length == 0) {
        return false;
        console.log("nonexistant");
      }
    },
    sortedArray() {
      return this.applications.sort((a, b) => b.id - a.id);
    },
    getAcceptedApplications($axios) {
      this.$axios
        .get("/api/v1/apps/", {
          params: {
            status: "Accepted"
          }
        })
        .then(response => {
          this.applications = response.data;
          this.sortedArray();
        })
        .catch(error => {
          console.log("GET REQUEST WENT AWRY");
        });
    },
    getRejectedApplications() {
      this.$axios
        .get("/api/v1/apps/", {
          params: {
            status: "Rejected"
          }
        })
        .then(response => {
          this.applications = response.data;
          this.sortedArray();
        })
        .catch(error => {
          console.log("GET REQUEST WENT AWRY");
        });
    },
    getPendingApplications() {
      this.$axios
        .get("/api/v1/apps/", {
          params: {
            status: "Pending"
          }
        })
        .then(response => {
          this.applications = response.data;
          this.sortedArray();
        })
        .catch(error => {
          console.log("GET REQUEST WENT AWRY");
        });
    },
    getArchivedApplications() {
      this.$axios
        .get("/api/v1/apps/", {
          params: {
            status: "Archived"
          }
        })
        .then(response => {
          this.applications = response.data;
          this.sortedArray();
        })
        .catch(error => {
          console.log("GET REQUEST WENT AWRY");
        });
    },
    archiveApplication(appID, status) {
      if (status == "Pending") {
        this.$axios
          .patch(`/api/v1/apps/${appID}/`, this.archive)
          .then(response => {
            this.getPendingApplications();
          });
      }
      if (status == "Accepted") {
        this.$axios
          .patch(`/api/v1/apps/${appID}/`, this.archive)
          .then(response => {
            this.getAcceptedApplications();
          });
      }
      if (status == "Rejected") {
        this.$axios
          .patch(`/api/v1/apps/${appID}/`, this.archive)
          .then(response => {
            this.getRejectedApplications();
          });
      }
    }
  },
  computed: {
    ...mapGetters(["loggedInUser"]),
    gridHeight() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "260px";
        case "sm":
          return "190px";
        case "xs":
          return "35vh";
        case "lg":
          return "350px";
      }
    },
    isMobile() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
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
      const [applications, actor] = await Promise.all([
        $axios.$get(`/api/v1/apps/`, {
          params: {
            user: body
          }
        }),
        $axios.$get(`/api/v1/actors/`, {
          params: {
            user: body
          }
        })
      ]);
      return { applications, actor };
      if (applications.length == 0) {
        const hasApps = false;
      }
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
      sideHeight: `0vh`,

      hasPermission: true,
      applications: [],
      hasApps: true,
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