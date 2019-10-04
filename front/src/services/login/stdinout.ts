import {
  DataServiceInterface,
  Lock,
} from '@/services/login/types';

class StdInOut implements DataServiceInterface {
  name: string = 'stdin';

  connect(permissions: string): Promise<DataServiceInterface> {
    return Promise.resolve(this);
  }

  setLock(lock: Lock): Promise<DataServiceInterface> {
    return Promise.resolve(this);
  }

  flush(): Promise<DataServiceInterface> {
    return Promise.resolve(this);
  }

  push(text?: string): Promise<DataServiceInterface> {
    console.log(text);
    return Promise.resolve(this);
  }

  pull(maxLength?: number): Promise<string> {
    console.log(maxLength);
    return Promise.resolve('');
  }

  /**
   * Get password
   * @returns {Promise<string>} Password
   */
  password(prompt?: string): Promise<string> {
    return this.push(prompt || '')
      .then((s: DataServiceInterface) => (s as StdInOut).push('*'))
      .then((s: DataServiceInterface) => (s as StdInOut).flush())
      .then((s: DataServiceInterface) => Promise.all([
        (s as StdInOut).pull(),
        (s as StdInOut),
      ]))
      .then(([
        password,
        s,
      ]) => Promise.all([
        password,
        s.push('\n'),
      ]))
      .then(([password]) => password);
  }


  /**
   * Wait until return is pressed
   */
  wait(message?: string): Promise<DataServiceInterface> {
    return this.push(message)
      .then((s: DataServiceInterface) => (s as StdInOut).pull(1))
      .then((res: string) => ((res === '\n') ? Promise.resolve(this) : this.wait()));
  }
}

export default new StdInOut();
