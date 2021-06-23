<template>
  <div>
    <TopNavbar />
    <v-app id="bigGrid">
      <div v-if="!mobile"></div>
      <stripe-checkout
        mode="payment"
        ref="checkoutRef"
        :pk="publishableKey"
        :lineItems="lineItems"
        :successUrl="successUrl"
        :cancelUrl="cancelUrl"
        :payment_status="payment_status"
        :clientReferenceId="clientReference"
      />

      <v-row v-if="!secondPage && !fourthPage && !thirdPage && !displayFifth">
        <v-spacer></v-spacer>
        <v-col class="px-10 px-sm-0" lg="6" cols="12" sm="8">
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start">Tell Us About Your Film</v-card-title>
            <v-card-subtitle>Add basic details to introduce this project.</v-card-subtitle>
          </v-card>
          <v-row justify="center">
            <v-col cols="12" sm="8">
              <v-text-field outlined justify="center" v-model="form.title" label="Project Title"></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                justify="center"
                v-model="form.director_email"
                label="Director's Email"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-textarea label="Bio" outlined v-model="form.overview" color="teal">
                <template v-slot:label>
                  <div>Project Logline</div>
                </template>
              </v-textarea>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                justify="center"
                v-model="form.studio"
                label="Production Studio"
              ></v-text-field>
            </v-col>
            <v-col class="ml-lg-4" outlined style="height=10vh" cols="12" sm="12">
              <v-card class="pl-md-16 ml-lg-16 ml-md-10 ml-sm-16 pl-sm-2" elevation="0">
                <v-card-title
                  v-if="!posterUploaded"
                  class="text-md-h6 ml-n4 ml-sm-0 text-subtitle-2"
                >Upload a project banner or choose one from our gallery</v-card-title>
                <v-card-title
                  v-if="!hideUploadName"
                  class="text-lg-subtitle-1"
                >{{displayPosterName}}</v-card-title>
                <v-img
                  :aspect-ratio="16/9"
                  class="grey mb-lg-6 ml-sm-2"
                  max-height="315px"
                  :width="galleryPreviewWidth"
                  v-if="galleryPhotoSelected"
                  :src="selectedGalleryPhoto"
                ></v-img>
              </v-card>
            </v-col>
            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="!mobile" class="mb-6">
                <v-col class="pl-12" cols="12" sm="6">
                  <v-btn
                    class="white--text ml-16 ml-lg-n10"
                    width="15vw"
                    height="60px"
                    color="brown"
                    depressed
                    @click="inputFileClick"
                  >
                    <v-icon left>mdi-upload</v-icon>Thumbnail
                  </v-btn>
                  <input type="file" style="display: none" ref="poster" @change="createPoster" />
                </v-col>

                <v-col cols="12" class="pl-8" sm="1">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="white--text ml-sm-n4"
                        width="15vw"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="generatePosterFromComponent" />
                    </v-card>
                  </v-dialog>
                </v-col>
              </v-row>
              <v-spacer></v-spacer>
            </v-col>

            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="mobile" class="mb-6">
                <v-col class="pl-sm-12" cols="12" sm="6" lg="6">
                  <v-btn
                    class="white--text ml-n16 ml-sm-16 ml-sm-n10 ml-lg-n10"
                    :width="buttonWidth"
                    height="60px"
                    color="brown"
                    depressed
                    @click="inputFileClick"
                  >
                    <v-icon left>mdi-upload</v-icon>Thumbnail
                  </v-btn>
                  <input type="file" style="display: none" ref="poster" @change="createPoster" />
                </v-col>

                <v-col cols="12" class="pl-sm-8" sm="3" lg="1">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="ml-n16 white--text ml-sm-n4"
                        :width="buttonWidth"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="generatePosterFromComponent" />
                    </v-card>
                  </v-dialog>
                </v-col>
              </v-row>
              <v-spacer></v-spacer>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select outlined v-model="form.location" :items="states" label="Location (state)"></v-select>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                v-model="form.city_location"
                justify="center"
                label="Location (City)"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="8">
              <v-menu
                v-model="startDateMenuOpen"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    outlined
                    label="Start Date"
                    readonly
                    :value="form.start_date"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="form.start_date"
                  no-title
                  @input="startDateMenuOpen = false"
                ></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12" sm="8">
              <v-menu
                v-model="endDateMenuOpen"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field outlined label="End Date" readonly :value="form.end_date" v-on="on"></v-text-field>
                </template>
                <v-date-picker v-model="form.end_date" no-title @input="endDateMenuOpen = false"></v-date-picker>
              </v-menu>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select
                outlined
                v-model="form.status"
                justify="center"
                :items="payStatus"
                label="Pay Status"
              ></v-select>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select
                outlined
                v-model="form.job_type"
                justify="center"
                :items="timeCommit"
                label="Time Commitment"
              ></v-select>
            </v-col>
            <v-col outlined style="height=10vh" cols="12">
              <v-card
                class="pl-lg-16 pl-md-16 ml-md-10 ml-n4 ml-sm-16 pl-sm-2 ml-lg-16"
                elevation="0"
              >
                <v-card-title class="text-lg-subtitle-1 text-subtitle-1 text-sm-h6 bold">
                  <b>What Best Describes Your Film?</b>
                </v-card-title>
                <v-card-subtitle>Check One</v-card-subtitle>
              </v-card>
            </v-col>
            <v-col outlined style="height=10vh" cols="8" sm="5">
              <v-checkbox v-model="form.genre" label="Animation" color="green" value="Animation"></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Documentary"
                color="green"
                value="Documentary"
              ></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Experimental"
                color="green"
                value="Experimental"
              ></v-checkbox>
              <v-checkbox v-model="form.genre" label="Feature" color="green" value="Feature"></v-checkbox>
              <v-checkbox
                v-model="form.genre"
                label="Music Video"
                color="green"
                value="Music Video"
              ></v-checkbox>
              <v-checkbox v-model="form.genre" label="Short" color="green" value="Short"></v-checkbox>
            </v-col>
            <v-col outlined style="height=10vh" cols="4" sm="3">
              <v-checkbox v-model="form.genre" label="Student" color="green" value="Student"></v-checkbox>
              <v-checkbox v-model="form.genre" label="Television" color="green" value="Television"></v-checkbox>
              <v-checkbox
                v-model="form.tags"
                label="Virtual Reality"
                color="green"
                value="Virtual Reality"
              ></v-checkbox>
              <v-checkbox
                v-model="form.tags"
                label="Web / New Media"
                color="green"
                value="Web/New Media"
              ></v-checkbox>
              <v-checkbox v-model="form.tags" label="Theater" color="green" value="Theater"></v-checkbox>
            </v-col>
          </v-row>

          <v-row justify="center">
            <!-- <v-col cols="6"></v-col> -->
            <v-spacer></v-spacer>
            <v-col cols="4" sm="3">
              <v-btn @click="secondPage = !secondPage" style="margin-top: 50px;">Next</v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
      <v-row v-if="secondPage && !thirdPage && !fourthPage">
        <v-spacer></v-spacer>
        <v-col class="px-10 px-sm-0" lg="6" cols="12" sm="8">
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start">Add Roles</v-card-title>
            <v-card-subtitle>Add any non post or production crew positions. Specifications are optional.</v-card-subtitle>
          </v-card>
          <v-row justify="center">
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                justify="center"
                v-model="filmRoles.role_name"
                label="Role Type (Lead Actor, Support Dancer, Photographer, etc)"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-text-field
                outlined
                justify="center"
                v-model="filmRoles.character_name"
                label="Character Name (Optional)"
                maxlength="500"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="8">
              <v-textarea label="Bio" outlined v-model="filmRoles.role_description" color="teal">
                <template v-slot:label>
                  <div>Role Description</div>
                </template>
              </v-textarea>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select
                outlined
                justify="center"
                :items="ethnicities"
                v-model="filmRoles.ethnicity"
                label="Character Ethnicity (Optional)"
              ></v-select>
            </v-col>
            <v-col cols="12" sm="8">
              <v-select
                outlined
                justify="center"
                :items="professions"
                v-model="filmRoles.role_type"
                label="Role Type"
              ></v-select>
            </v-col>
            <v-col outlined style="height=10vh" cols="12" sm="12">
              <v-card class="pl-md-16 ml-xl-16 ml-md-10 ml-sm-16 pl-sm-2" elevation="0">
                <v-card-title
                  v-if="!posterUploaded"
                  class="text-md-h6 pl-lg-8 ml-n4 ml-sm-0 ml-lg-2 text-subtitle-2"
                >Pick a thumbnail for this role</v-card-title>

                <v-img
                  :aspect-ratio="16/9"
                  class="mb-lg-6 ml-sm-4 ml-lg-10"
                  max-height="310px"
                  :width="galleryPreviewWidth"
                  v-if="galleryPhotoSelected"
                  :src="filmRoles.role_thumbnail"
                ></v-img>
              </v-card>
            </v-col>
            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="!mobile" class="mb-6">
                <v-col class="pl-12" cols="12" sm="6">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="white--text ml-n16 ml-sm-16 ml-sm-n10 ml-lg-n10"
                        :width="buttonWidth"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="filmRoleGalleryPhoto" />
                    </v-card>
                  </v-dialog>
                </v-col>

                <v-col cols="12" class="pl-8" sm="1">
                  <v-btn
                    justify="center"
                    class="white--text ml-sm-n4"
                    width="15vw"
                    height="60px"
                    color="brown"
                    @click.prevent="addRoles()"
                    depressed
                  >Submit</v-btn>
                </v-col>
              </v-row>
              <v-spacer></v-spacer>
            </v-col>

            <v-col cols="8">
              <v-spacer></v-spacer>
              <v-row v-if="mobile" class="mb-6">
                <v-col class="pl-sm-12" cols="12" sm="6" lg="6">
                  <v-dialog v-model="dialog">
                    <template v-slot:activator="{ on }">
                      <v-btn
                        justify="center"
                        class="white--text ml-n16 ml-sm-16 ml-sm-n10 ml-lg-n10"
                        :width="buttonWidth"
                        height="60px"
                        color="brown"
                        depressed
                        v-on="on"
                      >
                        <v-icon left>mdi-upload</v-icon>Gallery
                      </v-btn>
                    </template>
                    <v-card dark>
                      <GalleryThumbnailComponent @clicked="filmRoleGalleryPhoto" />
                    </v-card>
                  </v-dialog>
                </v-col>

                <v-col cols="12" class="pl-sm-8" sm="1">
                  <v-btn
                    justify="center"
                    class="white--text ml-sm-n4 ml-n16"
                    :width="buttonWidth"
                    height="60px"
                    color="brown"
                    @click.prevent="addRoles()"
                    depressed
                  >Submit</v-btn>
                </v-col>
              </v-row>
              <v-divider></v-divider>
              <v-spacer></v-spacer>
            </v-col>
            <v-col outlined class="ml-lg-n16" style="height=10vh" cols="12" sm="12">
              <template v-for="returnedRole in returnedFilmRoles">
                <v-card
                  :key="returnedRole.id"
                  class="pl-md-16 ml-md-10 ml-sm-10 ml-md-n2 ml-lg-8 ml-xl-0 pl-sm-2"
                  elevation="0"
                >
                  <v-card-title
                    class="ml-sm-n4"
                  >{{returnedRole.role_name}} | {{returnedRole.character_name}} | {{returnedRole.role_type}} | {{returnedRole.ethnicity}}</v-card-title>

                  <v-card-subtitle
                    class="mt-lg-6 mt-sm-2 ml-sm-n4"
                  >{{returnedRole.role_description}}</v-card-subtitle>

                  <v-img class="mr-lg-6" :aspect-ratio="16/9" :src="returnedRole.role_thumbnail"></v-img>
                  <v-spacer></v-spacer>
                  <v-row class="justify-end">
                    <v-btn
                      justify-end
                      class="text--brown text-right mt-8 mr-sm-3 mr-lg-9"
                      text
                      outlined
                      @click="deleteRole(returnedRole.id)"
                    >Delete</v-btn>
                  </v-row>

                  <v-divider></v-divider>
                </v-card>
              </template>
            </v-col>
          </v-row>

          <v-row justify="center">
            <!-- <v-col cols="6"></v-col> -->
            <v-spacer></v-spacer>
            <v-col cols="7" sm="6">
              <v-btn
                class="ml-n2 ml-sm-0"
                @click="secondPage = !secondPage"
                style="margin-top: 50px;"
              >Back</v-btn>
            </v-col>
            <v-col cols="4" md="4" sm="4">
              <v-btn
                @click="thirdPage =!thirdPage"
                class="ml-md-0 ml-lg-6"
                style="margin-top: 50px;"
              >Next</v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
      <v-row v-if="thirdPage && !fourthPage">
        <v-spacer></v-spacer>
        <v-col class="px-10 px-sm-0" lg="6" cols="12" sm="8">
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start">Add Crew Members</v-card-title>
            <v-card-subtitle>Add any crew member types that you will need for this project.</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-subtitle-1">
              <b>Production</b>
            </v-card-title>
            <v-card-subtitle>(Check all that apply).</v-card-subtitle>
          </v-card>
          <v-row class="pr-10">
            <v-spacer></v-spacer>

            <v-col outlined style="height=10vh" cols="8" sm="10">
              <v-checkbox value="true" v-model="hasArt" label="Art Team" />
              <v-text-field v-model="productionRoles.role_name" />
              <v-btn @click="addProduction(art)">Add</v-btn>
              <v-card-subtitle
                v-for="returnedProduction in returnedProductionRoles"
                :key="returnedProduction.id"
              >{{returnedProduction.role_name}}</v-card-subtitle>

              <v-checkbox value="true" v-model="hasCamera" label="Camera Team" />
              <v-text-field v-model="form.crew_positions" />
            </v-col>
          </v-row>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="text-subtitle-1 justify-start">
              <b>Post Production</b>
            </v-card-title>
            <v-card-subtitle>(Check all that apply).</v-card-subtitle>
          </v-card>
          <v-row class="pr-10">
            <v-spacer></v-spacer>

            <v-col outlined style="height=10vh" cols="8" sm="4">
              <v-checkbox value="Editing" v-model="form.post_production_positions" label="Editing" />
              <v-checkbox
                value="Sound Mixer"
                v-model="form.post_production_positions"
                label="Sound Mixer"
              />
              <v-checkbox
                value="Music Composer"
                v-model="form.post_production_positions"
                label="Music Composer"
              />
              <v-checkbox
                value="Audio Engineer"
                v-model="form.post_production_positions"
                label="Audio Engineer"
              />
            </v-col>
            <v-col outlined style="height=10vh" cols="4" sm="6">
              <v-checkbox
                value="Sound Editor"
                v-model="form.post_production_positions"
                label="Sound Editor"
              />
              <v-checkbox
                value="Producer"
                v-model="form.post_production_positions"
                label="Producer"
              />

              <v-spacer></v-spacer>
            </v-col>
          </v-row>
          <v-row justify="center">
            <!-- <v-col cols="6"></v-col> -->
            <v-spacer></v-spacer>
            <v-col cols="7" sm="6">
              <v-btn
                class="ml-n2 ml-sm-0"
                @click="thirdPage = !thirdPage"
                style="margin-top: 50px;"
              >Back</v-btn>
            </v-col>
            <v-col cols="4" md="4" sm="4">
              <v-btn
                @click="fourthPage =!fourthPage"
                class="ml-md-0 ml-lg-6"
                style="margin-top: 50px;"
              >Next</v-btn>
            </v-col>
          </v-row>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
      <v-row v-if="fourthPage">
        <v-spacer></v-spacer>
        <v-col class="px-10 px-sm-0" lg="6" cols="12" sm="8">
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start">Confirm details and post listing</v-card-title>
            <v-card-subtitle>Your project will now be live and searchable on The Melacast Network.</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-img class="grey mr-lg-6" :aspect-ratio="16/9" :src="selectedGalleryPhoto">
              <v-row height="200px" class="mt-lg-12 align-center justify-center">
                <v-card-title class="mt-lg-16 pt-lg-16" v-if="hasPoster">{{displayPosterName }}</v-card-title>
              </v-row>
            </v-img>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Movie Title</b>
            </v-card-title>
            <v-card-subtitle>{{form.title}}</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Production Studio</b>
            </v-card-title>
            <v-card-subtitle>{{form.studio}}</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Location</b>
            </v-card-title>
            <v-card-subtitle>{{form.city_location}}, {{form.location}}</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Logline</b>
            </v-card-title>
            <v-card-subtitle>{{form.overview}}</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-row>
              <v-col cols="6">
                <v-card-title class="justify-start text-lg-h5">
                  <b>Start Date</b>
                </v-card-title>
                <v-card-subtitle>{{form.start_date}}</v-card-subtitle>
              </v-col>
              <v-col cols="6">
                <v-card-title class="justify-start text-lg-h5">
                  <b>End Date</b>
                </v-card-title>
                <v-card-subtitle>{{form.end_date}}</v-card-subtitle>
              </v-col>
            </v-row>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Genre</b>
            </v-card-title>
            <v-card-subtitle>{{form.genre}}</v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start text-lg-h5">
              <b>Roles</b>
            </v-card-title>
            <v-row>
              <v-card-subtitle v-for="role in returnedFilmRoles" :key="role.id">
                <GridComponent>
                  <template #cardSlot>
                    <v-card class="ml-lg-n5 pr-lg-10 mr-lg-12" elevation="0">
                      <v-card-title>{{role.role_name}} | {{role.role_type}}</v-card-title>
                      <v-card-title>Character Name:{{role.character_name}}</v-card-title>
                      <v-card-title>Role Description:{{role.role_description}}</v-card-title>
                    </v-card>

                    <v-spacer></v-spacer>
                  </template>
                </GridComponent>
              </v-card-subtitle>
            </v-row>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start mb-lg-2 text-lg-h5">
              <b>Production</b>
            </v-card-title>
            <v-card-subtitle
              class="text-lg-subtitle-1 mb-lg-n8"
              v-for="production in form.crew_positions"
              :key="production"
            >
              <b>{{production}}</b>
            </v-card-subtitle>
          </v-card>
          <v-card
            class="mb-lg-10 ml-md-16 pl-md-10 ml-n4 ml-sm-16 pl-sm-3 ml-lg-16 pl-lg-16"
            elevation="0"
          >
            <v-card-title class="justify-start mb-lg-2 text-lg-h5">
              <b>Post Production</b>
            </v-card-title>
            <v-card-subtitle
              class="text-lg-subtitle-1 mb-lg-n8"
              v-for="postProduction in form.post_production_positions"
              :key="postProduction"
            >
              <b>{{postProduction}}</b>
            </v-card-subtitle>
          </v-card>
        </v-col>
        <v-spacer></v-spacer>

        <v-col sm="12">
          <v-row class="justify-end">
            <v-col class="pl-lg-16 justify-center" cols="7" sm="5">
              <v-btn
                class="ml-n2 ml-sm-16"
                @click="fourthPage = !fourthPage"
                style="margin-top: 50px;"
              >Back</v-btn>
            </v-col>
            <v-col cols="4">
              <v-btn
                v-if="!showPayButton"
                class="brown white--text ml-n2 ml-sm-n16"
                style="margin-top: 50px;"
                @click="submitForm"
              >Post</v-btn>
              <v-btn
                v-else
                class="brown white--text ml-n2 ml-sm-n16"
                style="margin-top: 50px;"
                @click="setPrice(`price_1J4RHBIXVRhKifjK2imEv2pg`)"
              >Pay</v-btn>
            </v-col>

            <v-col cols="4" md="4" sm="4"></v-col>
          </v-row>
          <v-spacer></v-spacer>
        </v-col>
      </v-row>
      <v-row class="align-center" v-if="displayFifth">
        <v-spacer></v-spacer>
        <v-col lg="6" cols="12">
          <!-- {{returnedForm.crew_positions}} -->
          <v-card class="mt-n10" outlined elevation="0">
            <v-btn text block class="ma-2" height="500px">
              <v-icon x-large dark right>mdi-checkbox-marked-circle</v-icon>
              <v-card-title>Listing Successfully Submitted</v-card-title>

              <v-card-actions></v-card-actions>
            </v-btn>
            <v-row>
              <v-spacer></v-spacer>
              <v-col cols="6">
                <v-btn text @click="submitForm();finishListing()">View Your Submitted Listings</v-btn>
              </v-col>
              <v-col cols="4">
                <v-btn text @click="submitForm();submitAnotherListing()">Submit Another Listing</v-btn>
              </v-col>
              <v-spacer></v-spacer>
            </v-row>
          </v-card>
        </v-col>
        <v-spacer></v-spacer>
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
import GalleryThumbnailComponent from "~/components/GalleryThumbnailComponent";

