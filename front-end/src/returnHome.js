import React, { Component } from 'react';
import Icon from '@material-ui/core/Icon';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/ArrowBackRounded';
import { styles, theme } from './styling';

class ReturnToHome extends Component {

    handleClick = () => {
        this.props.returnHome()
        }


    render(){
        console.log(this.state)
        return (
            <div>
                <IconButton onClick={this.handleClick}>
                    <DeleteIcon
                        style={styles.backIconStyle}
                    />
                </IconButton>
                <div style={styles.backIconTextStyle}>
                    Home
                </div>
            </div>


        )
    }
}

export default ReturnToHome