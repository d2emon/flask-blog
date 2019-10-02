import { ActionTree } from 'vuex';
import authService from '@/services/auth';
import { RootState } from '@/store/types';
import User, {
  AuthState,
  LoginData,
  RegistrationData,
} from './types';

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

  registerUser: ({ dispatch }, payload: RegistrationData): Promise<void> => authService
    .registerUser(payload)
    .then(data => dispatch('processAuthResponse', data)),
  /*
  loginUser: ({ commit, dispatch }, payload: LoginRequest): Promise<void> => authService
    .authUser(payload)
    .then(data => dispatch('processAuthResponse', data))
    .then((data) => {
      const { token } = data;
      commit('setToken', token);
      return data;
    }),
  */
  loginUser: ({ commit }, payload: LoginData): Promise<void> => authService
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
  logoutUser: ({ commit, getters }): Promise<void> => authService
    .logoutUser(getters.token)
    .then(() => commit('removeToken')),
};

export default actions;
