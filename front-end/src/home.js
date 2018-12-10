import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
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
            <div className="home-button">
                <Button
                    variant="raised"
                    color={"primary"}
                    onClick={this.connectDevices}
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