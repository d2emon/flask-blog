<template>
  <v-card>
    <v-card-title>
      <h1>Welcome To Admin</h1>
    </v-card-title>

    <v-alert
      v-if="message"
      type="info"
    >{{ message }}</v-alert>

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

    <v-list
      one-line
      subheader
    >
      <v-subheader>Main Menu</v-subheader>

      <v-list-item
        @click="showChangePassword = true"
      >
        <v-list-item-content>
          Change Password
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        @click="logoutUser"
      >
        <v-list-item-content>
          Logout
        </v-list-item-content>
      </v-list-item>

      <template v-if="isAdmin">
        <v-divider />

        <v-list-item
          @click="askShowUser"
        >
          <v-list-item-content>
            Show user
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          @click="askEditUser"
        >
          <v-list-item-content>
            Edit user
          </v-list-item-content>
        </v-list-item>
        <v-list-item
          @click="removeUser"
        >
          <v-list-item-content>
            Delete user
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
import * as roles from '@/auth/roles';
import {
  ChangePassword,
  User,
} from '@/auth/types';

@Component({
  components: {
    AskUserForm: () => import('@/forms/AskUserForm.vue'),
    ChangePasswordForm: () => import('@/forms/ChangePasswordForm.vue'),
    EditUserForm: () => import('@/forms/EditUserForm.vue'),
  },
  computed: {
    ...mapState('auth', [
      'user',
      'errors',
      'viewUser',
      'logoutUser',
    ]),
  },
  methods: {
    ...mapActions('auth', [
      'changePassword',
      'showUser',
    ]),
  },
})
export default class UserMenu extends Vue {
  message: string | null = null;

  showChangePassword: boolean = false;

  askUser:boolean = false;

  showUserDialog: boolean = false;

  editUserDialog: boolean = false;

  onAskUser = (user: User) => {};

  get isAdmin(): boolean {
    return (this as any).user && ((this as any).user.role === roles.ADMIN);
  }

  get username(): string {
    return (this as any).user ? (this as any).user.username : 'Guest';
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

  removeUser() {
    if (!(this as any).isAdmin) return;
    console.log('Remove user');
  }
}
</script>
