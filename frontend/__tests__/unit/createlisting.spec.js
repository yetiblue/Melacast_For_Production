jest.mock("axios", () => ({
  get: jest.fn(() => Promise.resolve({ data: 3 }))
}));

import { shallowMount, config, createLocalVue } from "@vue/test-utils";
import CreateListing from "@/pages/createlisting.vue";
import GalleryThumbnailComponent from "@/components/GalleryThumbnailComponent";
import MyApps from "@/pages/myapps.vue";
import axios from "axios";
import Vuetify from "vuetify";
import Vue from "vue";

config.silent = true;
Vue.config.silent = true;

describe("CreateProfile.vue axios mock test", () => {
  const localVue = createLocalVue();
  let methods = { generatePublicID: jest.fn() };
  let vuetify;

  // wrapper = mount(CreateListing);
  beforeEach(() => {
    vuetify = new Vuetify();
    jest.resetModules();
    jest.clearAllMocks();
  });

  it("make mount work", async () => {
    const wrapper = shallowMount(CreateListing, {
      vuetify,
      methods,

      // computed: {
      //   loggedInUser: () => {
      //     id: "1";
      //   }
      // },
      mocks: {
        $vuetify: { breakpoint: {} },
        $store: {
          getters: {
            loggedInUser: { id: "1" }
          }
        }
      }

      // stubs: {
      //   SideBarComponent: true,
      //   FooterComponent: true
      // }
    });
    await wrapper.setData({
      actors: [
        {
          return_to_page: true
        }
      ]
    });
    console.log(wrapper.html());
  });
});
