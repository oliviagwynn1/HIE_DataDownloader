import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { styles } from './styling'
import ErrorMessage from './error';



class Home extends Component {
    state = {
        'errorMessage1': false,
        'errorMessage2': false,
        'errorMessage3': false,
    };


    connectDevices = () => {
        let get_connectDevices = axios.get('http://vcm-7335.vm.duke.edu:5005/api/send_device_info');
        get_connectDevices.then( (response) => {
            console.log(response)

            if (response.status === 210) {
                console.log("problem with local server");
                this.setState({'errorMessage1': true})
            }
            else if (response.status === 220) {
                console.log("No devices connected")
                this.setState({'errorMessage2': true })
            }
            else {
               this.props.data(response);
               this.props.view()
            }
        })
        .catch( (error) => {
            console.log("Unknown error")
            this.setState({'errorMessage3': true })
        })
        }


    render(){
        return (
            <div style={styles.viewStyle}>
                <Button
                    style={styles.connectButtonStyle}
                    variant="raised"
                    onClick={this.connectDevices}
                    label={"Connect to Devices"}
                    >
                    Connect to Devices
                </Button>
                <ErrorMessage
                    open={this.state.errorMessage1}
                    title={"An error occurred while accessing the local server"}
                    content={"Please refer to the server log at Main_Log.txt"}
                    close={() => this.setState({errorMessage1: false})}
                />
                <ErrorMessage style={styles.errorMessageStyle}
                    open={this.state.errorMessage2}
                    title={"No devices were found"}
                    content={"Please check connections and try again"}
                    close={() => this.setState({errorMessage2: false})}
                />
                 <ErrorMessage style={styles.errorMessageStyle}
                    open={this.state.errorMessage3}
                    title={"Unknown Error"}
                    content={"Please check all server and device connections"}
                    close={() => this.setState({errorMessage3: false})}
                />
            </div>
        )
    };
}

export default Home