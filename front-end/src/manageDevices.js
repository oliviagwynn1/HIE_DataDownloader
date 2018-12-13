import React, { Component } from 'react';
import { styles } from './styling';
import Button from '@material-ui/core/Button';
import axios from "axios";

class Devices extends Component {
    state = {
        data: this.props.data
    }

    handleChange = () => {
        this.setState({data: this.state.data})
    }


    uploadData = () => {

        const dataForUpload = {
            data: this.state.data
        };

        axios.post('http://vcm-7335.vm.duke.edu:5002/api/send_data', { dataForUpload })
            .then(res => {
            console.log(res);
            console.log(res.data);
        })
    }

    render(){
        console.log(this.props.data)
        console.log(this.state.data)
        console.log(this.props.players)
        return(
            <div style={styles.viewStyle}>
                <div onClick={this.handleChange}>
                this is where Olivia's table will go! wooooo
                </div>
                <Button
                    style={styles.connectButtonStyle}
                    variant="raised"
                    onClick={this.uploadData}
                    label={"Connect to Devices"}
                    >
                    Upload data
                </Button>

            </div>
        )
    }


}


export default Devices