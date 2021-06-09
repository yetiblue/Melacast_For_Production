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
        <v-col cols="10">
          <v-card flat class="text-center text-lg-left ml-lg-n6">
            <v-card-title class="justify-center justify-lg-start">
              <h1 class="mb-2 pt-3 pl-lg-10 text-h4 brown--text">Applications</h1>
            </v-card-title>
          </v-card>
          <v-row class="pr-16">
            <v-col cols="3">
              <v-btn @click="getAcceptedApplications" class="grey" elevation="0" block>Accepted</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn @click="getRejectedApplications" elevation="0" block :to="'google.com'">Pending</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn @click="getPendingApplications" elevation="0" block :to="'google.com'">Declined</v-btn>
            </v-col>
            <v-col cols="3">
              <v-btn
                @click="getArchivedApplications"
                elevation="0"
                block
                :to="'google.com'"
              >Archived</v-btn>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
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
            user: body,
            status: "Pending"
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
      sideHeight: `20vh`,

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