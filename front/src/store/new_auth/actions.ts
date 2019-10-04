import { ActionTree } from 'vuex';
import {
  banService,
  exeService,
  hostService, logService, motdService,
  noLoginService,
  resetNService,
} from '@/services/login/services';
import { RootState } from '@/store/types';
import {
  NewAuthState,
  NewAuthData,
} from './types';
import talker from "@/services/login/talker";

const actions: ActionTree<NewAuthState, RootState> = {
  startNewAuth: ({ commit }, payload: NewAuthData): Promise<any> => Promise.all([
    banService.getBanned(payload.userId),
    hostService.getHost(payload.hostname),
    noLoginService.getNoLogin(),
  ])
    .catch((e: Error) => commit('setError', e.message))
    .then(() => Promise.all([
      exeService.getStats(),
      resetNService.getStarted(),
    ]))
    .then(([
      createdAt,
      startedAt,
    ]) => {
      commit('setCreatedAt', createdAt);
      commit('setStartedAt', startedAt);
    }),
  validateUsername: ({ commit }, payload: string): Promise<any> => {
    // Gets name tidied up
    commit('setError');
    return User.validateUsername(payload)
      .catch((e: Error) => commit('setError', e.message));
  },
  onUsername: async ({ dispatch }, payload: string): Promise<any> => {
    await dispatch('validateUsername', payload);
    const user: User | null = await User.find(payload);

    /* If he/she doesnt exist */
    if (!user) return 'confirmUsername';

    // Password checking
    return dispatch('auth', user);
  },
  authUser: async ({ commit, state }, payload: User): Promise<any> => {
    if (payload.checkPassword(state.password || '')) {
      return commit('setUser', payload);
    }
    return (state.tries <= 0)
      ? commit('setError', '\nNo!\n\n')
      : commit('setTries', state.tries - 1);
  },
  newUser: async ({ commit, state }): Promise<any> => {
    const user: User = new User(
      state.username || '',
      state.password,
    );
    return user.validate()
      .then(() => user.save())
      .catch((e: Error) => commit('setError', e.message));
  },
  auth: ({ dispatch }, payload: User): Promise<any> => (
    payload
      ? dispatch('authUser', payload)
      : dispatch('newUser')
  ),
  fetchMotd: ({ commit }): Promise<any> => motdService
    .getMessage()
    .then((message: string) => commit('setMotd', message)),
  startMain: ({ state }): Promise<any> => Promise.all([
    // Log entry
    logService.postLog(`Game entry by ${state.user && state.user.username} : UID ${state.user && state.user.userId}`),
    // Run system
    talker(state.user.username || '', !state.username),
  ]),
};

export default actions;
