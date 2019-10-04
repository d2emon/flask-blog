export type Lock = 'LOCK_SH' | 'LOCK_EX' | 'LOCK_UN';

export interface DataServiceInterface {
  name: string;
  connect(permissions: string): Promise<DataServiceInterface>;
  setLock(lock: Lock): Promise<DataServiceInterface>;
}

export interface Item {
  name: string;
  desc: string[];
  maxState: number;
  value: number;
  flannel: number;
}

export class DataService implements DataServiceInterface {
  name: string;

  permissions?: string;

  lock?: string;

  constructor(name: string) {
    this.name = name;
  }

  async connect(permissions: string): Promise<DataServiceInterface> {
    this.permissions = permissions;
    return this;
  }

  async setLock(lock: Lock): Promise<DataServiceInterface> {
    switch (lock) {
      case 'LOCK_SH':
        this.lock = 'F_RDLCK';
        break;
      case 'LOCK_EX':
        this.lock = 'F_WRLCK';
        break;
      case 'LOCK_UN':
        this.lock = 'F_UNLCK';
        break;
      default:
        throw new Error('EINVAL');
    }

    // this.l_whence = 'SEEK_SET';
    // this.l_start = this.l_len = 0;
    // fcntl(this, lock ? 'F_SETLK' : 'F_SETLKW', this.lock);
    return this;
  }
}
