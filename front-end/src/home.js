import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';
import ErrorMessage from './error';
import ChangeView from './actions';



class Home extends Component {
    state = {
        'loading': false,
        'player_id': [],
        'errorMessageOpen': false,
    };


    connectDevices = () => {
        let get_connectDevices = axios.get('http://vcm-7335.vm.duke.edu:5002/api/send_enc_file');
        this.setState({loading: true});
        get_connectDevices.then( (data) => {
            this.setState({'player_id': [data.data.player_id]})


            if (data.data.status > 300) {
                console.log("Issue initializing device");
                this.setState({'errorMessageOpen': true})
            }
            else {
                this.ChangeView()
                console.log([data.data.player_id])
                console.log(data)
                console.log(this.state.devices)
                console.log(this.state.home)


            }

        })}


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