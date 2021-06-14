<template>
  <div id="app">
    <!-- {{ photolist }} -->
    <v-row class="pr-lg-16 pt-lg-8 px-auto">
      <v-col cols="3">
        <v-btn block text @click.prevent="chooseType(personals)">Personal Projects</v-btn>
      </v-col>
      <v-col cols="3">
        <v-btn block text @click.prevent="chooseType(listings)">Listings</v-btn>
      </v-col>
      <v-col cols="3">
        <v-btn block text @click.prevent="chooseType(roles)">Roles</v-btn>
      </v-col>
      <v-col cols="3">
        <v-btn block text @click="getThumbnails()" elevation="0">All</v-btn>
      </v-col>
    </v-row>
    <v-divider inset-right class="px-16"></v-divider>

    <img :src="form.selectedThumbnail" alt />
    <GridComponent>
      <template #cardSlot>
        <template v-for="thumbnail in thumbnails">
          <v-col :key="thumbnail.id" justify="end" cols="12" sm="3">
            <v-card :height="gridHeight" outlined title>
              <v-img
                class="white--text align-end"
                :height="gridHeight"
                :src="thumbnail.thumbnail"
                alt
                @click="selectThumbnail(thumbnail.thumbnail)"
              ></v-img>
            </v-card>
          </v-col>
        </template>
      </template>
    </GridComponent>

    <!-- <button @click="submitThumbnail">Submit Image</button> -->
  </div>
</template>

<script>
import Navigation from "~/components/Navigation.vue";
import GridComponent from "~/components/GridComponent";
export default {
  data: function() {
    return {
      form: {
        selectedThumbnail: null
      },
      personals: "Personals",
      listings: "Listings",
      roles: "Roles",
      thumbnails: null,
      selectedType: null
    };
  },
  components: {
    Navigation,
    GridComponent
  },
  computed: {
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
  },

  mounted() {
    this.getThumbnails();
  },
  methods: {
    getThumbnails() {
      this.$axios //for everything else
        .$get(`/api/v1/thumbnails/`)
        .then(response => {
          console.log(response);
          this.thumbnails = response;
          console.log(this.thumbnails);
        })
        .catch(error => {
          console.log(error);
        });
    },
    selectThumbnail(thumbID) {
      //   this.form.selectedThumbnail = thumbID;
      this.$emit("clicked", thumbID);
    },
    chooseType(type) {
      this.selectedType = type;
      if (this.selectedType == "Personals") {
        this.$axios
          .$get(`/api/v1/thumbnails/`, {
            params: {
              category_name: this.selectedType
            }
          })
          .then(response => {
            console.log(response);
            this.thumbnails = response;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (this.selectedType == "Listings") {
        this.$axios
          .$get(`/api/v1/thumbnails/`, {
            params: {
              category_name: this.selectedType
            }
          })
          .then(response => {
            console.log(response);
            this.thumbnails = response;
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        this.$axios
          .$get(`/api/v1/thumbnails/`, {
            params: {
              category_name: this.selectedType
            }
          })
          .then(response => {
            console.log(response);
            this.thumbnails = response;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
};
</script>