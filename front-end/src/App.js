import React, { Component } from 'react';
import './App.css';
import Home from './home';
import Devices from './devices';
import { MuiThemeProvider} from '@material-ui/core/styles';



class App extends Component {
    state = {
        homeView: true,
        devicesView: false,
    };

    changeView = () => {
        this.setState({
            homeView: false
        })
    };


  render() {
    return (
        <MuiThemeProvider>
            <div className={"App-header"}>
                Welcome to the client application for the DASHR
            </div>
            <div className={"App"}>
                {
                    (this.state.homeView) ? <Home view={this.changeView}/> : <Devices/>
                }


            </div>
        </MuiThemeProvider>
    );
  }
}

export default App
