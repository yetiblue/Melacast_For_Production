import { mount, createLocalVue } from "@vue/test-utils";
import Vuetify from "vuetify";
import CreateProfile from "@/pages/createprofile.vue";

// beforeEach(() => {
//   localVue = createLocalVue(); // because of vuetify, we should use a localVue instance
//   let vuetify = new Vuetify();
//   let wrapper = mount(CreateProfile, {
//     localVue,
//     vuetify,
//     attachToDocument: true
//   });
// });
describe("CreateProfile.vue", () => {
  it("Show card when true", async () => {
    const wrapper = mount(CreateProfile);
    await wrapper.setData({ showCard: true });
    const byID = wrapper.find({ ref: "testCard" });
    // expect(byID.element.id).toBe("testCard");
    expect(byID.text()).toBe("Test text here");
  });
  it("Show Card when false", async () => {
    const wrapper = mount(CreateProfile);
    await wrapper.setData({ showCard: false });
    const byID = wrapper.find({ ref: "testCard2" });

    expect(byID.text()).toBe("The opposite");
  });
});
