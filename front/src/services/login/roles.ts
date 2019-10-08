export const UNAUTHORIZED = 'UNAUTHORIZED';
export const USER = 'USER';
export const ADMIN = 'ADMIN';

export type Role = typeof UNAUTHORIZED
  | typeof USER
  | typeof ADMIN;
