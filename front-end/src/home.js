import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { styles } from './styling'
import ErrorMessage from './error';



class Home extends Component {
    state = {
        'data':[] ,
        'errorMessageOpen': false,
    };


    connectDevices = () => {
        let get_connectDevices = axios.get('http://vcm-7335.vm.duke.edu:5005/api/send_device_info');
        get_connectDevices.then( (data) => {
            this.setState({'data': data.data})
            if (data.data.status > 300) {
                console.log("Issue initializing device");
                this.setState({'errorMessageOpen': true})
            }
            else {
                this.props.view()
                console.log(this.state.data.Num_Files)
                console.log(data.data.Players)
                console.log(this.props.view)
            }
        })
        .catch( (error) => {
            this.setState({errorMessageOpen: true})
            console.log(this.state.homeView)
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
                    open={this.state.errorMessageOpen}
                    close={() => this.setState({errorMessageOpen: false})}
                />
            </div>
        )
    };
}

export default Home