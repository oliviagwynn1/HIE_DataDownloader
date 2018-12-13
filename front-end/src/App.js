import React, { Component } from 'react';
import './App.css';
import Home from './home';
import Devices from './manageDevices';
import Paper from '@material-ui/core/Paper';
import { styles, theme } from './styling'
import { MuiThemeProvider} from '@material-ui/core/styles';




class App extends Component {
    state = {
        homeView: true,
        devicesView: false,
        dashrData: []
    };

    changeView = () => {
        this.setState({
            homeView: false
        })
    };

    getDashrData = (resp) => {
        this.setState({
            dashrData: [resp],
            players: [resp.data.Players],
            mountPoints: [resp.data.Mount_Points],
            numFiles: [resp.data.Num_Files],
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
                    (this.state.homeView)
                        ? <Home view={this.changeView}
                              data={this.getDashrData}/>
                        : <Devices data={this.state.dashrData} players={this.state.players}/>
                }
                </Paper>

            </div>
        </MuiThemeProvider>
    );
  }
}

export default App
