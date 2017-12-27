<template>
    <v-container fill-height id="login">
        <v-layout align-center justify-center>
            <v-card>
                <form @submit.prevent="submit()">
                    <v-layout column wrap class="ma-2">
                        <h2>Welcome back to Docvite!</h2>
                        <input type="text" placeholder="Username" v-model="username" required />
                        <input type="password" placeholder="Password" v-model="password" required />
                        <button type="submit">Login</button>
                        <div>{{ error }}</div>
                    </v-layout>
                    </form>
                </v-card>
            </v-layout>
        </v-container>
</template>

<script>
    export default {
        data () {
            return {
                username: null,
                password: null,
                error: null,
            }
        },
        methods: {
            submit() {
                var requestData = {username: this.username, password: this.password}
                this.$http.post('doctors/login/', requestData).then(response => {
                    localStorage.setItem('user', JSON.stringify(response.data))
                    this.$router.push('/')
                }, response => {
                    this.error = response.data.detail
                })
            }
        }
    }
</script>
<style scoped>
</style>