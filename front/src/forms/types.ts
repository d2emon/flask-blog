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

export interface ChangePasswordFormData {
  oldPassword: FormField<string>,
  newPassword: FormField<string>,
}

export interface LoginFormData {
  username: FormField<string>,
  password: FormField<string>,
  rememberMe: FormField<boolean>,
}

export interface NewLoginFormData {
  username: FormField<string>,
  password: FormField<string>,
}

export interface RegistrationFormData {
  username: FormField<string>,
  email: FormField<string>,
  password: FormField<string>,
  password2: FormField<string>,
}
