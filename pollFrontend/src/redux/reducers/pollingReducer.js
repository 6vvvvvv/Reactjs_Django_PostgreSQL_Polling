import { ALTER } from "../actions/action-types/polling-actions";

const initialState = {
  pollingAnswers: [
    { option: "0", vote: 0, rate: 0 },
    { option: "1", vote: 0, rate: 0 },
    { option: "2", vote: 0, rate: 0 },
  ],

  totalVotes: 0,
};

export default (state = initialState, action) => {
  switch (action.type) {
    case ALTER:
      const newpollingAnswers = state.pollingAnswers.map((item, id) => {
        action.payload.tofrontend.map((t) => {
          if (id === t.id) {
            if (
              item.option !== t.option ||
              item.vote !== t.vote ||
              item.rate !== t.rate
            ) {
              item.option = t.option;
              item.vote = t.vote;
              item.rate = t.rate;
            }
          }
        });
        return item;
      });

      return {
        ...state,
        pollingAnswers: newpollingAnswers,
      };

    default:
      return state;
  }
};

export const getPollingAnswers = (state) => state.pollingAnswers;
