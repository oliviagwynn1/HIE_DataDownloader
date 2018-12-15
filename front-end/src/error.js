import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import Typography from '@material-ui/core/Typography';


const styles = theme => ({
  paper: {
    "height": "25vh",
  },
});

const ErrorMessage = props => {
        return (
            <Dialog
                maxWidth={"md"}
                fullWidth={true}
                classes={{paper: props.classes.paper}}
                open={props.open}
                onClose={props.close}>
                <DialogTitle>
                    {props.title}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        {props.content}
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button
                        onClick={props.close}
                        color="primary">
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        )
    };

    ErrorMessage.propTypes = {
        onClose: PropTypes.func.isRequired, // function called when the user wants to close the dialog
        open: PropTypes.bool.isRequired, // bool to indicate whether the dialog is open or not right now
        title: PropTypes.string.isRequired, // title string
        content: PropTypes.string.isRequired, // content of the dialog

    };
export default withStyles(styles)(ErrorMessage)