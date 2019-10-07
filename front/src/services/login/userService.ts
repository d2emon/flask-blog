import {
  User,
  FileResponse,
  PflFileResponse,
} from './types';
import {
  isValidString,
  isReservedWord,
  findItem,
} from './utils';

type Rule = (v: string) => Promise<string | boolean>;

const users: User[] = [];

const isValidUsername: Rule[] = [
  async v => !v || !isReservedWord(v)
    || 'Sorry I cant call you that',
  async v => !v || v.length <= 10
    || 'Username string is too long',
  async v => !v || v.indexOf(' ') < 0
    || 'Spaces in user name',
  async v => !v || !(await findItem(v))
    || 'I can\'t call you that , It would be confused with an object',
];

const usernameRules: Rule[] = [
  async v => !!v
    || 'Username is required',
  async v => !v || v.indexOf('.') < 0
    || 'Illegal characters in username',
  async v => !v || isValidString(v)
    || 'Username string is invalid',
  ...isValidUsername,
];

const passwordRules: Rule[] = [
  async v => !!v
    || 'Password is required',
  async v => !v || v.indexOf('.') < 0
    || 'Illegal characters in password',
];

const applyRules = (value: string, rules: Rule[]): Promise<boolean> => Promise.all(
  rules.map((rule: Rule) => rule(value)),
)
  .then(res => res.filter((isValid: string | boolean) => isValid !== true) as string[])
  .then((errors: string[]) => {
    if ((errors.length) <= 0) return true;
    throw new Error(errors[0]);
  });

const validateUsername = async (username: string): Promise<boolean> => applyRules(
  username.toLowerCase(),
  usernameRules,
);

const validatePassword = async (password: string): Promise<boolean> => applyRules(
  password.toLowerCase(),
  passwordRules,
);

const save = async (user: User): Promise<User> => Promise
  .all([
    validateUsername(user.username),
    validatePassword(user.password),
  ])
  .then((res: boolean[]) => {
    if (!res.every(v => v)) {
      throw new Error();
    }
    const newUser: User = {
      ...user,
      userId: users.length,
    };
    users.push(newUser);
    return newUser;
  });

const findUser = async (username: string): Promise<User | undefined> => users
  .find((value: User) => (value.username.toLowerCase() === username.toLowerCase()));

export default {
  findUser: async (username: string): Promise<PflFileResponse> => findUser(username)
    .then((user: User | undefined) => {
      console.log(user);
      return user;
    })
    .then((user: User | undefined) => ({
      success: true,
      userId: user ? user.userId : undefined,
    }))
    .catch((e: Error) => ({ error: e.message })),

  newUser: async (user: User): Promise<PflFileResponse> => {
    const found: User | undefined = await findUser(user.username);
    if (found) return { error: 'User already exists' };
    return save(user)
      .then((newUser: User) => ({
        success: true,
        userId: newUser.userId,
      }))
      .catch((e: Error) => ({ error: e.message }));
  },

  authUser: async (user: User): Promise<PflFileResponse> => {
    const found: User | undefined = await findUser(user.username);
    if (!found) return { error: 'User doesn\'t exists' };
    if (user.password !== found.password) return { error: 'Wrong password!' };
    return {
      success: !!found,
      userId: found.userId,
    };
  },
};
