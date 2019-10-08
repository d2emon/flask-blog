import {
  FileResponse,
} from './types';

// Files
export const logFile = {
  postLog: (message: string): Promise<FileResponse> => Promise.resolve(console.log(message))
    .then(() => ({ success: true })),
};
