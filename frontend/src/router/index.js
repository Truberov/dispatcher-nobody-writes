import Vue from 'vue'
import VueRouter from 'vue-router'
import store from "@/store";
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'create_request',

    component: () => import('@/components/LoginEnter')
  },
  {
    path: '/view_transport',
    name: 'view_transport',

    component: () => import('@/pages/ViewTransport')
  }
  // {
  //   path: '/view_request',
  //   name: 'view_request'
  //
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})
export default router
