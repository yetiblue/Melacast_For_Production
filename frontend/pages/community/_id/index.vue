<template>
  <div>
    <TopNavbar />
    <div v-if="!hasPermission">
      <SubscribeComponent />
    </div>
    <v-app>
      <v-row flat justify="end">
        <SideBarComponent :actors="actors" :sideHeight="sideHeight">
          <template #userDesktopProfile>
            <v-card-subtitle class="ml-1 text-lg-subtitle-1 text-center">
              <a target="_blank" :href="actors.website">Personal Site</a>
            </v-card-subtitle>
            <v-card-actions class="justify-center">
              <v-icon
                class="ml-2 ml-lg-n1"
                @click="socialLink(actors.Instagram_Handle_if_applicable)"
              >mdi-instagram</v-icon>

              <v-icon class="ml-4" @click="socialLink(actors.youtube_or_vimeo)">mdi-youtube</v-icon>

              <v-icon @click="socialLink(actors.twitter)" class="ml-4">mdi-twitter</v-icon>
              <v-icon @click="socialLink(actors.linkedIn)" class="ml-4">mdi-linkedin</v-icon>
            </v-card-actions>
            <v-divider class="mt-2 mx-4"></v-divider>
            <v-card-subtitle class="justify-center text-center">
              <h3>Project Interests:</h3>
              <v-card-text>{{actors.project_types}}</v-card-text>
            </v-card-subtitle>
            <!-- <template > -->
            <div v-for="tab in projectInterests" :key="tab">
              <v-card-text class="mt-n6 justify-center">{{tab}}</v-card-text>
            </div>
            <!-- </template> -->
            <v-btn
              class="mb-2 brown white--text"
              @click="copyText(actors.email)"
              elevation="0"
              block
            >Contact Me</v-btn>
            <a target="_blank" :href="actors.resume">
              <v-btn class="mb-2 brown white--text" elevation="0" block>Resume</v-btn>
            </a>
            <v-card-title class="text-center">Languages</v-card-title>

            <v-card-text>{{actors.languages_spoken}}</v-card-text>
          </template>

          <template #userMobileProfile>
            <v-card-subtitle class="text-center">
              <a target="_blank" :href="actors.website">Personal Site</a>
            </v-card-subtitle>
            <v-card-actions class="justify-center">
              <v-icon
                class="ml-2 ml-lg-0"
                @click="socialLink(actors.Instagram_Handle_if_applicable)"
              >mdi-instagram</v-icon>
              <v-icon class="ml-4" @click="socialLink(actors.youtube_or_vimeo)">mdi-youtube</v-icon>

              <v-icon @click="socialLink(actors.twitter)" class="ml-4">mdi-twitter</v-icon>
              <v-icon @click="socialLink(actors.linkedIn)" class="ml-4">mdi-linkedin</v-icon>
            </v-card-actions>
            <v-card-title class="justify-center">Project Interests</v-card-title>
            <v-card-text class="text-center">{{actors.project_types}}</v-card-text>
            <v-card-actions class="justify-center text-center">
              <v-btn
                @click="copyText(actors.email)"
                class="mb-2 brown mx-auto white--text"
                elevation="0"
              >Contact Me</v-btn>
            </v-card-actions>
            <v-card-actions class="justify-center">
              <a target="_blank" :href="actors.resume">
                <v-btn class="mb-2 brown white--text" elevation="0">Resume</v-btn>
              </a>
            </v-card-actions>

            <!-- MOVE LANGUAGES TO PROFILE CARD SECTION BELOW -->
            <!-- <v-card-title>Languages</v-card-title> -->
          </template>
        </SideBarComponent>

        <v-col class="pt-11 pb-lg-n16 mt-sm-n16 mt-lg-0" cols="12" sm="12" lg="10">
          <v-col>
            <v-card flat class="text-center text-lg-left ml-lg-n6">
              <v-card-title :class="[forIpad ? 'justify-center' : 'none']">
                <h3 class="mb-n8">{{actors.group}}</h3>
              </v-card-title>
              <v-card-title :class="[forIpad ? 'justify-center' : 'none']">
                <h1
                  class="mb-2 text-lg-h4"
                >{{actors.firstname}} {{actors.lastname}} ({{actors.pronouns}})</h1>
              </v-card-title>
              <v-card-subtitle>{{actors.ethnicity}} | {{actors.city_location}}, {{actors.location}} | Member Since {{actors.date_joined}}</v-card-subtitle>
              <v-card-text>{{actors.bio}}</v-card-text>
            </v-card>
          </v-col>

          <v-col class="mt-16" v-if="noProjectsYet" cols="10">
            <v-card-title class="justify-center">This User Hasn't Added Any Personal Projects Yet</v-card-title>
            <!-- <v-card-actions class="justify-center">
              <v-btn class="justify-center">Click Here</v-btn>
            </v-card-actions>-->
          </v-col>
        </v-col>

        <!-- <v-row class="grey pb-lg-16 mb-lg-n16" justify="center" align="start"> -->

        <!-- </v-row> -->
      </v-row>
      <GridComponent v-if="!isWriter || !isPhotographer" :gridWidth="gridWidth">
        <template v-if="isDirector || isActorMakeuporDancer || isCrewMember" #rowTitleOne>My Reel</template>

        <template v-if="!noReelYet" #cardSlot2>
          <v-col v-if="!bg" justify="end" cols="12">
            <v-card :height="gridHeight" title>
              <a :href="actors.reel" target="_blank">
                <v-img
                  class="mt-lg-n6 white--text align-end"
                  :height="gridHeight"
                  :src="actors.reel_thumbnail"
                ></v-img>
              </a>
            </v-card>
          </v-col>
        </template>
        <template v-if="noReelYet" #cardSlot2>
          <v-col v-if="!bg" justify="end" cols="12">
            <v-card :height="gridHeight" title>
              <v-card-title class="pt-16 justify-center">No Reel Added Yet</v-card-title>
            </v-card>
          </v-col>
        </template>
      </GridComponent>
      <div v-if="isActorMakeuporDancer">
        <lightBoxGallery
          v-show="modalVisible"
          :currentImage="currentImage"
          :sortedPhotoList="sortedPhotoList"
          @close="closeModal"
        ></lightBoxGallery>
        <GridComponent class="mt-lg-6" :gridWidth="gridWidth">
          <template v-if="!noProjectsYet" #rowTitleOne>Additional Photos</template>

          <template #cardSlot>
            <template v-for="(photo,index) in photoList.slice(0,9)">
              <v-col v-if="!bg" :key="photo.id" justify="end" cols="12" sm="4">
                <v-card :key="photo.id" :height="gridHeight" outlined title>
                  <v-img
                    @click="lightboxEffect(index);
                      showModal()"
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="photo.photos"
                  ></v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isDirector">
        <GridComponent :gridWidth="gridWidth">
          <template v-if="!noProjectsYet" #rowTitleOne>Additional Works</template>
          <template #cardSlot>
            <template v-for="reel in sortedReelList">
              <v-col :key="reel.id" justify="end" cols="12" sm="4">
                <v-card :key="reel.id" :height="gridHeight" outlined title>
                  <a :href="reel.reel" target="_blank">
                    <v-img class="white--text align-end" :height="gridHeight" :src="reel.thumbnail">
                      <v-card-title
                        class="mb-n4 text-lg-h5 text-subtitle-2"
                        align="end"
                      >{{reel.title}}</v-card-title>
                      <v-card-text class="mb-lg-3 text-lg-h6 text-subtitle-1">{{reel.year_created}}</v-card-text>
                    </v-img>
                  </a>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isCrewMember">
        <lightBoxGallery
          v-show="modalVisible"
          :currentImage="currentImage"
          :cardsList="cardsList"
          :isCardsList="isCardsList"
          @close="closeModal"
        ></lightBoxGallery>
        <GridComponent class="mt-lg-6" :gridWidth="gridWidth">
          <template v-if="!noProjectsYet" #rowTitleOne>Past Works</template>

          <template #cardSlot>
            <template v-for="(card, index) in cardsList.slice(0,9)">
              <v-col v-if="!bg" :key="card.id" justify="end" cols="12" sm="4">
                <v-card :key="card.id" :height="gridHeight" outlined title>
                  <v-img
                    @click="lightboxEffect(index);
                      showModal()"
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="card.thumbnail"
                  >
                    <v-card-title class="text-lg-h5 text-subtitle-2" align="end">{{card.card_title}}</v-card-title>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isWriter">
        <GridComponent :gridWidth="gridWidth">
          <template v-if="!noProjectsYet" #rowTitleOne>My Work</template>
          <template #cardSlot>
            <template v-for="writingSample in sortedSampleList">
              <v-col :key="writingSample.id" justify="end" cols="12" sm="4">
                <v-card :key="writingSample.id" :height="gridHeight" outlined title>
                  <a :href="writingSample.samples" target="_blank">
                    <v-img
                      class="white--text align-end"
                      :height="gridHeight"
                      :src="writingSample.thumbnail"
                    >
                      <v-card-title
                        class="mb-n4 text-lg-h5 text-subtitle-2"
                        align="end"
                      >{{writingSample.title}}</v-card-title>
                      <v-card-text
                        class="mb-lg-3 text-lg-h6 text-subtitle-1"
                      >{{writingSample.year_created}}</v-card-text>
                    </v-img>
                  </a>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isPhotographer">
        <lightBoxGallery
          v-show="modalVisible"
          :currentImage="currentImage"
          :sortedPhotoList="sortedPhotoList"
          @close="closeModal"
        ></lightBoxGallery>
        <GridComponent :gridWidth="gridWidth">
          <template v-if="!noProjectsYet" #rowTitleOne>My Work</template>

          <template #cardSlot>
            <template v-for="(photo,index) in sortedPhotoList">
              <v-col v-if="!bg" :key="photo.id" justify="end" cols="12" sm="4">
                <v-card :key="photo.id" :height="gridHeight" outlined title>
                  <v-img
                    @click=" lightboxEffect(index);
                      showModal()"
                    class="white--text align-end"
                    :height="gridHeight"
                    :src="photo.photos"
                  >
                    <v-card-title
                      class="mb-n4 text-lg-h5 text-subtitle-2"
                      align="end"
                    >{{photo.title}}</v-card-title>
                    <v-card-text class="mb-lg-3 text-lg-h6 text-subtitle-1">{{photo.year_created}}</v-card-text>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
    </v-app>
    <FooterComponent />
  </div>
