import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

//correct export syntax for NUXT only
//nuxt handles a lot of the syntax of vanilla vue by default

// const store = new Vuex.Store({
//   state: {
//     count: 0
//   },
//   mutations: {
//     increment(state) {
//       state.count++
//     }
//   }
// })

// ^ vanilla vuex syntax
export const state = () => ({
  tiers: [
    {
      id: 1,
      name: "Director II",
      price: 5,
      desc: `Profile on our website \n
         Access to actors reels headshots \n
         Can post projects and cast actors/hire crew \n
         Invite to private in-person pitch sessions and mixers from database`
    },
    {
      id: 2,
      name: "Director III -Gold",
      price: 15,
      desc: null
    },
    {
      id: 3,
      name: "Actor II",
      price: 5,
      desc: null
    },
    {
      id: 4,
      name: "Actor III",
      price: 10,
      desc: null
    },
    {
      id: 5,
      name: "Crew II",
      price: 5,
      desc: null
    },
    {
      id: 6,
      name: "Photographer II",
      price: 5,
      desc: null
    }
  ],
  StoreCart: [],
  ItemName: []
});
export const mutations = {
  ADD_Item(state, id, price) {
    state.StoreCart.push(id);
  },
  REMOVE_Item(state, index) {
    state.StoreCart.splice(index, 1);
  },
  ADD_Name(state, id) {
    state.ItemName.push(id);
  },
  REMOVE_Name(state, index) {
    state.ItemName.splice(index, 1);
  }
};
export const actions = {
  //all actions require two parameters from the frontend, what exactly is index?
  // I'm putting price and name as placeholders, do they do anything?
  addItem(context, id, price) {
    context.commit("ADD_Item", id);
  },
  removeItem(context, index) {
    context.commit("REMOVE_Item", index);
  },
  addName(context, index) {
    context.commit("ADD_Name", index);
  },
  removeName(context, index) {
    context.commit("REMOVE_Name", index);
  }
};
export const getters = {
  isAuthenticated(state) {
    return state.auth.loggedIn;
  },
  loggedInUser(state) {
    return state.auth.user;
  },
  tiers: state => state.tiers,
  StoreCart: state => state.StoreCart,
  ItemName: state => state.ItemName
};
