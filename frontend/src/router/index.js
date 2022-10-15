import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'create_request',

    component: () => import('@/pages/CreateRequest')
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

export default router
