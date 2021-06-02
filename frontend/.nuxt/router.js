import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _07ce192b = () => interopDefault(import('../pages/listings.vue' /* webpackChunkName: "pages/listings" */))
const _1f75c686 = () => interopDefault(import('../pages/listings.vue/index.vue' /* webpackChunkName: "pages/listings.vue/index" */))
const _7d47a31e = () => interopDefault(import('../pages/listings.vue/_id/index.vue' /* webpackChunkName: "pages/listings.vue/_id/index" */))

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
    path: "/listings",
    component: _07ce192b,
    name: "listings"
  }, {
    path: "/listings.vue",
    component: _1f75c686,
    name: "listings.vue"
  }, {
    path: "/listings.vue/:id",
    component: _7d47a31e,
    name: "listings.vue-id"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
