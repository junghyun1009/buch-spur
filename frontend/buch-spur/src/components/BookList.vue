<template>
    <div>
        <h1>책 목록</h1>
        <ul>
            <li v-for="book in books" :key="book.id">
                {{ book.title }} : {{ book.author }}
            </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'BookList',
    data() {
        return {
            books: []
        }
    },
    mounted() {
        axios.get('http://localhost:8000/')
        .then(response => {
            console.log(response)
            this.books = response.data
        })
        .catch(error => {
            console.error('API 호출 실패 : ', error)
        })
    }
}
</script>