import { mount, createLocalVue } from "@vue/test-utils";
import Vuetify from "vuetify";
import CreateProfile from "@/pages/createprofile.vue";

describe("CreateProfile.vue", () => {
  const localVue = createLocalVue();
  let vuetify;

  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("Show card when true", async () => {
    const wrapper = mount(CreateProfile, {
      localVue,
      vuetify,
      data() {
        return { showCard: "my-override" };
      }
    });
    const overRide = wrapper.find("#testOverride");
    expect(overRide.text()).toBe("my-override");
    // await wrapper.setData({ showCard: true });
    // const byID = wrapper.find({ ref: "testCard" });
    // // expect(byID.element.id).toBe("testCard");
    // expect(byID.text()).toBe("Test text here");
  });
  it("Show Card when false", async () => {
    const wrapper = mount(CreateProfile, {
      localVue,
      vuetify
    });
    await wrapper.setData({ showCard: false });
    const byID = wrapper.find({ ref: "testCard2" });

    expect(byID.text()).toBe("The opposite");
  });
});
