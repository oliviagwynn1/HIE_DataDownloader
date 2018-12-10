import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';


class ErrorMessage extends Component {


    render() {
        return (
            <Dialog
                open={this.props.open}
                onClose={this.props.close}>
                <DialogTitle>
                    {"No Devices Found"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Please check device connection and try again
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={this.props.close}
                        color="primary">
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        )
    }
}

export default ErrorMessage