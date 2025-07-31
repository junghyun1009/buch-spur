import BookList from '../components/BookList.vue'
import SignupForm from '../components/user/SignupForm.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    { path: '/', component: BookList },
    { path: '/signup', component: SignupForm }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router