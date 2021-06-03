import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _30e05924 = () => interopDefault(import('../pages/listings/index.vue' /* webpackChunkName: "pages/listings/index" */))
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
    path: "/listings",
    component: _30e05924,
    name: "listings"
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
