<template>
  <v-toolbar elevation="0" dark>
    <v-toolbar-title>MELACAST</v-toolbar-title>
    <v-spacer></v-spacer>

    <div v-if="mobile">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer">
        <v-navigation-drawer>HELLO</v-navigation-drawer>
      </v-app-bar-nav-icon>
    </div>
    <div v-else>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn v-for="item in menu" :key="item.icon" :to="item.link" flat>
          {{
          item.title
          }}
        </v-btn>
      </v-toolbar-items>
    </div>
  </v-toolbar>
</template>
<script>
export default {
  data() {
    return {
      drawer: false,
      group: null,
      menu: [
        { icon: "home", title: "Link A" },
        { icon: "info", title: "Link B" },
        { icon: "warning", title: "Link C" }
      ]
    };
  },
  computed: {
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
        case "xl":
          return false;
      }
    }
  },
  watch: {
    group() {
      this.drawer = false;
    }
  },
  methods: {
    menuItems() {
      return this.menu;
    }
  }
};
</script>