</template>
<script>
import SideBarComponent from "~/components/SideBarComponent";
import TopNavbar from "~/components/TopNavbar";
import FooterComponent from "~/components/FooterComponent";
import GridComponent from "~/components/GridComponent";
import lightBoxGallery from "~/components/lightBoxGallery";
import SubscribeComponent from "~/components/SubscribeComponent.vue";
import { mapGetters } from "vuex";
export default {
  head() {},
  components: {
    GridComponent,
    FooterComponent,
    TopNavbar,
    SideBarComponent,
    lightBoxGallery,
    SubscribeComponent
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
    ...mapGetters(["loggedInUser"]),
    sortedReelList() {
      return this.reelList.slice(0, 6);
    },
    sortedSampleList() {
      return this.sampleList.slice(0, 6);
    },
    sortedPhotoList() {
      return this.photoList.slice(0, 18);
    },
    noProjectsYet() {
      if (
        this.sampleList == "" &&
        this.reelList == "" &&
        this.photoList == ""
      ) {
        return true;
      }
    },
    noReelYet() {
      if (
        this.actors.reel == null &&
        this.actors.group !== "Writers" &&
        this.actors.group !== "Photographers"
      ) {
        return true;
      }
    },
    isPhotographer() {
      if (this.actors.group == "Photographers") {
        return true;
      }
    },
    isDirector() {
      if (this.actors.group == "Directors") {
        return true;
      }
    },
    isActorMakeuporDancer() {
      if (
        this.actors.group == "Actors" ||
        this.actors.group == "Makeup Artist" ||
        this.actors.group == "Dancers"
      ) {
        return true;
      }
    },
    isCrewMember() {
      if (
        this.actors.group == "Post Production" ||
        this.actors.group == "Production"
      ) {
        return true;
      }
    },
    isWriter() {
      if (this.actors.group == "Writers") {
        return true;
      }
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
          return "350px";
      }
    }
  },
  async asyncData({ $axios, params, store }) {
    const body = store.getters.loggedInUser.id;
    try {
      const [
        actors,
        photoList,
        sampleList,
        reelList,
        cardsList
      ] = await Promise.all([
        $axios.$get(`/api/v1/actors/${params.id}/`),
        $axios.$get(`/api/v1/photos/`, {
          params: {
            user: params.id
          }
        }),
        $axios.$get(`/api/v1/writingsamples/`, {
          params: {
            user: params.id
          }
        }),
        $axios.$get(`/api/v1/reels/`, {
          params: {
            user: params.id
          }
        }),
        $axios.$get(`/api/v1/crewcards/`, {
          params: {
            user: params.id
          }
        })
      ]);
      return { actors, photoList, sampleList, reelList, cardsList };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
    }
  },
  methods: {
    copyText(text) {
      navigator.clipboard.writeText(text);
      window.alert("Email copied to clipboard!");
    },
    socialLink(link) {
      this.$router.push(link);
    },
    lightboxEffect(curr) {
      this.currentImage = curr;
      this.bg = !this.bg;
    },
    showModal() {
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;
      this.bg = !this.bg;
    }
  },
  data() {
    return {
      isCardsList: true,
      gridWidth: "10",
      sideHeight: `20vh`,
      hasPermission: true,
      actors: {},
      sampleList: [],
      reelList: [],
      photoList: [],
      sources: [],
      currentImage: 0,
      bg: false,
      modalVisible: false
    };
  }
};
</script>