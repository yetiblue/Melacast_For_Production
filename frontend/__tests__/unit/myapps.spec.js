import { mount, config, shallowMount, createLocalVue } from "@vue/test-utils";
import MyApps from "@/pages/myapps.vue";
import Vuetify from "vuetify";
import Vue from "vue";

config.silent = true;
Vue.config.silent = true;

describe("Testing Myapps", () => {
  let vuetify;

  beforeEach(() => {
    vuetify = new Vuetify();
  });
  it("myapps.vue", async () => {
    const wrapper = mount(MyApps, {
      //   localVue,
      vuetify,
      mocks: {
        $vuetify: { breakpoint: {} }
      },
      stubs: {
        SideBarComponent: true,
        FooterComponent: true
      },
      data() {
        return {
          actor: [
            {
              firstname: "bob",
              lastname: "bob",
              group: "actors"
            }
          ]
        };
      }
    });
    // await wrapper.setData({
    //   actor: [
    //     {
    //       firstname: "bob",
    //       lastname: "bob",
    //       group: "actors"
    //     }
    //   ]
    // });

    console.log(wrapper.html()); //  TypeError: Cannot read property 'firstname' of undefined
    console.log(wrapper.vm.actor[0].firstname); // "bob"});

    // const byID = wrapper.find("#testCard");
    // expect(byID.text()).toBe("The opposite");

    //   });
  });
});
