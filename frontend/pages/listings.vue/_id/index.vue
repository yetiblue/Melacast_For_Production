<template>
  <div>
    <TopNavbar />
    <v-app>
      <v-row flat justify="end">
        <v-spacer></v-spacer>
      </v-row>
      <v-row class="mt-lg-n16 pb-lg-16 mb-lg-n16" justify="end" align="start">
        <v-col class="pt-11 pb-lg-n16 mt-sm-n16 mt-lg-0" cols="12" sm="12" lg="12">
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
      <threeColGrid :displayGridCount="displayGridCount" :gridWidth="gridWidth">
        <template #cardSlot>
          <v-card :height="gridHeight" outlined title>
            <v-img
              class="white--text align-end"
              :height="gridHeight"
              @click="navigateToPage()"
              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            >
              <v-card-title class="mb-n5" align="end">Category Name</v-card-title>
              <v-card-text class="mb-n5">Timmy Zhou</v-card-text>
              <v-card-text class="mb-5">Date information</v-card-text>
              <v-row align="center" justify="end"></v-row>
            </v-img>
          </v-card>
        </template>
      </threeColGrid>
    </v-app>
    <BottomFooterComponent />
  </div>
</template>
<script>
import SideBarComponent from "~/components/SideBarComponent";
import TopNavbar from "~/components/TopNavbar";
// import BottomFooterComponent from "~/components/BottomFooterComponent";
import threeColGrid from "~/components/threeColGrid";
export default {
  components: {
    SideBarComponent,
    TopNavbar,
    BottomFooterComponent,
    threeColGrid
  },
  data() {
    return { sideHeight: `10vh`, gridWidth: "12" };
  },
  methods: {
    navigateToPage() {
      console.log("click");
      this.$router.push("/fourcols");
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
    }
  }
};
</script>
<style>
</style>
