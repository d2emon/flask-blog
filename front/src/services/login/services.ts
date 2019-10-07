import {
  ServiceStats,
  FileResponse,
  ExeFileResponse,
  MotdFileResponse,
  ResetNFileResponse,
} from './types';

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

// Files
export const banFile = {
  getBanned: (userId: string): Promise<FileResponse> => Promise.resolve(
    (files.BAN_FILE && files.BAN_FILE[userId])
      ? { error: 'I\'m sorry- that userId has been banned from the Game\n' }
      : { success: true },
  ),
};

export const exeFile = {
  getStats: (): Promise<ExeFileResponse> => Promise.resolve(
    files.EXE
      ? { success: true, stats: files.EXE.stats }
      : { success: false },
  ),
};

export const hostFile = {
  getHost: (hostname: string): Promise<FileResponse> => Promise.resolve(
    (hostname === HOST_MACHINE)
      ? { success: true }
      : { error: `AberMUD is only available on ${HOST_MACHINE}, not on ${hostname}` },
  ),
};

export const logFile = {
  postLog: (message: string): Promise<FileResponse> => Promise.resolve(console.log(message))
    .then(() => ({ success: true })),
};

export const motdFile = {
  getMessage: (): Promise<MotdFileResponse> => Promise.resolve({
    success: true,
    message: listFile('MOTD'),
  }),
};

export const noLoginFile = {
  getNoLogin: (): Promise<FileResponse> => Promise.resolve({
    success: !files.NOLOGIN,
    error: files.NOLOGIN,
  }),
};

export const resetNFile = {
  getStarted: (): Promise<ResetNFileResponse> => Promise.resolve({
    success: true,
  }),
};
