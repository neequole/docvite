<template>
  <v-container fluid fill-height id="home">
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
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Clients</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Tests</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Resources</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Profile</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile>
              <v-list-tile-content>
                <v-list-tile-title>Settings</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-list-tile @click="logout">
              <v-list-tile-content>
                <v-list-tile-title>Logout</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
    <v-container fluid fill-height>
      {{ msg }}
    </v-container>
  </v-container>
</template>

<script>
    export default {
        data () {
            return {
                msg: 'Welcome to Your Vue.js App',
            }
        },
        methods: {
            logout() {
                this.$http.post('doctors/logout/').then(response => {
                    this.$router.push('/login')
                })

            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#home {
  margin: 0;
  padding: 0;
}
</style>
