import React, { Component } from 'react';
import { styles } from './styling'

class Devices extends Component {

    render(){
        console.log(this.props.data)
        console.log(this.props.players)
        return(
            <div style={styles.viewStyle}>
                this is where Olivia's table will go! wooooo

            </div>
        )
    }


}


export default Devices