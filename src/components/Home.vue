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
            <v-list-tile v-for="link in links" :key="link.name" @click="navigationClicked(link)">
              <v-list-tile-content>
                <v-list-tile-title>{{ link.text }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-navigation-drawer>
    <v-container fluid fill-height>
      <clients-container v-if="activeLink == 'client'"></clients-container>
      <div v-else>{{ activeLink }}</div>
    </v-container>
  </v-container>
</template>

<script>
  import Clients from '@/components/Clients'
    export default {
        data () {
            return {
                activeLink: 'client',
                links: [
                    {name: 'client', text: 'Clients',},
                    {name: 'test', text: 'Tests',},
                    {name: 'resource', text: 'Resources',},
                    {name: 'profile', text: 'Profile',},
                    {name: 'setting', text: 'Settings',},
                    {name: 'logout', text: 'Logout',},
                ],
            }
        },
        methods: {
            logout() {
                this.$http.post('doctors/logout/').then(response => {
                    localStorage.removeItem('user')
                    this.$router.push('/login')
                })

            },
            navigationClicked(link) {
                this.activeLink = link.name
                if(link.name == 'logout') this.logout()
                else console.log('test')
            }
        },
        components: {
            'clients-container': Clients,
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
