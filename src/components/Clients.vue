<template>
    <v-layout row>
        <v-flex>
            <v-layout row id="header">
                <v-flex>
                </v-flex>
                <v-flex md3>
                    <v-btn color="primary" @click="inviteDialog=true">
                        <v-icon left dark>person_add</v-icon>
                            Invite Client
                    </v-btn>
                </v-flex>
            </v-layout>
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
        <!-- Invite client dialog -->
        <v-dialog v-model="inviteDialog" max-width="500px">
            <v-card>
                <v-form v-model="valid" ref="form" lazy-validation>
                  <v-card-title>
                    Invite Client
                  </v-card-title>
                  <v-card-text>
                      <v-text-field label="E-mail"
                                    v-model="email"
                                    :rules="emailRules"
                                    :error-messages="emailErrors"
                                    required>
                      </v-text-field>
                  </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" :disabled="!valid" @click="sendInvitation()">Invite</v-btn>
                    <v-btn flat @click.stop="inviteDialog=false">Close</v-btn>
                  </v-card-actions>
                </v-form>
            </v-card>
      </v-dialog>
    </v-layout>
</template>

<script>
    export default {
        data () {
            return {
                inviteDialog: false,
                invitations: [],
                email: '',
                emailRules: [
                    (v) => !!v || 'E-mail is required',
                    (v) => /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
                ],
                emailErrors: [],
                valid: false,
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
            },
            sendInvitation() {
                var data = {'email': this.email}
                this.$http.post('clients/invite/', data).then(response => {
                    this.emailErrors = []
                    this.inviteDialog = false
                    this.getInvitations()
                }, response => {
                    this.emailErrors.push(response.data.email) // TODO: clear when dialog is closed
                })
            }
        },
        created: function() {
            this.getInvitations()
        }
    }

</script>

<style scoped>
    #header{
        height: 50px;
    }
</style>