import React, { Component } from 'react';
import './App.css';
import Home from './home';
import Devices from './devices';
import Paper from '@material-ui/core/Paper';
import { styles, theme } from './styling'
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
        <MuiThemeProvider theme={theme}>
            <div style={styles.backgroundStyle}>
                <div style={styles.headerStyle}>
                    Welcome to the client application for the DASHR
                </div>
                <Paper style={styles.paperStyle}>
                {
                    (this.state.homeView) ? <Home view={this.changeView}/> : <Devices/>
                }
                </Paper>

            </div>
        </MuiThemeProvider>
    );
  }
}

export default App
