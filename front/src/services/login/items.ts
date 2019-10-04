import { Item as ItemInterface } from '@/services/login/types';

export class Item implements ItemInterface {
  name: string;

  desc: string[];

  maxState: number;

  value: number;

  flannel: number;

  constructor(
    name: string,
    desc1: string,
    desc2: string,
    desc3: string,
    desc4: string,
    maxState: number,
    value: number,
    flannel: number,
  ) {
    this.name = name;
    this.desc = [
      desc1,
      desc2,
      desc3,
      desc4,
    ];
    this.maxState = maxState;
    this.value = value;
    this.flannel = flannel;
  }
}

const count = 194;

const items = [
  new Item(
    'SYS$WEATHER', 'The Weather', '', '', '',
    1, 0, 4,
  ),
  new Item(
    'umbrella',
    'A furled umbrella lies here', 'An unfurled umbrella lies here',
    '', '',
    1, 30, 0,
  ),
  new Item(
    'shelf',
    'A wooden shelf on the north wall looks as if it once held many ancient tomes\n'
      + 'There is a small opening in the north wall.',
    'A wooden shelf on the north wall looks as if it once held many ancient tomes',
    '', '',
    1, 0, 1,
  ),
  new Item(
    'panel',
    'A small wooden panel is open in the southern wall', '', '', '',
    1, 0, 1,
  ),
  new Item('candle',
    'A red candle burns here, emitting a soft flickering flame',
    'There is a red candle here', '', '', 1, 20, 0),
  new Item('candle', 'A blue candle burns here, emitting a soft flickering flame',
    'There is a blue candle here', '', '', 1, 20, 0),
  new Item('candle', 'A green candle burns here, emitting a soft flickering flame',
    'There is a green candle here', '', '', 1, 20, 0),
  new Item(
    'ball',
    'A crystal ball has been placed here',
    'A crystal ball has been placed here, glowing a pale red',
    'A crystal ball has been placed here, glowing a pale blue',
    'A crystal ball has been placed here, glowing a pale green',
    3, 20, 0,
  ),
  new Item(
    'scroll', 'A tattered scroll lies at your feet', '', '', '',
    0, 20, 0,
  ),
  new Item(
    'runes',
    'Some mysterious runes are etched on the wall', '', '', '',
    1, 0, 1,
  ),
  new Item(
    'candlestick',
    'A hefty gold candlestick lies here, a candle flickering brightly within it',
    'A hefty gold candlestick lies here, with a candle in it',
    'A hefty gold candlestick lies here', '',
    2, 100, 0,
  ),
  new Item(
    'cauldron',
    'A large cauldron bubbles away before you', '', '', '',
    1, 0, 1,
  ),
];

const each = (callback: (item: ItemInterface) => any): Promise<any> => Promise
  .all(items.map((item: ItemInterface) => callback(item)));

const find = (callback: (item: ItemInterface) => boolean): Promise<Item | undefined> => Promise
  .resolve(items.find(callback));

const db = {
  count,
  items,
  each,
  find,
};

export default db;