export default {
  head() {
    return {
      //   title: "Create Your User Profile"
    };
  },
  mounted() {
    this.generatePublicID(32, "0123456789");
  },
  components: {
    SubscribeComponent,
    TopNavbar,
    FooterComponent,
    GridComponent,
    SideBarComponent,
    GalleryThumbnailComponent
  },
  computed: {
    ...mapGetters(["loggedInUser"]),
    clientReference() {
      let clientID = this.$store.getters.loggedInUser.id;
      return clientID.toString();
    },
    showPayButton() {
      if (this.sortedActorsOldestFirst[0].paid_listing == "false") {
        return true;
      } else {
        return false;
      }
    },
    sortedActorsOldestFirst() {
      return this.actors
        .map(sortedActor => sortedActor)
        .sort((a, b) => a.id - b.id);
    },
    displayFifth() {
      if (this.sortedActorsOldestFirst[0].return_to_page == "True") {
        return true;
        console.log("true fifth");
      } else {
        return false;
      }
    },
    memberListings() {
      return {
        title: this.form.title,
        start_date: this.form.start_date,
        genre: this.form.genre,
        poster: this.form.poster
      };
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
    },
    mobile() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return true;
        case "sm":
          return true;
        case "xs":
          return true;
        case "lg":
          return false;
      }
    },
    buttonWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "20vw";
        case "sm":
          return "20vw";
        case "xs":
          return "90vw";
        case "lg":
          return "15vw";
      }
    },

    galleryPreviewWidth() {
      switch (this.$vuetify.breakpoint.name) {
        case "md":
          return "450px";
        case "sm":
          return "345px";
        case "xs":
          return "90vw";
        case "lg":
          return "550px";
      }
    }
  },
  async asyncData({ $axios, store, params, loggedInUser }) {
    const body = store.getters.loggedInUser.id;
    try {
      let actors = await $axios.$get(`/api/v1/actors/`, {
        params: {
          user: body
        }
      });
      return { actors };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        return { hasPermission };
      }
      console.log(error);
    }
  },
  methods: {
    submitAnotherListing(store, loggedInUser) {
      let formData = new FormData();
      this.sortedActorsOldestFirst[0].return_to_page = false;
      this.sortedActorsOldestFirst[0].paid_listing = false;
      formData.append(
        "return_to_page",
        this.sortedActorsOldestFirst[0].return_to_page
      );
      formData.append(
        "paid_listing",
        this.sortedActorsOldestFirst[0].paid_listing
      );
      this.$axios
        .patch(
          `/api/v1/actors/${this.sortedActorsOldestFirst[0].id}/`,
          formData
        )
        .then(response => {
          console.log("Successfully Reset success submit");
          this.$router.push(`/createlisting`);
        })
        .catch(error => {
          if (error) {
            this.showSubmitError = true;
          }
        });
    },
    checkout() {
      this.$refs.checkoutRef.redirectToCheckout();
      console.log(this.lineItems[0].price, "priceID");
      //change the button v-if back here
      //include a go see listings button, or a "ex" out to submit another listing
    },
    setDatatoLocalStorage() {
      localStorage.setItem("form", JSON.stringify(this.form));
      console.log("adding to localstorage");
      localStorage.setItem("fifth", "true");
    },
    setPrice(priceID) {
      this.lineItems[0].price = priceID;
      this.setDatatoLocalStorage();

      this.checkout();
    },
    inputFileClick() {
      this.$refs.poster.click();
    },
    createPoster() {
      //Used if the poster is uploaded using Form File input
      this.poster = this.$refs.poster.files;
      console.log(this.poster[0]);
      this.hasPoster = true;
      this.posterUploaded = true;
      this.galleryPhotoSelected = false;
      this.selectedGalleryPhoto = null;

      this.displayPosterName = this.poster[0].name;
    },
    generatePosterFromComponent(thumbID) {
      //Used if the poster is chosen from the thumbnail galllery component

      //   this.$refs.testImage.src = thumbID;
      this.dialog = false;
      this.galleryPhotoSelected = true;
      this.hideUploadName = true;
      console.log(thumbID, "thumbID");
      this.selectedGalleryPhoto = thumbID;
      console.log(this.selectedGalleryPhoto, "selectedGallery");
      this.hasPoster = false;
      this.displayPosterName = null;

      this.closeGallery();
    },
    filmRoleGalleryPhoto(thumbnailID) {
      this.dialog = false;
      this.galleryPhotoSelected = true;

      this.filmRoles.role_thumbnail = thumbnailID;
      console.log(this.filmRoles.role_thumbnail);
    },
    // onClickFromChild(thumbID) {
    //   //Used when selecting a thumbnail for a role
    //   console.log(thumbID, "thumbID");
    //   this.filmRoles.role_thumbnail = thumbID;
    // },

    closeGallery() {
      //Close Thumbnail gallery
      this.galleryNotOpen = true;
    },
    finishListing() {
      //After submitting basic information and the roles

      let formData = new FormData();
      this.sortedActorsOldestFirst[0].return_to_page = false;
      this.sortedActorsOldestFirst[0].paid_listing = false;
      formData.append(
        "return_to_page",
        this.sortedActorsOldestFirst[0].return_to_page
      );
      formData.append(
        "paid_listing",
        this.sortedActorsOldestFirst[0].paid_listing
      );
      this.$axios
        .patch(
          `/api/v1/actors/${this.sortedActorsOldestFirst[0].id}/`,
          formData
        )
        .then(response => {
          console.log("Successfully Reset success submit");
          this.$router.push(`/applications`);
        })
        .catch(error => {
          if (error) {
            this.showSubmitError = true;
          }
        });
    },

    submitForm() {
      // Submit the information on page 1 and 2 of the creation form
      this.form.date_submitted = this.currentDateTime; //currentDateTime is a computed Function
      let formAnswers = this.form;
      const config = {
        headers: {
          "content-type": "multipart/form-data; "
        }
      };
      let formData = new FormData();
      for (let data in formAnswers) {
        formData.append(data, formAnswers[data]);
      }
      if (this.hasPoster == true) {
        // if poster came from form upload input
        for (var i = 0; i < this.poster.length; i++) {
          console.log("first checkpoint");
          // let posterData = new FormData()
          let poster = this.poster[i];
          this.forMembers(poster);
          formData.append("poster", poster);
        }
        this.$axios
          .post(
            `/api/v1/listings/`,
            formData,
            config,
            this.positionsForm,
            this.form.random_public_id
          )
          .then(response => {
            console.log("Successfully Created New Listing");
            this.$router.push("/applications");
          })
          .catch(error => {
            if (error) {
              this.showSubmitError = true;
            }
          });
      } else {
        // if poster came from the gallery component
        let img = this.selectedGalleryPhoto;
        console.log(img, "img");
        this.$axios
          .get(img, {
            responseType: "blob"
          })
          .then(response => {
            console.log(response.data);
            this.forMembers(response.data);
            formData.append("poster", response.data);
            this.$axios
              .post(
                `/api/v1/listings/`,
                formData,
                config,
                this.positionsForm,
                this.form.random_public_id
              )
              .then(response => {
                console.log("Successfully Created New Listing");
                this.finishListing();
              })
              .catch(error => {
                if (error) {
                  this.showSubmitError = true;
                }
              });
          });
      }
    },

    generatePublicID(length, chars) {
      // create the ID displayed in the URL for this listing
      var result = "";
      for (var i = length; i > 0; --i) {
        result += chars[Math.round(Math.random() * (chars.length - 1))];
      }
      // return result;
      this.form.random_public_id = result;
      this.filmRoles.listing_public_id = result;
      console.log(this.form.random_public_id);
      console.log(this.filmRoles.listing_public_id);
    },
    forMembers(sentImage) {
      //just grab all the fields from this.form, the extra data will just go into the void >:)
      let editedForm = this.form;
      const config = {
        headers: {
          "content-type": "multipart/form-data; "
        }
      };
      let formData = new FormData();
      for (let data in editedForm) {
        formData.append(data, editedForm[data]);
      }
      formData.append("random_public_id", this.form.random_public_id);
      formData.append("poster", sentImage);
      this.$axios
        .post(`/api/v1/memberlistings/`, formData)
        .then(response => {
          console.log("Successfully Created New Listing");
          //   this.$router.push(`/applications`);
        })
        .catch(error => {
          if (error) {
            this.showSubmitError = true;
          }
        });
    },
    displayReturnedRoles() {
      // Return all previous roles after each new role is submitted. Keeps a running list
      this.$axios
        .get(`/api/v1/filmroles/`, {
          params: {
            listing_public_id: this.form.random_public_id
          }
        })
        .then(response => {
          this.returnedFilmRoles = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    displayReturnedProductionRoles() {
      // Return all previous roles after each new role is submitted. Keeps a running list
      this.$axios
        .get(`/api/v1/productionroles/`, {
          params: {
            listing_public_id: this.form.random_public_id
          }
        })
        .then(response => {
          this.returnedProductionRoles = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    displayReturnedPostProductionRoles() {
      // Return all previous roles after each new role is submitted. Keeps a running list
      this.$axios
        .get(`/api/v1/postproductionroles/`, {
          params: {
            listing_public_id: this.form.random_public_id
          }
        })
        .then(response => {
          this.returnedPostProductionRoles = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteRole(roleID, $axios) {
      // Allows for deletion of a role from the returned list of all roles
      let deletionID = roleID;
      this.$axios.delete(`/api/v1/filmroles/${deletionID}/`);
      //called twice so that the delte button deletes, and refreshes the page instead of needing 2 clicks
      this.displayReturnedRoles();
      this.displayReturnedRoles();
    },
    deleteProductionRole(roleID, $axios) {
      // Allows for deletion of a role from the returned list of all roles
      let deletionID = roleID;
      this.$axios.delete(`/api/v1/productionroles/${deletionID}/`);
      //called twice so that the delte button deletes, and refreshes the page instead of needing 2 clicks
      this.displayReturnedProductionRoles();
      this.displayReturnedProductionRoles();
    },
    deletePostProductionRole(roleID, $axios) {
      // Allows for deletion of a role from the returned list of all roles
      let deletionID = roleID;
      this.$axios.delete(`/api/v1/postproductionroles/${deletionID}/`);
      //called twice so that the delte button deletes, and refreshes the page instead of needing 2 clicks
      this.displayReturnedPostProductionRoles();
      this.displayReturnedPostProductionRoles();
    },
    addRoles($axios) {
      //  listingThatWasJustAdded array holds all listings objects. The one that was submitted before the roles
      this.$axios
        .post(`/api/v1/filmroles/`, this.filmRoles)
        .then(response => {
          console.log("Successfully Submitted Role");
          this.displayReturnedRoles();
          this.filmRoles.role_name = null; // reset the fields for the role after each one is submitted
          this.filmRoles.ethnicity = null;
          this.filmRoles.role_type = null;
          this.filmRoles.character_name = null;
          this.filmRoles.role_description = null;
          this.filmRoles.role_thumbnail = null;
          this.filmRoles.listing_public_id = this.form.random_public_id;
          console.log(this.filmRoles.listing_public_id, "roles public id");
        })
        .catch(error => {
          console.log(error);
        });
    },
    addProduction(tag, $axios) {
      //  listingThatWasJustAdded array holds all listings objects. The one that was submitted before the roles
      this.productionRoles.tag = tag;
      this.productionRoles.listing_public_id = this.form.random_public_id;

      console.log(this.productionRoles.tag, "tag");
      this.$axios
        .post(`/api/v1/productionroles/`, this.productionRoles)
        .then(response => {
          console.log("Successfully Submitted Production Role");
          this.displayReturnedProductionRoles();
          this.productionRoles.role_name = null; // reset the fields for the role after each one is submitted
          this.productionRoles.tag = null;
          this.productionRole.listing_public_id = this.form.random_public_id;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addPostProduction($axios) {
      //  listingThatWasJustAdded array holds all listings objects. The one that was submitted before the roles
      this.$axios
        .post(`/api/v1/postproductionroles/`, this.postProductionRoles)
        .then(response => {
          console.log("Successfully Submitted Production Role");
          this.displayReturnedRoles();
          this.postProductionRoles.role_name = null; // reset the fields for the role after each one is submitted
          this.postProductionRoles.tag = null;
          this.postProductionRole.listing_public_id = this.form.random_public_id;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  data() {
    return {
      loading: false,
      group: null,
      publishableKey: `${process.env.STRIPE_PK}`,
      lineItems: [
        {
          price: "",
          quantity: 1
        }
      ],
      payment_status: "unpaid",
      successUrl: "http://localhost:3000/createlisting",
      cancelUrl: "http://localhost:3000",
      timeCommit: ["Fulltime", "Part time"],
      payStatus: ["Paid", "Unpaid"],
      secondPage: false,
      thirdPage: false,
      fourthPage: false,
      hideUploadName: false,
      galleryPhotoSelected: false,
      dialog: false,
      professions: [
        "",
        "Directors",
        "Actors",
        "Dancers",
        "Writers",
        "Photographer",
        "Post Production",
        "Makeup Artist",
        "Production"
      ],
      states: [
        "",
        "Alabama",
        "Alaska",
        "American Samoa",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "District of Columbia",
        "Florida",
        "Georgia",
        "Guam",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Minor Outlying Islands",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Northern Mariana Islands",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Puerto Rico",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "U.S. Virgin Islands",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming"
      ],
      ethnicities: [
        "",
        "Hispanic/Latino",
        "Native Hawaiian/Pacific Islander",
        "Asian",
        "Black/African American",
        "Native American/Alaskan Native",
        "Middle Eastern"
      ],
      art: "art",
      camera: "camera",
      lighting: "lighting",
      sound: "sound",
      hasPoster: false,
      selectedGalleryPhoto: null,
      hasPermission: true,
      galleryNotOpen: true,
      showSubmitError: false,
      actors: [],
      posterUploaded: false,
      displayPosterName: null,
      returnedProductionRoles: [],
      returnedPostProductionRoles: [],
      form: {
        title: null,
        start_date: null,
        end_date: null,
        location: null,
        overview: null,
        studio: null,
        // poster: null,
        genre: null,
        status: null,
        job_type: null,
        user: this.$store.getters.loggedInUser.id,
        // post_production_positions: [],
        // crew_positions: [],
        director_email: null,
        random_public_id: null,
        date_submitted: null
      },
      filmRoles: {
        role_name: null,
        role_type: null,
        character_name: null,
        ethnicity: null,
        listing: null,
        role_description: null,
        listing_public_id: null,
        role_thumbnail: null
      },
      productionRoles: {
        role_name: null,
        tag: null,
        listing_public_id: null
      },
      postProductionRoles: {
        role_name: null,
        tag: null,
        listing_public_id: null
      },
      returnedFilmRoles: [],
      listingSubmitted: false,
      listingThatWasJustAdded: [],
      basicInfoSectionComplete: false
    };
  }
};
</script>