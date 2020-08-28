import React, { Component } from "react";
import GithubCorner from "react-github-corner";
import "./App.css";
import ProgressBar from "react-bootstrap/ProgressBar";
import { connect } from "react-redux";
import { polling_tobackend } from "./redux/thunk/pollingThunk";
import { getPollingAnswers } from "./redux/reducers/pollingReducer";
// import EditableLabel from 'react-inline-editing';

class App extends Component {
  constructor(props) {
    super(props);
    this.inputBlur = React.createRef();
    this.state = {
      count: 0,
      text: "",
      totalVotes: 0,
      isEdited: false,
      editContent: undefined,
      pollQuestion: "Which one would you like choose?",
      changeContent: "",
    };
  }

  vote = (id) => {
    console.log("vote", id);
  };

  inputchange = (selectid) => {
    this.setState({
      count: this.state.count + 1,
      isEdited: !this.state.isEdited,
      editContent: selectid,
    });

    if (this.state.count % 2) {
      this.setState((prevState) => ({
        pollingAnswers: prevState.pollingAnswers.map((item, id) =>
          id === selectid ? { ...item, option: this.state.changeContent } : item
        ),
      }));
    }
  };

  textChange = (e) => {
    this.setState({
      text: e.target.value,
      changeContent: e.target.value,
    });
  };
  s;

  render() {
    console.log("---------editContent", this.state.editContent);
    console.log("*********isEdited", this.state.isEdited);
    console.log("---------changecontent", this.state.changeContent);
    console.log("*********pollanswer", this.props.pollingAnswers);

    const { pollingAnswers } = this.props;
    var greenBarPer = parseFloat(
      (pollingAnswers[0].vote /
        (pollingAnswers[0].vote +
          pollingAnswers[1].vote +
          pollingAnswers[2].vote)) *
        100
    ).toFixed(2);
    var yellowBarPer = parseFloat(
      (pollingAnswers[1].vote /
        (pollingAnswers[0].vote +
          pollingAnswers[1].vote +
          pollingAnswers[2].vote)) *
        100
    ).toFixed(2);
    var redBarPer = parseFloat(
      (pollingAnswers[2].vote /
        (pollingAnswers[0].vote +
          pollingAnswers[1].vote +
          pollingAnswers[2].vote)) *
        100
    ).toFixed(2);

    return (
      <div className="container">
        <div>
          <div>
            <div className="question">
              <p>{this.state.pollQuestion}</p>
            </div>
            <div>
              {this.props.pollingAnswers.map((item, id) => {
                return (
                  <div key={id}>
                    {this.state.isEdited && id === this.state.editContent ? (
                      <input
                        ref={this.inputBlur}
                        className="input"
                        type="text"
                        value={this.state.text}
                        onChange={this.textChange}
                        placeholder="Enter new option..."
                      ></input>
                    ) : (
                      <button
                        key={id}
                        type="button"
                        className="btn btn-outline-primary"
                        onClick={this.props.polling_tobackend.bind(this, id)}
                      >
                        {item.option}
                      </button>
                    )}

                    <span>
                      <i
                        className="fas fa-cogs"
                        onClick={this.inputchange.bind(this, id)}
                      ></i>
                    </span>
                  </div>
                );
              })}
            </div>
          </div>
          <p>Total Vote : {this.state.totalVotes}</p>
        </div>
        <hr></hr>
        <div className="progess">
          <div>
            <ProgressBar
              animated
              striped
              variant="success"
              now={greenBarPer}
              label={`${greenBarPer}%`}
            />
            <ProgressBar
              animated
              striped
              variant="warning"
              now={yellowBarPer}
              label={`${yellowBarPer}%`}
            />
            <ProgressBar
              animated
              striped
              variant="danger"
              now={redBarPer}
              label={`${redBarPer}%`}
            />
          </div>
        </div>
        <button onClick={this.props.polling_tobackend.bind(this, "test")}>
          test
        </button>
        <GithubCorner
          href="https://github.com/6vvvvvv/Reactjs_Django_Polling"
          bannerColor="#303030"
          size={80}
          direction="right"
        />
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  pollingAnswers: getPollingAnswers(state),
});

const mapDispatchToProps = (dispatch) => ({
  polling_tobackend: (optiondata) => dispatch(polling_tobackend(optiondata)),
});
export default connect(mapStateToProps, mapDispatchToProps)(App);
