<template>
  <v-card>
    <v-card-title>
      <h1>Welcome To Blog</h1>
    </v-card-title>

    <v-alert
      v-if="message"
      type="info"
    >{{ message }}</v-alert>

    <v-dialog
      v-model="showDialog"
      max-width="512"
    >
      <v-card>
        <v-card-title>{{ dialogTitle }}</v-card-title>
        <v-container>
          <v-card-text>
            <h3>The Hallway</h3>
            <div>
              You stand in a long dark hallway, which echoes to the tread of your
              booted feet. You stride on down the hall, choose your masque and enter the
              worlds beyond the known......
            </div>
          </v-card-text>
        </v-container>
        <v-card-actions>
          <v-btn
            @click="showDialog = false"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="showChangePassword"
      max-width="512"
    >
      <v-card>
        <v-container>
          <change-password-form
            :errors="errors"
            @submit="onChangePassword"
          />
        </v-container>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="askUser"
      max-width="512"
    >
      <v-card>
        <v-container>
          <ask-user-form
            :errors="errors"
            @submit="onAskUser"
          />
        </v-container>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="showUserDialog"
      max-width="512"
    >
      <v-card>
        <v-card-title
          v-if="!viewUser"
        >
          No user registered in that name
        </v-card-title>
        <template
          v-else
        >
          <v-card-title>
            User Data For {{ viewUser.username }}
          </v-card-title>
          <v-card-text>
            <div>Name: {{ viewUser.username }}</div>
            <div>Password: {{ viewUser.password }}</div>
          </v-card-text>
        </template>
        <v-card-actions>
          <v-btn
            @click="showUserDialog = false"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="editUserDialog"
      max-width="512"
    >
      <v-card>
        <v-template
          v-if="!viewUser"
        >
          <v-card-title>
            No user registered in that name
          </v-card-title>
          <v-card-actions>
            <v-btn
              @click="editUserDialog = false"
            >
              Ok
            </v-btn>
          </v-card-actions>
        </v-template>
        <v-container
          v-else
        >
          <edit-user-form
            :username="viewUser.username"
            :errors="errors"
            @submit="onSaveEditedUser"
          />
        </v-container>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="show"
      max-width="512"
    >
      <v-card>
        <v-card-title></v-card-title>
        <v-card-text></v-card-text>
        <v-card-actions></v-card-actions>
      </v-card>
    </v-dialog>

    <v-list
      one-line
      subheader
    >
      <v-subheader>Options</v-subheader>

      <v-list-item
        @click="start"
      >
        <v-list-item-content>
          Enter Blog
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        @click="showChangePassword = true"
      >
        <v-list-item-content>
          Change Password
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        @click="logout"
      >
        <v-list-item-content>
          Exit
        </v-list-item-content>
      </v-list-item>

      <template v-if="isAdmin">
        <v-divider />

        <v-list-item
          @click="testVersion"
        >
          <v-list-item-content>
            Run TEST game
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          @click="askShowUser"
        >
          <v-list-item-content>
            Show persona
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          @click="askEditUser"
        >
          <v-list-item-content>
            Edit persona
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          @click="removeUser"
        >
          <v-list-item-content>
            Delete persona
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';
import {
  mapActions,
  mapState,
} from 'vuex';
import * as roles from '@/d2auth/services/login/roles';
import { ChangePassword } from '@/store/new_auth/types';
import { User } from '@/d2auth/services/login/types';

@Component({
  components: {
    AskUserForm: () => import('@/forms/AskUserForm.vue'),
    ChangePasswordForm: () => import('@/forms/ChangePasswordForm.vue'),
    EditUserForm: () => import('@/forms/EditUserForm.vue'),
  },
  computed: {
    ...mapState('newAuth', [
      'role',
      'user',
      'errors',
      'viewUser',
    ]),
  },
  methods: {
    ...mapActions('newAuth', [
      'changePassword',
      'showUser',
    ]),
  },
})
export default class UserMenu extends Vue {
  message: string | null = null;

  showDialog: boolean = false;

  showChangePassword: boolean = false;

  askUser:boolean = false;

  showUserDialog: boolean = false;

  editUserDialog: boolean = false;

  show: boolean = false;

  dialogTitle: string = `   --}----- ABERMUD -----{--    Playing as ${this.username}`;

  onAskUser = (user: User) => {};

  get isAdmin(): boolean {
    return (this as any).role === roles.ADMIN;
  }

  get username(): string {
    return (this as any).user ? (this as any).user.username : 'Guest';
  }

  start() {
    this.dialogTitle = `   --{----- ABERMUD -----}--      Playing as ${this.username}`;
    this.showDialog = true;
  }

  onChangePassword(values: ChangePassword) {
    return (this as any).changePassword(values)
      .then((res: boolean) => {
        this.showChangePassword = !res;
        if (res) this.message = 'Changed';
      });
  }

  onShowUser({ username }: User) {
    this.askUser = false;
    this.showUserDialog = true;
    (this as any).showUser(username);
  }

  onEditUser({ username }: User) {
    this.askUser = false;
    this.editUserDialog = true;
    (this as any).showUser(username);
  }

  onSaveEditedUser(user: User) {
    this.editUserDialog = false;
    console.log(user);
  }

  askShowUser() {
    if (!(this as any).isAdmin) return;
    this.onAskUser = this.onShowUser;
    this.askUser = true;
  }

  askEditUser() {
    if (!(this as any).isAdmin) return;
    this.onAskUser = this.onEditUser;
    this.askUser = true;
  }

  logout() {

  }

  testVersion() {
    if (!(this as any).isAdmin) return;
    this.dialogTitle = 'Entering Test Version';
    this.showDialog = true;
  }

  removeUser() {
    if (!(this as any).isAdmin) return;
  }
}
</script>
