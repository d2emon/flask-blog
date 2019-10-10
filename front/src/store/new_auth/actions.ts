import { ActionTree } from 'vuex';
import config from '@/helpers/config';
import {
  blogService,
} from '@/services/login';
import {
  ServiceStats,
  User,
  UserResponse,
} from '@/services/login/types';
import { RootState } from '@/store/types';
import {
  NewAuthState,
  ChangePassword,
} from './types';
// import talker from "@/services/login/talker";

const actions: ActionTree<NewAuthState, RootState> = {
  checkNewAuth: ({ commit }): Promise<void> => blogService
    .check(config.newAuth)
    .then((stats: ServiceStats) => commit('setStats', stats))
    .catch((e: Error) => commit('setError', e.message)),

  fetchUser: ({ commit }, payload: string): Promise<number | null> => blogService
    .getUser(payload)
    .then((response: UserResponse) => {
      commit('setUserResponse', response);
      const { user } = response;
      return user ? user.userId : null;
    })
    .catch((e: Error) => {
      commit('setError', e.message);
      return null;
    }),
  newUser: ({ commit, dispatch, state }, payload: User): Promise<any> => blogService
    .postUser(payload)
    .then((response: UserResponse) => {
      commit('setUserResponse', response);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),
  authUser: ({ commit, dispatch, state }, payload: User): Promise<any> => blogService
    .putUser(payload)
    .then((response: UserResponse) => {
      commit('setUserResponse', response);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),

  changePassword: ({ commit, state }, payload: ChangePassword): Promise<boolean> => blogService
    .putPassword(state.user as User, payload)
    .then((response: UserResponse) => {
      commit('setUserResponse', response);
      return !!response.success;
    }),
  showUser: ({ commit, state }, payload: string): Promise<void> => blogService
    .getUser(payload)
    .then((response: UserResponse) => commit('setViewUser', response)),
};

export default actions;
