import {ALTER } from "./action-types/polling-actions";



export const alter_option = (payload) => ({
  type: ALTER,
  payload,
});
