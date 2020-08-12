import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
  path: "/diamond",
  name: "Diamond",
  component: () => import("../components/diamond.vue"),
  children: [
    {
      path: "dashboard/team/:teamId",
      name: "TeamInfo",
      component: () => import("../views/dashboard/teamInfo.vue")
    },
    {
      path: "profile",
      name: "Profile",
      component: () =>
          import(/* webpackChunkName: "about" */ "../components/profile.vue"),
      children: [
        {
          path: "changeusername",
          name: "ChangeUsername",
          component: () =>
              import(/* webpackChunkName: "about" */ "../views/profile/changeUsername.vue")
        },
        {
          path: "changepassword",
          name: "ChangePassword",
          component: () =>
              import(/* webpackChunkName: "about" */ "../views/profile/changePassword.vue")
        },
        {
          path: "changeicon",
          name: "ChangeIcon",
          component: () =>
              import(/* webpackChunkName: "about" */ "../views/profile/changeIcon.vue")
        },
      ]
    },
    {
      path:"templates/:teamId",
      name: "Templates",
      component: () => import("../views/templates.vue")
    },
    {
      path:"createTeam",
      name: "CreateTeam",
      component: () => import("../views/createTeam.vue")
    },
    {
      path: "dashboard",
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
  ]
},
  {
    path:"/login",
    name: "Login",
    component: () => import("../components/Login.vue")
  },
  {
    path:"/register",
    name: "Register",
    component: () => import("../components/Register.vue")
  },
  {
    path:"/editor",
    name: "editor",
    component: () => import("../components/editor.vue")
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
