<template>
  <div>
    <div></div>
    <transition name="modal-fade">
      <div class="modal-backdrop">
        <div
          class="modal"
          role="dialog"
          aria-labelledby="modalTitle"
          aria-describedby="modalDescription"
        >
          <slot name="buttonControls"></slot>
          <slot name="footer">
            <v-img
              v-if="!isProfilePic && !isCardsList"
              contain
              class="justify-center align-center mt-16 imageLight"
              :src="sortedPhotoList[currentImage].photos"
              alt
            />

            <v-img
              v-if="isProfilePic"
              contain
              class="justify-center align-center mt-16 imageLight"
              :src="profilePic"
              alt
            />
            <v-card v-if="isCardsList">
              <v-img>
                <v-card-title class="imageLight">{{cardsList[0].card_description}}</v-card-title>
              </v-img>
            </v-card>
            <v-row class="mt-4">
              <v-col v-if="!isProfilePic" cols="6">
                <v-btn class="white--text" text block @click="next">Prev</v-btn>
              </v-col>
              <v-spacer></v-spacer>
              <v-col v-if="!isProfilePic" cols="6">
                <v-btn class="white--text" text block @click="prev">Next</v-btn>
              </v-col>
              <v-col cols="12">
                <v-btn
                  class="white--text mt-n6"
                  text
                  block
                  @click="close"
                  aria-label="Close modal"
                >Close me!</v-btn>
              </v-col>
            </v-row>
          </slot>
        </div>
      </div>
    </transition>
  </div>
</template>
<script>
export default {
  name: "modal",
  props: [
    "currentImage",
    "sortedPhotoList",
    "profilePic",
    "isProfilePic",
    "cardsList",
    "isCardsList"
  ],
  methods: {
    close() {
      this.$emit("close");
    },
    next() {
      if (this.currentImage < this.sortedPhotoList.length - 1) {
        this.currentImage++;
        console.log(this.currentImage);
      } else {
        this.currentImage = 0;
        console.log(this.currentImage);
      }
    },
    prev() {
      if (this.currentImage > 0) {
        this.currentImage--;
      } else {
        this.currentImage = this.sortedPhotoList.length - 1;
      }
    }
  }
};
</script>
<style>
.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100000;
}
.imageLight {
  max-height: 80%;
}
.modal {
  background: rgba(0, 0, 0, 0.75);
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}
.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}
.modal-header {
  border-bottom: 1px solid #eeeeee;
  color: #4aae9b;
  justify-content: space-between;
}
.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
  padding: 100px;
}
.modal-body {
  position: relative;
  padding: 20px 10px;
}
.btn-close {
  border: none;
  font-size: 20px;
  padding: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #4aae9b;
  background: transparent;
}
.btn-green {
  color: white;
  background: #4aae9b;
  border: 1px solid #4aae9b;
  border-radius: 2px;
}
</style>