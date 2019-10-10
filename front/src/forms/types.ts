import { Validator } from '@/helpers/validators';

export interface FormField<T> {
  errors?: string[],
  isCheckBox?: boolean,
  label?: string,
  required?: boolean,
  rules?: Validator[],
  size?: number,
  type?: string,
  value?: T,
}

export type FormData = { [field: string]: FormField<any> };
