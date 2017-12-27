<template>
    <v-layout row>
        <v-flex>
            <v-card>
                <template v-for="invitation in invitations">
                    <v-divider></v-divider>
                    <v-list three-line>
                        <v-list-tile>
                            <v-list-tile-content>
                                <v-list-tile-title>{{ invitation.client.fullname }}</v-list-tile-title>
                                <v-list-tile-sub-title>
                                    {{ moment(invitation.created).format('MMMM Do YYYY, h:mm:ss a') }}
                                </v-list-tile-sub-title>
                            </v-list-tile-content>
                            <v-list-tile-action>
                                <span>{{ invitation.status }}</span>
                            </v-list-tile-action>
                        </v-list-tile>
                    </v-list>
                </template>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        data () {
            return {
                invitations: [],
            }
        },
        methods: {
            getInvitations() {
                var user = JSON.parse(localStorage.getItem('user'))
                var url = `doctors/${user.id}/invitations/`
                this.$http.get(url).then(response => {
                    this.invitations = response.data
                }, response => {
                    this.invitations = []
                })
            }
        },
        created: function() {
            this.getInvitations()
        }
    }

</script>

<style scoped>
</style>