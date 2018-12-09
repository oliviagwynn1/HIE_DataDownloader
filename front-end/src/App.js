import React, { Component } from 'react';
import './App.css';
import Home from './home';
import { MuiThemeProvider} from '@material-ui/core/styles';
import { componentMap, viewIDs} from './component-map';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { changeView } from './actions/index';



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