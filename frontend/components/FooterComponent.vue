<template>
  <section>
    <footer>
      <div class="footer_style">
        <div class="left_box">
          <p style="font-size:24px;margin-bottom:12px;font-weight:500;">Hours of Operation</p>
          <div id="footer_content">
            <div style="font-size:14px;font-weight:bold;">9am - 6pm</div>
            <div style="font-size:14px">Monday - Friday</div>
          </div>
          <div id="footer_content_2">
            <div style="font-size:14px;font-weight:bold;">Closed</div>
            <div style="font-size:14px">Saturday - Sunday</div>
          </div>
          <div style="margin-top:25px">
            <v-btn id="social_media_2" large icon color="#efefef" href="https://www.facebook.com/">
              <v-icon large>mdi-facebook</v-icon>
            </v-btn>
            <v-btn id="social_media_2" large icon color="#efefef" href="https://www.instagram.com/">
              <v-icon large>mdi-instagram</v-icon>
            </v-btn>
            <p style="font-size:14px;">Copyright © Melecast 2020 | New York, NY</p>
          </div>
        </div>
        <div class="footer_nav">
          <div>
            <nuxt-link style="color:#efefef;" to="/listings">Community</nuxt-link>
          </div>
          <div>
            <nuxt-link style="color:#efefef;" to="/listings">Projects</nuxt-link>
          </div>
          <div>
            <nuxt-link style="color:#efefef;" to="/listings">About Us</nuxt-link>
          </div>
          <div>
            <nuxt-link style="color:#efefef;" to="/listings">Contacts</nuxt-link>
          </div>
        </div>
      </div>
    </footer>
  </section>
</template>


<style>
.footer_style {
  background-color: #231f20;
  width: 100%;
  height: 297px;
  bottom: 0px;
  padding-top: 50px;
  display: flex;
  flex-direction: row;
}
.left_box {
  width: 40%;
  margin-left: 138px;
  color: #efefef;
}
#footer_content {
  display: flex;
  flex-direction: row;
}
#footer_content > div {
  margin-right: 28px;
}
#footer_content_2 {
  display: flex;
  flex-direction: row;
}
#footer_content_2 > div {
  margin-right: 55px;
}
#social_media_2 {
  margin-top: 25px;
  margin-bottom: 15px;
  width: 28px;
  height: 28px;
  margin-right: 20px;
}
.footer_nav {
  width: 40%;
  margin-right: 138px;
  flex-direction: column;
  text-align: right;
}
.footer_nav > div {
  margin-bottom: 20px;
}
</style>