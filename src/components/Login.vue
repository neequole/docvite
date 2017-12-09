<template>
    <v-container text-xs-center id="login">
        <v-layout column wrap>
            <v-flex xs10>
                <v-card>
                    <form @submit.prevent="submit()">
                        <h2>Welcome back to Docvite!</h2>
                        <input type="text" placeholder="Username" v-model="username" required />
                        <input type="password" placeholder="Password" v-model="password" required />
                        <button type="submit">Login</button>
                        <div>{{ error }}</div>
                    </form>
                </v-card>
            </v-flex>
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
                var url = this.$DOCTOR_API_URL + 'login/'
                var requestData = {username: this.username, password: this.password}
                this.$http.post(url, requestData).then(response => {
                    localStorage.setItem('user', response.data)
                    this.$router.push('/')
                }, response => {
                    this.error = response.data.detail
                })
            }
        }
    }
</script>
<style scoped>
    #login {
        height: 100%;
        width: 100%;
        margin: 0;
    }
</style>