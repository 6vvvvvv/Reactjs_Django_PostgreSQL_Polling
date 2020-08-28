import axios from "axios";
import { add_option, alter_option } from "../actions/pollingActionCreator";

export const polling_tobackend = (optiondata) => {
  console.log("^^^^^^optiondata", optiondata);
  return (dispatch, getState) => {
    axios
      .post(
        "http://localhost:8000/api/polling/",
        { optiondata },
        { headers: { "Content-Type": "application/json" } }
      )
      .then((res) => {
        console.log("---------res", res.data);
        dispatch(alter_option(res.data));
      });
  };
};
