jest.mock("axios", () => ({
  get: jest.fn(() => Promise.resolve({ data: 3 }))
}));

import { mount, createLocalVue } from "@vue/test-utils";
import CreateListing from "@/pages/createlisting.vue";
import MyApps from "@/pages/myapps.vue";
import axios from "axios";
import Vuetify from "vuetify";

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

  it("Checks SideBarComponent is rendered", async () => {
    const wrapper = mount(CreateListing, {
      vuetify,
      methods,
      mocks: {
        $vuetify: { breakpoint: {} }
      }

      // stubs: {
      //   SideBarComponent: true,
      //   FooterComponent: true
      // }
    });
    await wrapper.setData({
      form: {
        random_public_id: "boo"
      }
    });
    expect(methods.generatePublicID).toHaveBeenCalled();
    console.log(wrapper.html());
  });
});
