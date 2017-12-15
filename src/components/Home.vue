<template>
  <v-container grid-list-xs id="home">
    <v-layout row>
      <v-flex xs3 style="background-color: yellow">
        <v-navigation-drawer permanent light id="navigation">
          <v-toolbar flat>
            <v-list>
              <v-list-tile>
                <v-list-tile-title class="title">
                  Welcome
                </v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-toolbar>
          <v-divider></v-divider>
          <v-list dense class="pt-0">
            <v-list-tile v-for="item in items" :key="item" @click="logout()">
              <v-list-tile-content>
                <v-list-tile-title>{{ item }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
      </v-flex>
      <v-flex style="background-color: aqua">
        {{ msg }}
      </v-flex>
    </v-layout>
    <!--<button @click="logout">Log out</button>-->
    <!--{{ msg }}-->
  </v-container>
</template>

<script>
    export default {
        data () {
            return {
                items: [
                    'Clients',
                    'Tests',
                    'Resources',
                    'Profile',
                    'Settings',
                    'Logout',
                ],
                msg: 'Welcome to Your Vue.js App',
            }
        },
        methods: {
            logout() {
                var url = this.$DOCTOR_API_URL + 'logout/'
                this.$http.post(url).then(response => {
                    localStorage.removeItem('user')
                    this.$router.push('/login')
                })

            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#home {
  height: 100%;
  width: 100%;
  margin: 0;
}
#navigation {
  /*height: ;*/
}
</style>
