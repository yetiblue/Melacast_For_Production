const axios = require("axios");
const qs = require("qs");
module.exports = {
  /*
   ** Headers of the page
   */

  head: {
    title: "nuxt-auth",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "Nuxt.js project" }
    ],

    link: [
      { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
      {
        rel: "stylesheet",
        href:
          "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css"
      }
    ]
  },
  /*
   ** Customize the progress bar color
   */
  loading: { color: "#3B8070" },
  plugins: [{ src: "~/plugins/vue-stripe-checkout.js", ssr: false }],
  env: {
    STRIPE_PK: process.env.STRIPE_PK
  },

  buildModules: ["@nuxtjs/vuetify", "@nuxt/components"],
  modules: ["@nuxtjs/axios", "@nuxtjs/auth"],

  axios: {
    // proxy: true,
    baseURL:
      //   // process.env.NODE_ENV === 'production'
      //   //   ? process.env.BASE_URL
      "http://localhost:8000",
    headers: {
      "Content-Type": "application/json"
    }
  },

  auth: {
    redirect: {
      home: "/dashboard",
      login: "/login",
      logout: "/"
    },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: "/auth/token/login/",
            method: "post",
            propertyName: "auth_token"
          },
          logout: { url: "/auth/token/logout/", method: "post" },
          user: {
            url: "/auth/users/me/",
            method: "get",
            propertyName: false
          }
        },
        tokenType: "Token"
      }
    },

    build: {
      /*
       ** Run ESLint on save
       */

      standalone: true,
      extend(config, { isDev, isClient }) {
        if (isDev && isClient) {
          config.module.rules.push({
            enforce: "pre",
            test: /\.(js|vue)$/,
            loader: "eslint-loader",
            exclude: /(node_modules)/
          });
        }
      }
    },
    router: {
      middleware: ["auth"]
    }
  }
};
