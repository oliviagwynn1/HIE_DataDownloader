import React, { Component } from 'react';
import './App.css';
import Home from './home';
import { MuiThemeProvider} from '@material-ui/core/styles';

var styles = {
    "backgroundStyle": {
        "backgroundColor": "#222222",
        "color": "white",
        "padding": "20px",
        "height": "20px",

    },
    "headerStyle": {
        "marginBottom": "10px",
        "backgroundColor": "#222222",
        "height": "150px",
        "padding": "20px",
        "color": "white",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "flex-start",
    },
};

class App extends Component {
  render() {
    return (
        <MuiThemeProvider>
            <div style={styles.backgroundStyle}>
                <div style={styles.headerStyle}>
                Welcome to the client application for the DASHR
                </div>
                <Home/>
            </div>
        </MuiThemeProvider>
    );
  }
}

export default App;
