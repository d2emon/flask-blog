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

/**
 * Delete user
 */
const deluser = async (): Promise<void> => {
  const name: string = await getunm();
  const u: User | null = await User.find(name);
  if (!u) return inOut.push('\nCannot delete non-existant user\n').then(() => {});
  return delu2(name);
};
