import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import axios from 'axios';

class Home extends Component {

    getData = () => {
        axios.get('http://vcm-7335.vm.duke.edu:5002/api/send_enc_file').then((data)  => {
            console.log(data)
        }
        )
    };

    render(){
        return (
            <div>
                <Button variant="raised" label={"Test"} primary={true} onClick={this.getData} style={{margin:'20px'}}/>
            </div>
        )
    };
}

export default Home