import {
  User,
  ServiceStats,
  FileResponse,
  ExeFileResponse,
  MotdFileResponse,
  PflFileResponse,
  ResetNFileResponse,
} from './types';
import {
  banFile,
  exeFile,
  hostFile,
  logFile,
  motdFile,
  noLoginFile,
  resetNFile,
} from './services';
import pflService from './userService';

const checkResponse = (response: FileResponse, value: any = true) => (
  response.success
    ? (response.success && value)
    : Promise.reject(new Error(response.error || 'Unknown error')));

export const banService = {
  /**
   * Check if banned first
   * Check to see if UID in banned list
   * @param userId {string}
   * @returns {Promise<boolean>} User is banned
   */
  getBanned: (userId: string): Promise<boolean> => banFile.getBanned(userId)
    .then(checkResponse),
};

export const exeService = {
  /**
   * Check for all the created at stuff
   * We use stats for this which is a UN*X system call
   * @returns {Promise<ServiceStats>} Stats of service
   */
  getStats: (): Promise<ServiceStats> => exeFile.getStats()
    .then((response: ExeFileResponse) => checkResponse(response, response.stats))
    .catch(() => ({})),
};

export const hostService = {
  /**
   * Check we are running on the correct host
   * see the notes about the use of flock();
   * and the affects of lockf();
   * @param hostname {string}
   */
  getHost: (hostname: string): Promise<boolean> => hostFile.getHost(hostname)
    .then(checkResponse),
};

export const logService = {
  /**
   * Add to system log
   * @param message {string}
   */
  postLog: (message: string): Promise<boolean> => logFile.postLog(message)
    .then(checkResponse),
};

export const motdService = {
  /**
   * Show message of the day
   */
  getMessage: (): Promise<string> => motdFile.getMessage()
    .then((response: MotdFileResponse) => checkResponse(response, response.message)),
};

export const noLoginService = {
  /**
   * Check if there is a no login file active
   */
  getNoLogin: (): Promise<boolean> => noLoginFile.getNoLogin()
    .then(checkResponse),
};

export const resetNService = {
  /**
   * Get started date
   */
  getStarted: (): Promise<number | undefined> => resetNFile.getStarted()
    .then((response: ResetNFileResponse) => checkResponse(response, response.started))
    .catch(() => undefined),
};

export const userService = {
  getValidateUsername: (username: string): Promise<boolean> => pflService
    .validateUsername(username)
    .then((response: FileResponse) => checkResponse(response)),
  postUser: (user: User): Promise<boolean> => pflService
    .save(user)
    .then((response: FileResponse) => checkResponse(response)),
  getUser: (username: string): Promise<number | null> => pflService
    .findUser(username)
    .then((response: PflFileResponse) => checkResponse(response, response.userId || null)),
  getAuth: (user: User): Promise<number | null> => pflService
    .authUser(user)
    .then((response: PflFileResponse) => checkResponse(response, response.userId || null)),
};
