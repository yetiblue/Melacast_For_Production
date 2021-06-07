<template>
  <div>
    <TopNavbar />
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
            <v-btn class="mb-2 brown white--text" elevation="0" block>Contact Me</v-btn>
            <v-btn
              class="mb-2 brown text-lg-caption white--text"
              elevation="0"
              block
            >{{actors.email}}</v-btn>
            <v-card-title class="text-center">Languages</v-card-title>
            <v-card-text>{{actors.languages_spoken}}</v-card-text>
          </template>

          <template #userMobileProfile>
            <v-card-subtitle class="text-center">www.melacast.com</v-card-subtitle>
            <v-card-actions class="justify-center">
              <v-icon class="ml-2 ml-lg-0">mdi-instagram</v-icon>
              <v-icon class="ml-4">mdi-youtube</v-icon>

              <v-icon class="ml-4">mdi-vimeo</v-icon>
              <v-icon class="ml-4">mdi-linkedin</v-icon>
            </v-card-actions>
            <v-card-title class="justify-center">Project Interests</v-card-title>
            <v-card-text class="text-center">Cool Stuff Cool Stuff Cool Stuff</v-card-text>
            <v-card-actions class="justify-center">
              <v-btn class="mb-2 brown mx-auto white--text" elevation="0">Contact Me</v-btn>
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
        </v-col>
      </v-row>
      <div v-if="isActorDirectororDancer">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>My Work</template>
          <template #cardSlot>
            <template v-for="reel in sortedReelList">
              <v-col :key="reel.id" justify="end" cols="12" sm="4">
                <v-card
                  :key="reel.id"
                  :to="`/actors/${reel.id}/`"
                  :height="gridHeight"
                  outlined
                  title
                >
                  <v-img class="white--text align-end" :height="gridHeight" :src="reel.thumbnail">
                    <v-card-title
                      class="mb-n4 text-lg-h5 text-subtitle-2"
                      align="end"
                    >{{reel.title}}</v-card-title>
                    <v-card-text
                      class="mb-lg-5 mb-7 text-lg-h6 text-subtitle-1"
                    >{{reel.year_created}}</v-card-text>

                    <v-row align="center" justify="end"></v-row>
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isWriter">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>My Work</template>
          <template #cardSlot>
            <template v-for="reel in sortedReelList">
              <v-col :key="reel.id" justify="end" cols="12" sm="4">
                <v-card
                  :key="reel.id"
                  :to="`/actors/${reel.id}/`"
                  :height="gridHeight"
                  outlined
                  title
                >
                  <v-img class="white--text align-end" :height="gridHeight" :src="reel.thumbnail">
                    <!-- <v-card-title
                    class="mb-n6 text-lg-h5 text-subtitle-2"
                    align="end"
                  >{{individualActor.firstname}} {{individualActor.middle}} {{individualActor.lastname}}</v-card-title>
                  <v-card-text
                    class="mb-lg-n5 mb-n7 text-lg-h6 text-subtitle-1"
                  >{{individualActor.group}}</v-card-text>
                  <v-card-text class="mb-5 text-caption text-lg-subtitle-1">
                    Member Since
                    {{ individualActor.date_joined }}
                  </v-card-text>
                    <v-row align="center" justify="end"></v-row>-->
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-if="isPhotographer">
        <GridComponent :gridWidth="gridWidth">
          <template #rowTitleOne>My Work</template>
          <template #cardSlot>
            <template v-for="reel in sortedReelList">
              <v-col :key="reel.id" justify="end" cols="12" sm="4">
                <v-card
                  :key="reel.id"
                  :to="`/actors/${reel.id}/`"
                  :height="gridHeight"
                  outlined
                  title
                >
                  <v-img class="white--text align-end" :height="gridHeight" :src="reel.thumbnail">
                    <!-- <v-card-title
                    class="mb-n6 text-lg-h5 text-subtitle-2"
                    align="end"
                  >{{individualActor.firstname}} {{individualActor.middle}} {{individualActor.lastname}}</v-card-title>
                  <v-card-text
                    class="mb-lg-n5 mb-n7 text-lg-h6 text-subtitle-1"
                  >{{individualActor.group}}</v-card-text>
                  <v-card-text class="mb-5 text-caption text-lg-subtitle-1">
                    Member Since
                    {{ individualActor.date_joined }}
                  </v-card-text>
                    <v-row align="center" justify="end"></v-row>-->
                  </v-img>
                </v-card>
              </v-col>
            </template>
          </template>
        </GridComponent>
      </div>
      <div v-else>
        <v-row>
          <v-col cols="10">
            No Projects Yet?
            <v-btn>Click Here</v-btn>
          </v-col>
        </v-row>
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
// import SubscribeComponent from "~/components/SubscribeComponent.vue";
import { mapGetters } from "vuex";
export default {
  head() {
    return {
      title: "View Recipe"
    };
  },
  components: {
    GridComponent,
    FooterComponent,
    TopNavbar,
    SideBarComponent
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
    isPhotographer() {
      if (this.actors.group == "Photographers") {
        return true;
      }
    },
    isActorDirectororDancer() {
      if (
        this.actors.group == "Actors" ||
        this.actors.group == "Directors" ||
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
          return "320px";
        case "sm":
          return "240px";
        case "xs":
          return "35vh";
        case "lg":
          return "465px";
      }
    }
  },
  async asyncData({ $axios, params, store }) {
    const body = store.getters.loggedInUser.id;
    try {
      const [actors, photoList, sampleList, reelList] = await Promise.all([
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
        })
      ]);
      return { actors, photoList, sampleList, reelList };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
    }
  },
  methods: {
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