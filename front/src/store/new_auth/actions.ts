import { ActionTree } from 'vuex';
import config from '@/helpers/config';
import {
  banService,
  exeService,
  hostService,
  logService,
  motdService,
  noLoginService,
  resetNService,
  userService,
} from '@/services/login';
import { User } from '@/services/login/types';
import { RootState } from '@/store/types';
import {
  NewAuthState,
} from './types';
// import talker from "@/services/login/talker";

const actions: ActionTree<NewAuthState, RootState> = {
  startNewAuth: ({ commit }): Promise<any> => Promise.all([
    banService.getBanned(config.newAuth.userId),
    hostService.getHost(config.newAuth.hostname),
    noLoginService.getNoLogin(),
  ])
    .catch((e: Error) => commit('setError', e.message))
    .then(() => Promise.all([
      exeService.getStats(),
      resetNService.getStarted(),
    ]))
    .then(([
      stats,
      startedAt,
    ]) => {
      commit('setCreatedAt', stats.createdAt);
      commit('setStartedAt', startedAt);
    }),
  validateUsername: ({ commit }, payload: string): Promise<any> => {
    // Gets name tidied up
    commit('setError');
    return userService.getValidateUsername(payload)
      .catch((e: Error) => commit('setError', e.message));
  },
  submitUsername: ({ commit }): void => {
    commit('setNew', false);
  },
  resetUsername: ({ commit }): void => {
    commit('setUsername');
    commit('setNew', false);
  },
  onUsername: async ({ commit, dispatch }, payload: string): Promise<any> => {
    await dispatch('resetUsername');
    await dispatch('validateUsername', payload);
    const userId: number | null = await userService.getUser(payload);

    /* If he/she doesnt exist */
    // if (!user) return 'confirmUsername';

    // Password checking
    // return dispatch('auth', user);
    commit('setUsername', payload);
    commit('setNew', userId === null);
    return userId;
  },
  newUser: async ({ commit, state }, payload: User): Promise<any> => userService
    .postUser(payload)
    .then(() => commit('setUser', payload))
    .catch((e: Error) => commit('setError', e.message)),
  authUser: async ({ commit, state }, payload: User): Promise<any> => userService
    .getAuth(payload)
    .then((userId: number | null) => commit('setUser', payload))
    .catch((e: Error) => (
      (state.tries <= 0)
        ? commit('setError', '\nNo!\n\n')
        : commit('setTries', state.tries - 1)
    )),
  fetchMotd: ({ commit }): Promise<any> => motdService
    .getMessage()
    .then((message: string) => commit('setMotd', message)),
  startMain: ({ state }): Promise<any> => Promise.all([
    // Log entry
    // logService.postLog(`Game entry by ${state.user && state.user.username} : UID ${state.user && state.user.userId}`),
    // Run system
    // talker(state.user.username || '', !state.username),
  ]),
};

export default actions;
