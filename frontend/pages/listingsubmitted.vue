<template>
  <v-app>
    <v-row>
      <v-spacer></v-spacer>
      <v-col cols="6">
        <!-- {{returnedForm.crew_positions}} -->
        <v-card elevation="0">
          <v-btn block class="ma-2" height="500px">
            <v-icon x-large dark right>mdi-checkbox-marked-circle</v-icon>
            <v-card-title>Listing Successfully Submitted</v-card-title>
          </v-btn>
        </v-card>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
  </v-app>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  components: {},
  computed: {
    ...mapGetters(["loggedInUser"]),
    clientReference() {
      let clientID = this.$store.getters.loggedInUser.id;
      return clientID.toString();
    }
  },
  data() {
    return {
      crew_positions: null,
      listing_paid: false,
      returnedForm: null,
      returnedPositionsForm: null,
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
      successUrl: "http://localhost:3000/stripe",
      cancelUrl: "http://localhost:3000"
      // clientReferenceId:
    };
  },
  mounted() {
    console.log(this.payment_status, "payment status");
    this.getLocalStorage();
  },
  methods: {
    getLocalStorage() {
      let formData = new FormData();
      formData.append("listing_paid", this.listing_paid);
      this.returnedForm = JSON.parse(localStorage.getItem("form"));
      this.crew_positions = this.returnedForm.crew_positions.join();

      console.log(this.crew_positions, "crew pos");
      delete this.returnedForm.crew_positions;

      // formData.append("crew_positions", returnedCrew);
      this.$axios
        .post(`/api/v1/listings/`, this.returnedForm)
        .then(response => {
          this.$axios
            .patch(`/api/v1/listings/`, formData)
            .then(response => {
              console.log("Successfully reset paid listng");
            })
            .catch(error => {
              if (error) {
                console.log(error);
              }
            });
        })
        .catch(error => {
          if (error) {
            console.log(error);
          }
        });
      // this.postListing();

      // console.log(formStorage, "formStorage");
    },
    postListing() {
      this.$axios
        .post(`/api/v1/listings/`, this.returnedForm, formData)
        .then(response => {
          this.$axios
            .patch(`/api/v1/listings/`, formData)
            .then(response => {
              console.log("Successfully reset paid listng");
            })
            .catch(error => {
              if (error) {
                console.log(error);
              }
            });
        })
        .catch(error => {
          if (error) {
            console.log(error);
          }
        });
    },
    checkout() {
      this.$refs.checkoutRef.redirectToCheckout();
      console.log(this.lineItems[0].price, "priceID");
    },
    setPrice(priceID) {
      this.lineItems[0].price = priceID;
    }
  }
};
</script>