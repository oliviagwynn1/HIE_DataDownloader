import React, { Component } from 'react';
import { styles } from './styling';

class ManageDevices extends Component {

    render(){
        console.log(this.props.data)
        console.log(this.props.players)
        return(
            <div>
                <div style={styles.viewStyle}>

                this is where Olivia's table will go! wooooo

                </div>
            </div>
        )
    }


}


export default ManageDevices