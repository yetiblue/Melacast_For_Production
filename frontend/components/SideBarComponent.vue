<template>
  <v-col cols="12" sm="12" md="12" lg="2" xl="2">
    <div v-if="mobile">
      <v-container justify="center">
        <v-card class="pa-8" flat>
          <div v-if="extraSmallMobile">
            <lightBoxGallery
              v-show="modalVisible"
              :currentImage="currentImage"
              :profilePic="actors.headshot"
              :isProfilePic="isProfilePic"
              @close="closeModal"
            ></lightBoxGallery>
            <v-hover>
              <v-img
                class="mx-auto center center"
                v-if="!bg"
                height="200px"
                width="200px"
                @click=" lightboxEffect();
                      showModal()"
                :src="actors.headshot"
              ></v-img>
            </v-hover>
          </div>
          <div v-else>
            <lightBoxGallery
              v-show="modalVisible"
              :currentImage="currentImage"
              :profilePic="actors.headshot"
              :isProfilePic="isProfilePic"
              @close="closeModal"
            ></lightBoxGallery>
            <v-hover>
              <v-img
                v-if="!bg"
                class="mx-auto center center"
                height="200px"
                width="200px"
                @click=" lightboxEffect();
                      showModal()"
                :src="actors.headshot"
              ></v-img>
            </v-hover>
            <!-- <v-img
              class="mx-auto center center"
              justify="center"
              height="200px"
              width="200px"
              :src="actors.headshot"
            ></v-img>-->
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
          <lightBoxGallery
            v-show="modalVisible"
            :currentImage="currentImage"
            :profilePic="actors.headshot"
            :isProfilePic="isProfilePic"
            @close="closeModal"
          ></lightBoxGallery>
          <v-hover>
            <v-img
              v-if="!bg"
              height="200px"
              width="200px"
              @click=" lightboxEffect();
                      showModal()"
              :src="actors.headshot"
            ></v-img>
          </v-hover>
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
import lightBoxGallery from "~/components/lightBoxGallery";

export default {
  props: ["sideHeight", "actors", "userButtons"],
  data() {
    return {
      currentImage: 0,
      bg: false,
      modalVisible: false,
      isProfilePic: true
    };
  },
  components: { lightBoxGallery },
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
  },
  methods: {
    lightboxEffect() {
      this.currentImage = 0;
      this.bg = !this.bg;
      console.log("clicky");
    },
    showModal() {
      this.modalVisible = true;
      console.log(this.modalVisible, "modal vis");
    },
    closeModal() {
      this.modalVisible = false;
      this.bg = !this.bg;
    }
  }
};
</script>
