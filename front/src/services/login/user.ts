const PFL: string = '';

class User {
  username: string;

  password?: string;

  value3?: any;

  value4?: any;

  value5?: any;

  value6?: any;

  constructor(
    username: string,
    password?: string,
    value3?: string,
    value4?: string,
    value5?: string,
    value6?: string,
  ) {
    this.username = username;
    this.password = password;
    this.value3 = value3;
    this.value4 = value4;
    this.value5 = value5;
    this.value6 = value6;
  }

  checkPassword(password: string) {
    return this.password === password;
  }

  // chkname
  /**
   * Chek name for validity
   * @param username {string} Username
   * @returns {boolean} Is username valid
   */
  static checkValidName = (username: string): boolean => /^[a-z]*$/.test(username);

  static async validateUsername(value?: string): Promise<boolean> {
    // Check for legality of names
    if (!value) {
      throw new Error();
    }
    if (value.indexOf('.') >= 0) {
      throw new Error('Illegal characters in user name');
    }
    if (!User.checkValidName(value)) {
      throw new Error();
    }
    return validateUsername(value);
  }

  static async validatePassword(value?: string): Promise<boolean> {
    if (!value) {
      throw new Error();
    }
    if (value.indexOf('.') >= 0) {
      throw new Error('Illegal character in password\n');
    }
    return true;
  }

  async validate(): Promise<boolean> {
    return Promise.all([
      User.validateUsername(this.username),
      User.validatePassword(this.password),
    ]).then((res: boolean[]) => res.every((v => v)));
  }

  asString(): string {
    return `${this.username}.${this.password}.${this.value3}.${this.value4}.${this.value5}.${this.value6}`;
  }

  async encode(): Promise<string> {
    return encode(this.asString());
  }

  static async decode(s: string): Promise<User> {
    const decoded: string = await decode(s);
    const [username, password]: string[] = decoded.split('.');
    return Promise.resolve(new User(username, password));
  }

  async save(): Promise<boolean> {
    const encoded: string = await this.encode();
    const file: DataFile = new DataFile(PFL, 'a');
    await file.unlock().catch(() => {
      throw new Error('No persona file....\n');
    });
    await file.push(`${encoded}\n`);
    await file.close();
    return Promise.resolve(true);
  }

  /**
   * Return block data for user or null if not exist
   * @param uid {string} - User ID
   * @returns {User} - User
   */
  static async find(username: string): Promise<User | null> {
    const file: DataFile = new DataFile(PFL, 'r');
    await file.unlock().catch(() => {
      throw new Error('No persona file\n');
    });
    return file.search(
      async (value: string) => {
        const decoded: User = await User.decode(value);
        return (decoded.username.toLowerCase() === username.toLowerCase()) ? decoded : null;
      },
      255,
    );
  }
}
