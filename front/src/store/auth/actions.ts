import { ActionTree } from 'vuex';
import { RootState } from '@/store/types';
import { AuthState } from './types';
import {
  AuthResponse,
  ChangePassword,
  LoginData,
  RegistrationData,
} from '@/auth/types';
import User from '@/auth/user';
import auth from '@/helpers/auth';

const actions: ActionTree<AuthState, RootState> = {
  processAuthResponse: ({ commit }, payload: {messages: string}) => payload,
  /*
  {
    const {
      messages,
    } = payload;
    commit('setMessages', messages);
    return payload;
  },
   */

  registerUser: ({ dispatch }, payload: RegistrationData): Promise<void> => auth
    .registerUser(payload)
    .then(data => dispatch('processAuthResponse', data)),
  /*
  loginUser: ({ commit, dispatch }, payload: LoginRequest): Promise<void> => auth
    .authUser(payload)
    .then(data => dispatch('processAuthResponse', data))
    .then((data) => {
      const { token } = data;
      commit('setToken', token);
      return data;
    }),
  */
  loginUser: ({ commit }, payload: LoginData): Promise<void> => auth
    .getToken({
      username: payload.username,
      password: payload.password,
    })
    .then((token: string) => {
      if (payload.rememberMe) commit('setToken', token);
      commit('setUser', new User(token));
    })
    .catch((e: Error) => {
      console.error(e);
      commit('removeToken');
      // commit('setMessages', e.message);
    }),
  logoutUser: ({ commit, getters }): Promise<void> => auth
    .logoutUser(getters.token)
    .then(() => commit('removeToken')),

  // New
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
    .then((response: AuthResponse) => commit('setUserResponse', response))
    .catch((e: Error) => commit('setError', e.message)),
  authUser: ({ commit, dispatch, state }, payload: User): Promise<any> => auth
    .updateUser(payload)
    .then((response: AuthResponse) => commit('setUserResponse', response))
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
