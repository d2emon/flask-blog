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
} from './types';
// import talker from "@/services/login/talker";

const actions: ActionTree<NewAuthState, RootState> = {
  checkNewAuth: ({ commit }): Promise<void> => blogService
    .check(config.newAuth)
    .then((stats: ServiceStats) => commit('setStats', stats))
    .catch((e: Error) => commit('setError', e.message)),

  fetchUser: async ({ commit }, payload: string): Promise<number | null> => blogService
    .getUser(payload)
    .then((user: UserResponse) => {
      commit('setUserResponse', user);
      return user.userId || null;
    })
    .catch((e: Error) => {
      commit('setError', e.message);
      return null;
    }),
  newUser: async ({ commit, dispatch, state }, payload: User): Promise<any> => blogService
    .postUser(payload)
    .then((user: UserResponse) => {
      commit('setUserResponse', user);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),
  authUser: async ({ commit, dispatch, state }, payload: User): Promise<any> => blogService
    .putUser(payload)
    .then((user: UserResponse) => {
      commit('setUserResponse', user);
      commit('setUser', payload);
    })
    .catch((e: Error) => commit('setError', e.message)),
  startMain: ({ state }): Promise<any> => Promise.all([
    // Log entry
    // logService.postLog(`Game entry by ${state.user && state.user.username} : UID ${state.user && state.user.userId}`),
    // Run system
    // talker(state.user.username || '', !state.username),
  ]),
};

export default actions;
