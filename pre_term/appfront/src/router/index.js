import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () => import("../components/dashboard.vue"),
    children: [
      {
        path: "used",
        name: "Used",
        component: () => import("../views/dashboard/used.vue")
      },
      {
        path: "desktop",
        name: "Desktop",
        component: () => import("../views/dashboard/desktop.vue")
      },
      {
        path: "favorites",
        name: "Favorites",
        component: () => import("../views/dashboard/favorites.vue")
      },
      {
        path: "own",
        name: "Own",
        component: () => import("../views/dashboard/own.vue")
      },
      {
        path: "team",
        name: "Team",
        component: () => import("../views/dashboard/team.vue")
      },
      {
        path: "trash",
        name: "Trash",
        component: () => import("../views/dashboard/trash.vue")
      },
    ]
  },
  {
    path: "/edit",
    name: "Edit",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/edit.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
