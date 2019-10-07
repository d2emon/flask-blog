import Item from '@/services/items/types';
import items from '@/services/items';

export const isValidString = (value: string): boolean => /^[a-z]*$/.test(value);

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
export const isReservedWord = (word: string): boolean => (reservedWords.indexOf(word) >= 0);

export const findItem = async (name: string): Promise<boolean> => items
  .find((item: Item) => (name.toLowerCase() === item.name))
  .then((item?: Item) => !!item);
