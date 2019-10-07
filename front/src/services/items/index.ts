import Item from './types';
import {
  count,
  items,
} from './data';


const each = (callback: (item: Item) => any): Promise<any> => Promise
  .all(items.map((item: Item) => callback(item)));

const find = (callback: (item: Item) => boolean): Promise<Item | undefined> => Promise
  .resolve(items.find(callback));

export default {
  count,
  items,
  each,
  find,
};
