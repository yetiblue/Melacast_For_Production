<template></template>
<script>
import { mapGetters } from "vuex";

export default {
  mounted() {
    this.redirectToProfile();
  },
  methods: {
    redirectToProfile() {
      this.$router.push(`/community/${this.actor[0].id}`);
    }
  },
  computed: {
    ...mapGetters(["loggedInUser"])
  },

  async asyncData({ params, $axios, store }) {
    try {
      const body = store.getters.loggedInUser.id;
      const actor = await $axios.$get(`/api/v1/actors/`, {
        params: {
          user: body
        }
      });

      return { actor };
    } catch (error) {
      if (error.response.status === 403) {
        const hasPermission = false;
        console.log(hasPermission, "perm");
        console.error(error);
        return { hasPermission };
      }
    }
  }
};
</script>