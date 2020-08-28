import axios from "axios";
import { alter_option } from "../actions/pollingActionCreator";

export const polling_tobackend = (optiondata) => {
  return (dispatch, getState) => {
    axios
      .post(
        "http://localhost:8000/api/polling/",
        { optiondata },
        { headers: { "Content-Type": "application/json" } }
      )
      .then((res) => {
        console.log("---------polling_tobackend", res.data);
        dispatch(alter_option(res.data));
      });
  };
};

export const polling_initial = () => {
  return (dispatch, getState) => {
    axios.get("http://localhost:8000/api/initial/").then((res) => {
      console.log("---------polling_initial", res.data);
      dispatch(alter_option(res.data));
    });
  };
};
