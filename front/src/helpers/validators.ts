export type Validator = (v:any) => string | boolean;
export type FormRules = {[key: string]: Validator[]};

const isRequiredMessage: string = 'Field is required';
const isEmailMessage: string = 'Field is not a valid email';

export const isRequired = (msg: string = isRequiredMessage): Validator => v => (
  !!v || msg
);
export const isEmail = (msg: string = isEmailMessage): Validator => v => (
  !v || /.+@.+\..+/.test(v) || 'E-mail must be valid'
);
