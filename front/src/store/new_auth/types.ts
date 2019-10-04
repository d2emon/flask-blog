export interface NewAuthState {
  error?: string,
  createdAt?: string,
  startedAt?: string,
  username?: string,
  password?: string,
  tries: number,
  user?: User,
  motd?: string,
}

export interface NewAuthData {
  userId: string,
  hostname: string,
}
