import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _006e47a0 = () => interopDefault(import('../pages/community/index.vue' /* webpackChunkName: "pages/community/index" */))
const _1f2a3b7c = () => interopDefault(import('../pages/createlisting.vue' /* webpackChunkName: "pages/createlisting" */))
const _0696e88b = () => interopDefault(import('../pages/dashboard/index.vue' /* webpackChunkName: "pages/dashboard/index" */))
const _30e05924 = () => interopDefault(import('../pages/listings/index.vue' /* webpackChunkName: "pages/listings/index" */))
const _48c5449a = () => interopDefault(import('../pages/listingsubmitted.vue' /* webpackChunkName: "pages/listingsubmitted" */))
const _7b15e85d = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _9e92634c = () => interopDefault(import('../pages/myapps.vue' /* webpackChunkName: "pages/myapps" */))
const _5e28b860 = () => interopDefault(import('../pages/profile/index.vue' /* webpackChunkName: "pages/profile/index" */))
const _07af5f38 = () => interopDefault(import('../pages/registration/index.vue' /* webpackChunkName: "pages/registration/index" */))
const _00eadeec = () => interopDefault(import('../pages/profile/edit.vue' /* webpackChunkName: "pages/profile/edit" */))
const _02e1ba2e = () => interopDefault(import('../pages/registration/awaiting_confirmation.vue' /* webpackChunkName: "pages/registration/awaiting_confirmation" */))
const _36ef8426 = () => interopDefault(import('../pages/registration/activate/_uid/_token.vue' /* webpackChunkName: "pages/registration/activate/_uid/_token" */))
const _fccadaea = () => interopDefault(import('../pages/community/_id/index.vue' /* webpackChunkName: "pages/community/_id/index" */))
const _bb54f14e = () => interopDefault(import('../pages/listings/_id/index.vue' /* webpackChunkName: "pages/listings/_id/index" */))

// TODO: remove in Nuxt 3
const emptyFn = () => {}
const originalPush = Router.prototype.push
Router.prototype.push = function push (location, onComplete = emptyFn, onAbort) {
  return originalPush.call(this, location, onComplete, onAbort)
}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/community",
    component: _006e47a0,
    name: "community"
  }, {
    path: "/createlisting",
    component: _1f2a3b7c,
    name: "createlisting"
  }, {
    path: "/dashboard",
    component: _0696e88b,
    name: "dashboard"
  }, {
    path: "/listings",
    component: _30e05924,
    name: "listings"
  }, {
    path: "/listingsubmitted",
    component: _48c5449a,
    name: "listingsubmitted"
  }, {
    path: "/login",
    component: _7b15e85d,
    name: "login"
  }, {
    path: "/myapps",
    component: _9e92634c,
    name: "myapps"
  }, {
    path: "/profile",
    component: _5e28b860,
    name: "profile"
  }, {
    path: "/registration",
    component: _07af5f38,
    name: "registration"
  }, {
    path: "/profile/edit",
    component: _00eadeec,
    name: "profile-edit"
  }, {
    path: "/registration/awaiting_confirmation",
    component: _02e1ba2e,
    name: "registration-awaiting_confirmation"
  }, {
    path: "/registration/activate/:uid?/:token?",
    component: _36ef8426,
    name: "registration-activate-uid-token"
  }, {
    path: "/community/:id",
    component: _fccadaea,
    name: "community-id"
  }, {
    path: "/listings/:id",
    component: _bb54f14e,
    name: "listings-id"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
