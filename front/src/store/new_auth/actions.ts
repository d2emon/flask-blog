import { ActionTree } from 'vuex';
import config from '@/helpers/config';
import auth from '@/helpers/auth';
import {
  ServiceStats,
  User,
  ChangePassword,
  AuthResponse,
} from '@/d2auth/services/login/types';
import { RootState } from '@/store/types';
import { NewAuthState } from './types';

const actions: ActionTree<NewAuthState, RootState> = {
  checkNewAuth: ({ commit }): Promise<void> => auth
    .check(config.newAuth)
    .then((stats: ServiceStats) => commit('setStats', stats))
    .catch((e: Error) => commit('setError', e.message)),

  fetchUser: ({ commit }, payload: string): Promise<number | null> => auth
    .getUser(payload)
    .then((response: AuthResponse) => {
      commit('setUserResponse', response);
      const { user } = response;
      return (user && user.userId) ? user.userId : null;
    })
    .catch((e: Error) => {
      commit('setError', e.message);
      return null;
    }),
  newUser: ({ commit, dispatch, state }, payload: User): Promise<any> => auth
    .newUser(payload)
    .then((response: AuthResponse) => {
      commit('setUserResponse', response);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),
  authUser: ({ commit, dispatch, state }, payload: User): Promise<any> => auth
    .updateUser(payload)
    .then((response: AuthResponse) => {
      commit('setUserResponse', response);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),

  changePassword: ({ commit, state }, payload: ChangePassword): Promise<boolean> => auth
    .newPassword(state.user as User, payload)
    .then((response: AuthResponse) => {
      commit('setUserResponse', response);
      return !!response.success;
    }),
  showUser: ({ commit, state }, payload: string): Promise<void> => auth
    .getUser(payload)
    .then((response: AuthResponse) => commit('setViewUser', response)),
};

export default actions;
