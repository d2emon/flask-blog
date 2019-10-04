import {
  DataService,
  Item,
} from '@/services/login/types';
import items from '@/services/login/items';

// Gmainstubs
/**
 * Encode data
 * @param data {string} Data to encode
 * @param maxLength {number}
 * @returns {string} Encoded data
 */
export const encode = (data: string, maxLength?: number): Promise<string> => Promise
  .resolve(data.substr(0, maxLength));

/**
 * Decode data
 * @param data {string} Data to decode
 * @param maxLength {number}
 * @returns {string} Decoded data
 */
export const decode = (data: string, maxLength?: number): Promise<string> => Promise
  .resolve(data.substr(0, maxLength));

/**
 * INTERRUPTED SYSTEM CALL CATCH
 * @param unit {DataService}
 * @return {Promise<DataService>}
 */
const tryLock = (unit: DataService): Promise<DataService> => unit
  .setLock('LOCK_EX')
  .catch((e: Error) => ((e.message === 'EINTR') ? tryLock(unit) : Promise.reject(e)));

/**
 * Connect & set lock
 * @param filename {string}
 * @param permissions {string}
 * @return {Promise<DataService>}
 */
export const openLock = (
  filename: string,
  permissions: string,
): Promise<DataService | null> => (new DataService(filename))
  .connect(permissions)
  // NOTE: Always open with R or r+ or w
  .then(tryLock)
  .catch(() => null);

const reservedWords: string[] = [
  'The',
  'Me',
  'Myself',
  'It',
  'Them',
  'Him',
  'Her',
  'Someone',
  'There',
];

/**
 * Word is reserved
 * @param word {string}
 * @returns {boolean}
 */
const isReservedWord = (word: string): boolean => (reservedWords.indexOf(word) >= 0);

const fobn = async (name: string): Promise<boolean> => items
  .find((item: Item) => (name.toLowerCase() === item.name))
  .then((item?: Item) => !!item);

/**
 * Validate username
 * @param username {string}
 */
export const validateUsername = async (username: string): Promise<void> => {
  if (isReservedWord(username)) {
    throw new Error('Sorry I cant call you that\n');
  }
  if (username.length > 10) {
    throw new Error();
  }
  if (username.indexOf(' ') >= 0) {
    throw new Error();
  }
  if (await fobn(username)) {
    throw new Error('I can\'t call you that , It would be confused with an object\n');
  }
};
