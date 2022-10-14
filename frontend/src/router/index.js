import { createRouter, createWebHistory } from 'vue-router'
import CreateRequest from "@/views/CreateRequest";

const routes = [
  {
    path: '/',
    name: 'home',
    component: CreateRequest
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
