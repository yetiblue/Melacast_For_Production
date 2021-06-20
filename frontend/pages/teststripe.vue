<template>
  <div>
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

    <div id="checkout-button">
      <button @click="checkout">Continue to Checktout</button>
      <ul>
        <li>
          <button @click="setPrice(`price_1J4RHBIXVRhKifjK2imEv2pg`)">Buy Listing</button>
        </li>
        <li>
          <button @click="setPrice(`price_1ISoQEIXVRhKifjKjHG4tECz`)">Buy Crew (Lvl 1)</button>
        </li>
        <li>
          <button @click="setPrice(`price_1ISoPyIXVRhKifjKQvoPvubn`)">Buy Actor</button>
        </li>
        <li>
          <button @click="setPrice(`price_1IW07qIXVRhKifjKSZIL4I0K`)">Buy Writer</button>
        </li>
        <li>
          <button @click="setPrice(`price_1ISpHLIXVRhKifjKiraBYpEC`)">Buy Photographer</button>
        </li>
        <li>
          <button @click="setPrice(`price_1IW07qIXVRhKifjKSZIL4I0K`)">Buy Writer</button>
        </li>
      </ul>
    </div>
  </div>
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
  },
  methods: {
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