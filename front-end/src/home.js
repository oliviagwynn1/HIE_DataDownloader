import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import { styles } from './styling'
import ErrorMessage from './error';



class Home extends Component {
    state = {
        'loading': false,
        'player_id': [],
        'errorMessageOpen': false,
    };


    connectDevices = () => {
        let get_connectDevices = axios.get('http://127.0.0.1:5000/name');
        get_connectDevices.then( (data) => {
            this.setState({'player_id': [data.data.player_id]})
            if (data.data.status > 300) {
                console.log("Issue initializing device");
                this.setState({'errorMessageOpen': true})
            }
            else {
                this.props.view()
                console.log([data.data.player_id])
                console.log(data)
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