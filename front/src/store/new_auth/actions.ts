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
  findUser: async ({ commit, dispatch, state }, payload: string): Promise<any> => userService
    .getUser(payload),
  newUser: async ({ commit, dispatch, state }, payload: User): Promise<any> => userService
    .postUser(payload)
    .then(() => commit('setUser', payload))
    .catch((e: Error) => commit('setError', e.message)),
  authUser: async ({ commit, dispatch, state }, payload: User): Promise<any> => userService
    .getAuth(payload)
    .then(() => commit('setUser', payload))
    .catch((e: Error) => commit('setError', e.message)),
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
