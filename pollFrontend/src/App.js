import React, { Component } from "react";
import GithubCorner from "react-github-corner";
import "./App.css";
import ProgressBar from "react-bootstrap/ProgressBar";


class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      pollQuestion: "Which one would you like choose?",
      pollAnswers: [
        { option: "Angular", vote: 0 },
        { option: "React", vote: 0 },
        { option: "Vue", vote: 0 }
      ],
      totalVotes: 0
    };
  }

  // In case control through backend
  // async componentDidMount() {
  //   try {
  //     const res1 = await fetch("http://127.0.0.1:8000/api/option"); // fetching the data from api, before the page loaded
  //     const polloption = await res1.json();
  //     let polloption1=JSON.parse(JSON.stringify(polloption))

  //     const res2 = await fetch("http://127.0.0.1:8000/api/title"); 
  //     const polltitle = await res2.json();
      
  //     this.setState({
  //       pollAnswers: polloption1,
  //       pollQuestion:polltitle[0]["title"]
  //     });
  //   } catch (e) {
  //     console.log(e);
  //   }
  // }

  //tranfer id from method bind id in main
  vote = id => {
    //add
    let newPollAnswers = this.state.pollAnswers.map((el)=>(el));
    newPollAnswers[id].vote++;

    let tmp = this.state.pollAnswers.map(el => el.vote);
    let newtotalVotes = tmp.reduce((total, amount) => total + amount);

    this.setState({
      pollAnswers: newPollAnswers,
      totalVotes: newtotalVotes
    });
  };

  render() {
    const { pollAnswers } = this.state;
    var greenBarPer = parseFloat(
      (pollAnswers[0].vote /
        (pollAnswers[0].vote + pollAnswers[1].vote + pollAnswers[2].vote)) *
        100
    ).toFixed(2);
    var yellowBarPer = parseFloat(
      (pollAnswers[1].vote /
        (pollAnswers[0].vote + pollAnswers[1].vote + pollAnswers[2].vote)) *
        100
    ).toFixed(2);
    var redBarPer = parseFloat(
      (pollAnswers[2].vote /
        (pollAnswers[0].vote + pollAnswers[1].vote + pollAnswers[2].vote)) *
        100
    ).toFixed(2);

    return (
      <div className="container">
        {/* {this.state.pollAnswers} */}
        <div>
          <div>
            <div className="question">
              <p>{this.state.pollQuestion}</p>
            </div>
            <div>
              {this.state.pollAnswers.map((el, id) => (
                <div>
                  <button
                    key={id}
                    type="button"
                    className="btn btn-outline-primary"
                    onClick={this.vote.bind(this, id)}
                  >
                    {el.option}
                  </button>
                
                </div>
              ))}
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

        <GithubCorner
          href="https://github.com/6vvvvvv/Reactjs_Django_Poll"
          bannerColor="#303030"
          size={80}
          direction="right"
        />
      </div>
    );
  }
}

export default App;
