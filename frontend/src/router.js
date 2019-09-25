import Vue from "vue";
import Router from "vue-router";
import Index from "./views/Index.vue";
import Search from "./views/Search.vue";
import Metadata from "./views/Metadata.vue";
import MainNavbar from "./layout/MainNavbar.vue";
import MainFooter from "./layout/MainFooter.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "index",
      components: { default: Index, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 100 },
        footer: { backgroundColor: "black" }
      }
    },
    {
      path: "/search",
      name: "search",
      components: { default: Search, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 10 },
        footer: { backgroundColor: "black" }
      }
    },
    {
      path: "/metadata",
      name: "metadata",
      components: { default: Metadata, header: MainNavbar, footer: MainFooter },
      props: {
        header: { colorOnScroll: 10 },
        footer: { backgroundColor: "black" }
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});
