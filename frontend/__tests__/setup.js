import Vue from "vue";
import Vuetify from "vuetify";

Vue.use(Vuetify);
Vue.config.productionTip = false;
config.stubs.nuxt = { template: "<div />" };
config.stubs["nuxt-link"] = { template: "<a><slot /></a>" };
config.stubs["no-ssr"] = { template: "<span><slot /></span>" };
