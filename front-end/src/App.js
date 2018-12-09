import React, { Component } from 'react';
import './App.css';
import Home from './home';
import { MuiThemeProvider} from '@material-ui/core/styles';



class App extends Component {
  render() {
    return (
        <MuiThemeProvider>
            <div className={"App-header"}>
                Welcome to the client application for the DASHR
            </div>
            <div className={"App"}>
                <Home/>
            </div>
        </MuiThemeProvider>
    );
  }
}

export default App;
