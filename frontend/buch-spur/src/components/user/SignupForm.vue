<template>
    <div>
        <form @submit.prevent="handleSignup">
            <input v-model="username" placeholder="아이디">
            <input v-model="password" placeholder="비밀번호">
            <input v-model="email" placeholder="이메일">
            <input v-model="nickname" placeholder="닉네임">
            <button type="submit">회원가입</button>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const email = ref('')
const nickname = ref('')

const handleSignup = async () =>{
    try {
        const response = await axios.post('/signup/', {
            username: username.value,
            password: password.value,
            email: email.value,
            nickname: nickname.value
        })
        alert('회원가입이 완료되었습니다.')
    } catch (error) {
        alert('회원가입을 실패하였습니다.')
    }
}

</script>