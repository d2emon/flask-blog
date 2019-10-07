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

export default {
  /**
   * Check for legality of names
   * @param username
   */
  validateUsername: (username: string): Promise<FileResponse> => validateUsername(username)
    .then((success: boolean) => ({ success }))
    .catch((e: Error) => ({ error: e.message })),

  save: async (user: User): Promise<FileResponse> => Promise
    .all([
      validateUsername(user.username),
      validatePassword(user.password),
    ])
    .then((res: boolean[]) => {
      const success = res.every(v => v);
      if (success) {
        users.push({
          ...user,
          userId: users.length,
        });
      }
      return { success };
    })
    .catch((e: Error) => ({ error: e.message })),

  findUser: async (username: string): Promise<PflFileResponse> => Promise.resolve(
    (users as User[])
      .find(
        (value: User) => value.username.toLowerCase() === username.toLowerCase(),
      ),
  )
    .then((user?: User) => ({
      success: true,
      userId: user ? user.userId : undefined,
    }))
    .catch(() => ({ error: 'No persona file' })),

  authUser: async (user: User): Promise<PflFileResponse> => Promise.resolve(
    (users as User[])
      .find(
        (value: User) => (
          value.username.toLowerCase() === user.username.toLowerCase()
            && value.password === user.password
        ),
      ),
  )
    .then((u?: User) => ({ success: !!u, userId: u ? u.userId : undefined }))
    .catch(() => ({ error: 'No persona file' })),
};
