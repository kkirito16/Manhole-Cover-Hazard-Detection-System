import Vue from "vue"
import VueRouter from "vue-router"
import Layout from "../layout"

Vue.use(VueRouter)

const routes = [
  { name: "login", path: "/login", meta: { title: "登录-井盖隐患检测系统" }, component: () => import("../views/login/index"), hidden: true },
  { name: "/", path: "/", component: Layout, redirect: "/index", hidden: false, children: [
      { name: "index", path: "/index", meta: { title: "主页-井盖隐患检测系统" }, component: () => import("../views/index/index") },
  ]}
]

const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
 return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({ routes })

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || '井盖隐患检测系统'; // 如果路由中设置了标题，则使用设置的标题，否则使用默认标题
  next();
});

export default router