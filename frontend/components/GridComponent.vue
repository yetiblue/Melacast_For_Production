<template>
  <v-row class="pb-lg-16 mb-lg-n16" justify="end" align="start">
    <v-col cols="8" sm="10" lg="9" class="pl-8 pl-sm-6 pl-md-12 pl-lg-10">
      <slot name="rowTitleOne"></slot>
      <slot name="rowTitleTwo"></slot>
      <slot name="rowTitleThree"></slot>
    </v-col>
    <v-col class="mb-n16 pr-16 pr-lg-0 mr-n4 mr-lg-4 mr-sm-4 mr-md-n4" cols="4" sm="2" lg="1">
      <slot name="navButtonOne"></slot>
      <slot name="navButtonTwo"></slot>
      <slot name="navButtonThree"></slot>
    </v-col>
    <v-col class="pb-16" cols="12" sm="12" md="12" :lg="gridWidth" justify="end">
      <v-row class="mt-2 mb-lg-n16 pl-4 pr-4 px-sm-10 pl-lg-8 pr-lg-8" justify="start">
        <slot name="cardSlot"></slot>
      </v-row>
    </v-col>
  </v-row>
</template>
<script>
export default {
  props: ["displayGridCount", "gridWidth"],
  computed: {},
  methods: {
    navigateToPage() {
      console.log("click");
      this.$router.push(`/listings/${sortedListing.id}/`);
    }
  }
};
</script>
<style>
</style>
