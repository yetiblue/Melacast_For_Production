<template>
  <v-col cols="12" sm="12" md="12" lg="2" xl="2">
    <div v-if="mobile">
      <v-container justify="center">
        <v-card class="pa-8" flat>
          <div v-if="extraSmallMobile">
            <v-img
              class="mx-auto"
              height="200px"
              width="200px"
              src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
            ></v-img>
          </div>
          <div v-else>
            <v-img
              class="mx-auto"
              justify="center"
              height="200px"
              width="200px"
              src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
            ></v-img>
          </div>

          <!-- navigation buttons -->
          <slot name="directorMobileSlot"></slot>
          <slot name="userMobileSlot"></slot>
          <slot name="userMobileProfile"></slot>
        </v-card>
      </v-container>
    </div>

    <div v-else>
      <div :style="{ height: sideHeight }">
        <!-- <div v-if="!mobile" > -->
        <v-card elevation="0" class="pb-lg-n16 pa-8">
          <v-img src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"></v-img>

          <!-- navigation buttons -->
          <slot name="directorDesktopSlot"></slot>
          <slot name="userDesktopSlot"></slot>
          <slot name="userDesktopProfile"></slot>
        </v-card>
      </div>
    </div>
    <!-- </div> -->
  </v-col>
</template>
<script>
export default {
  props: ["sideHeight"],
  computed: {
    height() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return 500;
      }
    },
    mobile() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return true;

        case "sm":
          return true;
        case "xs":
          return true;
      }
    },
    extraSmallMobile() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return true;
          console.log("is small");
      }
    }
  }
};
</script>
