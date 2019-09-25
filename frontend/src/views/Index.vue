<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div class="md-layout-item">
            <h1 class="title">LDA画像検索
            </h1>
            <br>
            <md-button v-bind:to="{ name : 'search'}" class="md-success md-lg">
              <i class="fas fa-search"></i>試してみる
            </md-button>
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section" id="about">
        <div class="container">
          <div class="md-layout">
            <div class="md-layout-item md-size-66 md-xsmall-size-100 mx-auto text-center">
              <h2 class="title text-center">About</h2>

              <div class="alert alert-info">
                <div class="container">
                  本システムはプロトタイプ（試作品）であり、データ等が予告なく変更される可能性があります。この点を了解の上でご利用ください。
                </div>
              </div>

              
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  bodyClass: "landing-page",
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg7.jpg")
    }
  },
  data() {
    return {
      items: []
    };
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  }
};
</script>
<style lang="scss" scoped>
h1, h2 {
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
}
.page-header {
    height: 70vh;
}
</style>