<template>
  <v-app>
    hello
    <v-row>
      <v-col>
        <v-img height="50vh" width="100vw" :src="listings.poster"></v-img>
      </v-col>
    </v-row>
  </v-app>
</template>
<script>
// import Navigation from "~/components/Navigation.vue";
// import SubscribeComponent from "~/components/SubscribeComponent.vue";
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
    // Navigation,
    // SubscribeComponent
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
    }
  },
  methods: {
    submitApplication() {
      // for resume
      this.form.date_submitted = this.currentDateTime;
      this.form.listing_url = `/listings/${this.listings.id}`; //for linking back to the listing when viewing all listings in a grid
      this.form.listing_thumbnail = this.listings.poster;
      this.form.profile_picture = this.userInfo[0].headshot;
      this.$axios
        .post(`/api/v1/apps/`, this.form)
        .then(response => {
          console.log(response);
          this.$router.push("/submitted");
        })
        .catch(error => {
          console.log(error);
        });
    },
    populateApplicationTitleField() {
      console.log(this.listings.title, "title");
      this.form.title = this.listings.title;
    },
    grabRoleName() {
      const input = this.$refs.roleList;
      this.form.role = input;
      console.log(this.form.role, "form role");
    },
    generateApplicantID(length, chars) {
      var result = "";
      for (var i = length; i > 0; --i) {
        result += chars[Math.round(Math.random() * (chars.length - 1))];
      }
      // return result;
      this.form.random_public_id_of_applicant = result;
      this.form.random_public_id_of_listing = this.listings.random_public_id;
      console.log(this.form.random_public_id_of_applicant);
    }
  },
  data() {
    return {
      hasPermission: true,
      applicationIsHidden: false,
      listings: [],
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