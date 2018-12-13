import React, { Component } from 'react';
import './App.css';
import Home from './home';
import Devices from './Devices';
import ManageDevices from './manageDevices'
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
            homeView: false,
            devicesView: true
        })
    };

    changeToVerView = () => {
        this.setState({
            devicesView: false
        })
    };

    getDashrData = (resp) => {
        this.setState({
            dashrData: resp,
            players: resp.data.Players,
            mountPoints: resp.data.Mount_Points,
            numFiles: resp.data.Num_Files,
        })
    };

    getC = () => {
     if ((this.state.homeView===true) && (this.state.devicesView===false)) {
                            return (<Home
                                        view={this.changeView}
                                        data={this.getDashrData}/>)
                        } else if ((this.state.homeView===false) && (this.state.devicesView===true)) {
                            return (<Devices
                                        data={this.state.dashrData}
                                        players={this.state.players}
                                        mountPoints={this.state.mountPoints}
                                        verificationData={this.verificationData}
                                        view1 = {this.changeToVerView}/>)
                        } else {
                            return(<ManageDevices
                                        verData={this.state.verData}/>)
                        }
                    }


    verificationData = (resp) => {
        this.setState({
            verData: resp.data
        })
    };



  render() {
      console.log(this.state)
    return (
        <MuiThemeProvider theme={theme}>
            <div style={styles.backgroundStyle}>
                <div style={styles.headerStyle}>
                    Welcome to the client application for the DASHR
                </div>
                <Paper style={styles.paperStyle}>
                    {this.getC()}

                </Paper>

            </div>
        </MuiThemeProvider>
    );
  }
}

export default App
