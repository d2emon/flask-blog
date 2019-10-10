import Vue from 'vue';
import { MutationTree } from 'vuex';
import {
  ServiceStats,
  User, UserResponse,
} from '@/services/login/types';
import { NewAuthState } from './types';

/**
 * Transform timestamp to text
 * Elapsed time and similar goodies
 * @param {number} timestamp - Time as timestamp
 * @returns {string} - Time as text
 */
const timestampToString = (timestamp: number): string => {
  const hours: number = Math.floor(timestamp / 36000);
  const minutes: number = (timestamp / 60) % 60;
  const seconds: number = timestamp % 60;

  const minutesText: string = ((minutes === 1) ? '1 minute' : `${minutes} minutes.`);
  const secondsText: string = ((seconds === 1) ? '1 second' : `${seconds} seconds.`);

  if (timestamp > 24 * 60 * 60) return 'Over a day!!!'; // Add a Day!
  if (timestamp < 61) return secondsText;
  if (timestamp === 60) return '1 minute';
  if (timestamp < 120) return `1 minute and ${secondsText}`;
  if (timestamp / 60 === 60) return '1 minute';
  if (timestamp < 3600) return `${minutes} minutes and ${secondsText}`;
  if (timestamp < 7200) return `1 hour and ${minutesText}`;
  return `${hours} hours and ${minutesText}`;
};

const mutations: MutationTree<NewAuthState> = {
  setError: (state, payload?: string) => Vue.set(state, 'error', payload),
  setStats: (state, payload: ServiceStats) => {
    const now = new Date();
    const {
      createdAt,
      startedAt,
    } = payload;

    Vue.set(state, 'createdAt', createdAt);
    Vue.set(
      state,
      'startedAt',
      startedAt
        ? timestampToString(now.getTime() - startedAt)
        : undefined,
    );
  },
  setUser: (state, payload?: User) => Vue.set(state, 'user', payload),
  setUserResponse: (state, payload: UserResponse) => {
    const { user } = payload;
    Vue.set(state, 'error', undefined);
    Vue.set(state, 'errors', payload.errors);
    if (user) {
      Vue.set(state, 'motd', user.messageOfTheDay);
      Vue.set(state, 'role', user.role);
    }
  },
  setViewUser: (state, payload: UserResponse) => {
    Vue.set(state, 'error', undefined);
    Vue.set(state, 'viewUser', payload.user);
  },
};

export default mutations;
