<template>
  <div id="app">
    <BookList />
    <SignupFrom />
  </div>
</template>

<script>
import BookList from './components/BookList.vue'
import SignupForm from './components/user/SignupForm.vue'

export default {
  name: 'App',
  components: {
    BookList,
    SignupForm
  }
}
</script>