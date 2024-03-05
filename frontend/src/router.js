import { createWebHistory, createRouter } from "vue-router";
import Home from "./views/HomeView.vue";
import Login from "./views/LoginView.vue";
import Register from "./components/Register.vue";
import Ping from "./components/Ping.vue";

// lazy-loaded
const Profile = () => import("./views/Profile.vue")
//const BoardAdmin = () => import("./components/BoardAdmin.vue")
//const BoardModerator = () => import("./components/BoardModerator.vue")
const BoardUser = () => import("./components/dashBoardUser.vue")

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/ping",
    name: "ping",
    component: Ping,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  },
  {
    path: "/profile",
    name: "profile",
    // lazy-loaded
    component: Profile,
  },
  //{
  //  path: "/admin",
  //  name: "admin",
    // lazy-loaded
  //  component: BoardAdmin,
  //},
  //{
  //  path: "/mod",
  //  name: "moderator",
  //  // lazy-loaded
  //  component: BoardModerator,
  //},
  {
    path: "/user",
    name: "user",
    // lazy-loaded
    component: BoardUser,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

