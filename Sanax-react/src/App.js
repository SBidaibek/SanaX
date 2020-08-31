import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Signup from './components/reg/Signup';
import SignupStudent from './components/reg/SignupStudent';
import SignupTutor from './components/reg/SignupTutor';
import StudentIndex from './components/student/index';

import { Link } from 'react-router-dom';

import './App.css';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="App">
          <Route exact path="/" render={props => (
            <React.Fragment>
              <h1>App</h1>
              <Link to="/signup">Sign up</Link>
            </React.Fragment>
          )} />

          <Route path="/signup" component={Signup} />

          <Route path="/student/:userId" component={StudentIndex} />
        </div>
      </Router>
    );
  }
}

export default App;
