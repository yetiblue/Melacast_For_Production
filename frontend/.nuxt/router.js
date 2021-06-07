import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _59465c5d = () => interopDefault(import('../pages/actors/index.vue' /* webpackChunkName: "pages/actors/index" */))
const _30e05924 = () => interopDefault(import('../pages/listings/index.vue' /* webpackChunkName: "pages/listings/index" */))
const _7b15e85d = () => interopDefault(import('../pages/login.vue' /* webpackChunkName: "pages/login" */))
const _07af5f38 = () => interopDefault(import('../pages/registration/index.vue' /* webpackChunkName: "pages/registration/index" */))
const _02e1ba2e = () => interopDefault(import('../pages/registration/awaiting_confirmation.vue' /* webpackChunkName: "pages/registration/awaiting_confirmation" */))
const _555b6708 = () => interopDefault(import('../pages/registration/activate/_token.vue' /* webpackChunkName: "pages/registration/activate/_token" */))
const _36ef8426 = () => interopDefault(import('../pages/registration/activate/_uid/_token.vue' /* webpackChunkName: "pages/registration/activate/_uid/_token" */))
const _5a9ffe70 = () => interopDefault(import('../pages/actors/_id/index.vue' /* webpackChunkName: "pages/actors/_id/index" */))
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
    path: "/actors",
    component: _59465c5d,
    name: "actors"
  }, {
    path: "/listings",
    component: _30e05924,
    name: "listings"
  }, {
    path: "/login",
    component: _7b15e85d,
    name: "login"
  }, {
    path: "/registration",
    component: _07af5f38,
    name: "registration"
  }, {
    path: "/registration/awaiting_confirmation",
    component: _02e1ba2e,
    name: "registration-awaiting_confirmation"
  }, {
    path: "/registration/activate/:token?",
    component: _555b6708,
    name: "registration-activate-token"
  }, {
    path: "/registration/activate/:uid?/:token?",
    component: _36ef8426,
    name: "registration-activate-uid-token"
  }, {
    path: "/actors/:id",
    component: _5a9ffe70,
    name: "actors-id"
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
