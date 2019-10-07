export interface ItemInterface {
  name: string;
  desc: string[];
  maxState: number;
  value: number;
  flannel: number;
}

export default class Item implements ItemInterface {
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
