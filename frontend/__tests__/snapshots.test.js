import { createLocalVue, mount } from "@vue/test-utils";
import Listings from "~/pages/listings/index.vue";
import Vue from "vue";
import Vuetify from "vuetify";

Vue.use(Vuetify);
let vuetify;

beforeEach(() => {
  vuetify = new Vuetify();
});
test("renders correctly", () => {
  const wrapper = mount(Listings);
  expect(wrapper.element).toMatchSnapshot();
});

describe("CustomCard.vue", () => {
  const localVue = createLocalVue();
  let vuetify;

  beforeEach(() => {
    vuetify = new Vuetify();
  });

  it("should have a custom title and match snapshot", () => {
    // With jest we can create snapshot files of the HTML output
    expect(wrapper.html()).toMatchSnapshot();
  });
});
