import { GetterTree } from 'vuex';
import { RootState } from '@/store/types';
import { AuthState } from './types';

const getters: GetterTree<AuthState, RootState> = {
  token: (): string | null => localStorage.getItem('token'),
};

export default getters;
