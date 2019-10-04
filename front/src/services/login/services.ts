interface ServiceStats {
  createdAt?: string;
}

interface ListData {
  [k: string]: any,
}

interface FilesData extends ListData {
  BAN_FILE?: {[id:string]: boolean},
  EXE?: { stats?: ServiceStats },
  MOTD?: string,
  RESET_N?: {
    stats?: ServiceStats,
  }
}

const HOST_MACHINE: string = 'HOST_MACHINE';

const files: FilesData = {};

/**
 * List file
 * @param filename {string}
 */
const listFile = (filename: string): string => {
  const contents: string = files[filename] || `[Cannot Find -> ${filename}]`;
  return `\n${contents}\n`;
};

// Response interfaces
interface FileResponse {
  success?: boolean,
  error?: string | null,
}

interface ExeFileResponse extends FileResponse {
  stats?: ServiceStats,
}

interface MotdFileResponse extends FileResponse {
  message: string,
}

interface ResetNFileResponse extends FileResponse {
  started?: number,
}

// Files
const banFile = {
  getBanned: (userId: string): Promise<FileResponse> => Promise.resolve(
    (files.BAN_FILE && files.BAN_FILE[userId])
      ? { error: 'I\'m sorry- that userId has been banned from the Game\n' }
      : { success: true },
  ),
};

const exeFile = {
  getStats: (): Promise<ExeFileResponse> => Promise.resolve(
    files.EXE
      ? { success: true, stats: files.EXE.stats }
      : { success: false },
  ),
};

const hostFile = {
  getHost: (hostname: string): Promise<FileResponse> => Promise.resolve(
    (hostname === HOST_MACHINE)
      ? { success: true }
      : { error: `AberMUD is only available on ${HOST_MACHINE}, not on ${hostname}` },
  ),
};

const logFile = {
  postLog: (message: string): Promise<FileResponse> => Promise.resolve(console.log(message))
    .then(() => ({ success: true })),
};

const motdFile = {
  getMessage: (): Promise<MotdFileResponse> => Promise.resolve({
    success: true,
    message: listFile('MOTD'),
  }),
};

const noLoginFile = {
  getNoLogin: (): Promise<FileResponse> => Promise.resolve({
    success: !files.NOLOGIN,
    error: files.NOLOGIN,
  }),
};

const resetNFile = {
  getStarted: (): Promise<ResetNFileResponse> => Promise.resolve({
    success: true,
  }),
};

const checkResponse = (response: FileResponse, value: any = true) => (
  response.success
    ? (response.success && value)
    : Promise.reject(new Error(response.error || 'Unknown error')));

// Services
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
    .then((response: ExeFileResponse) => checkResponse(response, response.stats)),
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
    .then((response: ResetNFileResponse) => checkResponse(response, response.started)),
};
