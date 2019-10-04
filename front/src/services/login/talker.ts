import {
  cls,
  getUserId,
} from '@/services/login/utils';
import inOut from '@/services/login/stdinout';

const execl = (args: string[]): Promise<void> => Promise.resolve();

const EXE: string = '';
const PFL: string = '';
const PFT: string = '';

const isWizard = (): boolean => {
  const user: string = getUserId();
  return [
    'wisner',
    'wisner',
  ].indexOf(user) >= 0;
};

const answer = (): string => getkbd(2).toLowerCase().substr(0, 1);

const play = (args: string[]): Promise<void> => execl(args).catch(() => {
  throw new Error('mud.exe : Not found\n');
});

//
/**
 * Edit user field
 * @param field {string} Field name
 * @param value {string} Field value
 * @returns {string} New value
 */
const edFld = async (field: string, value?: string): Promise<string> => {
  await inOut.push(`${field}(Currently ${value} ):`);
  const newValue: string = await inOut.pull(128);
  if (newValue.startsWith('.')) return value || '';
  if (newValue.indexOf('.') >= 0) {
    await inOut.push('\nInvalid Data Field\n');
    return edFld(field, value);
  }
  return newValue || value || '';
};

/**
 * Get user name
 * @returns {string} - Username
 */
const getunm = (): Promise<string> => inOut.push('\nUser Name:')
  .then(() => inOut.pull(79));

/**
 * For show user and edit user
 * @param name {string} - Username
 * @returns {Promise<User | null>} - User
 */
const shu = async (name: string): Promise<User | null> => {
  const u: User | null = await User.find(name);
  if (!u) {
    await inOut.push('\nNo user registered in that name\n\n\n');
    return null;
  }

  await inOut.push(`\n\nUser Data For ${name}\n\n`);
  await inOut.push(`Name:${u.username}\nPassword:${u.password}\n`);
  return u;
};

/**
 * For delete and edit
 * @param name {string} User name
 */
const delu2 = async (name: string): Promise<void> => {
  let a: DataFile = new DataFile(PFL, 'r+');
  let b: DataFile = new DataFile(PFT, 'w');
  let files: DataFile[] | null = await Promise.all([
    a.unlock(),
    b.unlock(),
  ]).catch(() => null);
  if (files === null) return;
  const found: User = await files[0].search(
    async (value: string): Promise<User | null> => {
      const u: User | null = await User.decode(value);
      return (u && (u.username.toLowerCase() === name.toLowerCase())) ? u : null;
    },
    128,
  );
  await Promise.all(files.map((f: DataFile) => f.close()));

  a = new DataFile(PFL, 'r+');
  b = new DataFile(PFT, 'w');
  files = await Promise.all([
    a.unlock(),
    b.unlock(),
  ]).catch(() => null);
  if (files === null) return;
  await files[1].search(
    async (value: string): Promise<boolean> => {
      if (!value) return false;
      if (!files) return false;
      files[0].push(value);
      return true;
    },
    128,
  );
  await Promise.all(files.map((f: DataFile) => f.close()));
};

//

const quickStart = (name: string): Promise<void> => play([
  EXE,
  '   --}----- ABERMUD -----{--    Playing as ',
  name,
]);

const start = async (name: string): Promise<void> => {
  cls();
  await inOut.push('The Hallway\n');
  await inOut.push('You stand in a long dark hallway, which echoes to the tread of your\n');
  await inOut.push('booted feet. You stride on down the hall, choose your masque and enter the\n');
  await inOut.push('worlds beyond the known......\n\n');
  return play([
    EXE,
    '   --{----- ABERMUD -----}--      Playing as ',
    name,
  ]);
};

/**
 * Change your password
 * @param user {string} Username
 */
const chpwd = async (user: string): Promise<void> => {
  const chptagn = async (): Promise<string> => {
    const newPassword: string = await inOut.password();
    if (!newPassword) return chptagn();
    if (newPassword.indexOf(',') >= 0) {
      await inOut.push('Illegal Character in password\n');
      return chptagn();
    }

    const pv: string = await inOut.password('\nVerify Password\n');
    if (pv !== newPassword) {
      await inOut.push('\nNO!\n');
      return chptagn();
    }

    return newPassword;
  };

  const u: User | null = await User.find(user);
  if (!u) return;
  const data: string = await inOut.password('\nOld Password\n');
  if (data !== u.password) {
    await inOut.push('Incorrect Password\n');
    return;
  }

  await inOut.push('New Password\n');
  u.password = await chptagn();
  await delu2(user); // delete me and tack me on end!
  await u.save();

  await inOut.push('Changed\n');
};

const testVersion = async (): Promise<void> => {
  cls();
  await inOut.push('Entering Test Version\n');
};

/**
 * Show user and wait
 */
const showuser = async (): Promise<void> => {
  cls();
  const name: string = await getunm();
  await shu(name);
  await inOut.wait('\nHit Return...\n');
};

/**
 * Edit user
 */
const edituser = async (): Promise<void> => {
  await cls();
  const name: string = await getunm();
  const u: User = await shu(name) || new User(name, 'default', 'E');
  await inOut.push(`\nEditing : ${name}\n\n`);
  u.username = await edFld('Name:', u.username);
  u.password = await edFld('Password:', u.password);
  await delu2(name);
  return u.save().catch(() => null).then(() => {});
};

/**
 * Delete user
 */
const deluser = async (): Promise<void> => {
  const name: string = await getunm();
  const u: User | null = await User.find(name);
  if (!u) return inOut.push('\nCannot delete non-existant user\n').then(() => {});
  return delu2(name);
};

interface MenuResult {
  exit?: number;
  result?: any;
}

const mainMenu = async (itemId: string, name: string, isawiz: boolean): Promise<MenuResult> => {
  if (itemId === '1') return { result: start(name) };
  if (itemId === '2') return { result: chpwd(name) };
  if (itemId === '0') return { exit: 0 };
  if (itemId === '4') return { result: isawiz && testVersion() };
  if (itemId === 'a') return { result: isawiz && showuser() };
  if (itemId === 'b') return { result: isawiz && edituser() };
  if (itemId === 'c') return { result: isawiz && deluser() };
  throw new Error('Bad Option\n');
};

const talker = async (name: string, qnmrq: boolean): Promise<number> => {
  if (qnmrq) await quickStart(name);

  cls();
  await inOut.push('Welcome To AberMUD II [Unix]\n\n\n');
  await inOut.push('Options\n\n');
  await inOut.push('1]  Enter The Game\n');
  await inOut.push('2]  Change Password\n');
  await inOut.push('\n\n0] Exit AberMUD\n');
  await inOut.push('\n\n');

  const isawiz = isWizard();
  if (isawiz) {
    await inOut.push('4] Run TEST game\n');
    await inOut.push('A] Show persona\n');
    await inOut.push('B] Edit persona\n');
    await inOut.push('C] Delete persona\n');
  }
  await inOut.push('\n\n');

  await inOut.push('Select > ');

  const res: MenuResult = await mainMenu(answer(), name, isawiz)
    .catch(
      (e: Error) => inOut
        .push(e.message)
        .then(() => ({})),
    );

  return (res.exit !== undefined) ? res.exit : talker(name, qnmrq);
};

export default talker;
