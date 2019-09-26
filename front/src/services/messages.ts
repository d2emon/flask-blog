export default {
  getMessages: (): Promise<string[]> => Promise.resolve([
    'Message 1',
    'Message 2',
    'Message 3',
  ]),
};
