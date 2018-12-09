import React, { Component } from 'react';
import './App.css';
import Home from './home';
import { MuiThemeProvider} from '@material-ui/core/styles';
import { componentMap, viewIDs} from './component-map';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { changeView } from './actions/index';

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
            </div>
             {
            // Render the proper top level view based on the current viewID stored in redux:
            React.createElement(
                componentMap[this.props.viewID],
                {changeView: this.props.changeView, viewIDs},
            )
        }
        </MuiThemeProvider>
    );
  }
}

const mapDispatchToProps = dispatch => {
    return bindActionCreators({ changeView }, dispatch);
};

const mapStateToProps = state => {
    return {
        viewID: state.view.viewID,
    }
};

export default connect(mapStateToProps, mapDispatchToProps)(App);