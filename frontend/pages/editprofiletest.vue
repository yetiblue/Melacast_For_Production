//
<script>
// import { mapGetters } from "vuex";
// import Navigation from "~/Components/Navigation";
// import SubscribeComponent from "~/Components/SubscribeComponent.vue";
// import PprojGrid from "~/Components/PprojGrid";
// import DashboardSideNavigation from "~/Components/DashboardSideNavigation";
// export default {
//   head() {
//     return {
//       title: "Edit Profile Form"
//     };
//   },
//   components: {
//     SubscribeComponent,
//     Navigation,
//     PprojGrid,
//     DashboardSideNavigation
//   },
//   computed: {
//     ...mapGetters(["loggedInUser"]),

//     updatedActor: function(actor) {
//       //resume field throws error since it's required. Because it's not being uploaded here, gotta
//       //restructure the data returned in 'actor' and patch that instead

//       //REPLACE IN THE CALL BY USING formDATA.DELETE THOSE FIELDS
//       return {
//         // headshot: this.actor[0].headshot,
//         ethnicity: this.actor[0].ethnicity,
//         age: this.actor[0].age,
//         firstname: this.actor[0].firstname,
//         lastname: this.actor[0].lastname,
//         middle: this.actor[0].middle,
//         location: this.actor[0].location,
//         website: this.actor[0].website,
//         Instagram_Handle_if_applicable: this.actor[0]
//           .Instagram_Handle_if_applicable,
//         project_types: this.actor[0].project_types,
//         writing_genres: this.actor[0].writing_genres
//       };
//     },
//     //UPDATE THIS SECTION WITH THE NEW GROUPINGS AND REMOVE DANCER
//     isDirector() {
//       if (this.actor[0].group == "Director") {
//         return true;
//       }
//     },
//     isPhotographerOrMakeup() {
//       if (
//         this.actor[0].group == "Photographers" ||
//         this.actor[0].group == "Makeup"
//       ) {
//         return true;
//       }
//     },
//     isActorDirectororDancer() {
//       if (
//         this.actor[0].group == "Actors" ||
//         this.actor[0].group == "Directors" ||
//         this.actor[0].group == "Dancer"
//       ) {
//         return true;
//       }
//     },
//     isWriter() {
//       if (this.actor[0].group == "Writers") {
//         return true;
//       }
//     }
//   },
//   async asyncData({ $axios, params, store }) {
//     const body = store.getters.loggedInUser.id;
//     try {
//       const [actor, photoList, writingSampleList, reelList] = await Promise.all(
//         [
//           $axios.$get(`/api/v1/actors/`, {
//             params: {
//               user: body
//             }
//           }),
//           $axios.$get(`/api/v1/photos/`, {
//             params: {
//               user: body
//             }
//           }),
//           $axios.$get(`/api/v1/writingsamples/`, {
//             params: {
//               user: body
//             }
//           }),
//           $axios.$get(`/api/v1/reels/`, {
//             params: {
//               user: body
//             }
//           })
//         ]
//       );
//       return { actor, photoList, writingSampleList, reelList };
//     } catch (error) {
//       if (error.response.status === 403) {
//         const hasPermission = false;
//         console.log(hasPermission, "perm");
//         return { hasPermission };
//       }
//     }
//   },
//   data() {
//     return {
//       hasPermission: true,
//       actor: {}, // returned from API
//       preview: "", //probably not needed, the preview for the uploaded image isn't being used.
//       addProj: false,
//       hasResume: false,
//       hasSample: false,
//       hasSampleThumbnail: false,
//       hasReel: false,
//       hasReelThumbnail: false,
//       hasPhotos: false,
//       hasHeadshot: false
//     };
//   },
//   methods: {
//     onPhotoChange() {
//       this.photos = this.$refs.photos.files;
//       console.log(this.photos);
//       this.hasPhotos = true;
//     },
//     onReelChange() {
//       this.reel = this.$refs.reel.files;
//       console.log(this.reel);
//       this.hasReel = true;
//       console.log(this.hasReel, "has reel");
//     },
//     onThumbnailChange() {
//       this.thumbnail = this.$refs.thumbnail.files;
//       console.log(this.thumbnail);
//       this.hasReelThumbnail = true;
//       console.log(this.hasReelThumbnail, "reel thumbn");
//     },
//     onSampleChange() {
//       this.samples = this.$refs.sample.files;
//       console.log(this.samples);
//       this.hasSample = true;
//       console.log(this.hasSample, "has reel");
//     },
//     onSampleThumbnailChange() {
//       this.thumbnail = this.$refs.sampleThumbnail.files;
//       console.log(this.thumbnail);
//       this.hasSampleThumbnail = true;
//       console.log(this.hasSampleThumbnail, "reel thumbn");
//     },
//     onResumeChange(e) {
//       this.newResume = this.$refs.resume.files;
//       console.log(this.newResume);
//       this.hasResume = true;
//     },
//     onHeadshotChange() {
//       this.headshot = this.$refs.headshot.files;
//       console.log(this.headshot);
//       this.hasHeadshot = true;
//     },
//     // onHeadshotChange(e) {
//     //   let files = e.target.files || e.dataTransfer.files;
//     //   if (!files.length) {
//     //     return;
//     //   }
//     //   this.headshotChanged = true;
//     //   this.updatedActor.headshot = files[0];
//     //   this.createHeadshot(files[0]);
//     // },
//     // createHeadshot(file) {
//     //   let reader = new FileReader();
//     //   let vm = this;
//     //   reader.onload = e => {
//     //     vm.preview = e.target.result;
//     //   };
//     //   reader.readAsDataURL(file);
//     // },
//     async updateProfile($axios) {
//       let editedForm = this.updatedActor;
//       const config = {
//         headers: {
//           "content-type": "multipart/form-data; "
//         }
//       };
//       let formData = new FormData();
//       for (let data in editedForm) {
//         formData.append(data, editedForm[data]);
//       }
//       //FORMDATA.DELETE RESUME, HEADSHOT ETC ETC
//       try {
//         let response = await this.$axios.$patch(
//           `/api/v1/actors/${this.actor[0].id}/`,
//           formData,
//           config
//         );
//         this.submitNewHeadshot();
//         //SUBMIT NEW RESUME HERE TOO
//         // this.$router.push("/profile/");
//       } catch (error) {
//         console.log(error);
//       }
//     },
//     deletePhoto(photoID, $axios) {
//       let deletionID = photoID;
//       this.$axios.delete(`/api/v1/photos/${deletionID}/`);
//       this.$router.go();
//     },
//     deleteSample(sampleID, $axios) {
//       let deletionID = sampleID;
//       this.$axios.delete(`/api/v1/writingsamples/${deletionID}/`);
//       this.$router.go();
//     },
//     deleteReel(reelID, $axios) {
//       let deletionID = reelID;
//       this.$axios.delete(`/api/v1/reels/${deletionID}/`);
//       this.$router.go();
//     },
//     submitPhotos(axios) {
//       console.log("submit photos");
//       if (this.hasPhotos == true) {
//         for (var i = 0; i < this.photos.length; i++) {
//           let photoData = new FormData();
//           let photo = this.photos[i];
//           photoData.append("photos", photo);
//           const config = {
//             headers: {
//               "content-type": "multipart/form-data; "
//             }
//           };
//           this.$axios
//             .post(`/api/v1/photos/`, photoData, config)
//             .then(response => {
//               console.log("Successfully Submitted Images");
//               this.$router.go();
//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       } else {
//       }
//     },
//     submitReel(axios) {
//       console.log("submit reels");
//       if (this.hasReel == true && this.hasReelThumbnail == true) {
//         for (var i = 0; i < this.reel.length; i++) {
//           console.log("first checkpoint");
//           let reelData = new FormData();
//           let reel = this.reel[i];
//           let thumbnail = this.thumbnail[i];
//           reelData.append("reel", reel);
//           reelData.append("thumbnail", thumbnail);
//           console.log(reelData, "reelData");
//           const config = {
//             headers: {
//               "content-type": "multipart/form-data; "
//             }
//           };
//           this.$axios
//             .post(`/api/v1/reels/`, reelData, config)
//             .then(response => {
//               console.log("Successfully Submitted reels");
//               this.$router.go();
//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       } else {
//       }
//     },
//     submitSample(axios) {
//       console.log("submit reels");
//       if (this.hasSample == true && this.hasSampleThumbnail == true) {
//         for (var i = 0; i < this.samples.length; i++) {
//           console.log("first checkpoint");
//           let sampleData = new FormData();
//           let sample = this.samples[i];
//           let thumbnail = this.thumbnail[i];
//           sampleData.append("samples", sample);
//           sampleData.append("thumbnail", thumbnail);
//           console.log(sampleData, "sampleData");
//           const config = {
//             headers: {
//               "content-type": "multipart/form-data; "
//             }
//           };
//           this.$axios
//             .post(`/api/v1/writingsamples/`, sampleData, config)
//             .then(response => {
//               console.log("Successfully Submitted samples");
//               this.$router.go();
//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       } else {
//       }
//     },
//     submitNewHeadshot($axios) {
//       if (this.hasHeadshot == true) {
//         for (var i = 0; i < this.headshot.length; i++) {
//           console.log("first checkpoint");
//           let headshotData = new FormData();
//           let headshot = this.headshot[i];
//           headshotData.append("headshot", headshot);
//           console.log(headshotData, "sampleData");
//           const config = {
//             headers: {
//               "content-type": "multipart/form-data; "
//             }
//           };
//           this.$axios
//             .patch(`/api/v1/actors/${this.actor[0].id}/`, headshotData, config)
//             .then(response => {
//               console.log("Successfully Submitted headshot");
//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       } else {
//       }
//     },
//     submitNewResume(axios) {
//       if (this.hasResume == true) {
//         for (var i = 0; i < this.newResume.length; i++) {
//           let resumeData = new FormData();
//           let newResume = this.newResume[i];
//           resumeData.append("resume", newResume);
//           const config = {
//             headers: {
//               "content-type": "multipart/form-data; "
//             }
//           };
//           this.$axios
//             .patch(`/api/v1/actors/${this.actor[0].id}/`, resumeData, config)
//             .then(response => {
//               console.log("Successfully Submitted New Resume");
//             })
//             .catch(error => {
//               console.log(error);
//             });
//         }
//       } else {
//         //do nothing here if someone doesn't want to change resume
//       }
//     }
//   }
// };
//
</script>
