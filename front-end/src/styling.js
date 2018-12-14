import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

export const theme = createMuiTheme({
  palette: {
      primary: {
      main: '#232F34',
    },
    secondary: {main: "#03DAC5"}
  },
  typography: {
    // Use the system font instead of the default Roboto font.
    fontFamily: [
      'sans-serif',
    ].join(','),
  },

});


export var styles = {
    "backgroundStyle":{
        "height": "100vh",
        "backgroundColor":"#344955"

    },
    "headerStyle": {
        "text-align": "center",
        "font-size": "2vh",
        "color": "white",
        "padding": "2.5vh",
        "backgroundColor":"#232F34"
    },
    "paperStyle": {
        "text-align": "center",
        "height": "75vh",
        "width": "75vh",
        "marginTop": "5vh",
        "display": "inline-block",
        "backgroundColor":"#344955",

    },
    "viewStyle": {
        "text-align": "center",
    },
    "connectButtonStyle": {
        "text-align": "center",
        "font-size": "3vh",
        "backgroundColor":"#03DAC5",
        "marginTop": "20vh"

    },
    "backIconStyle": {
        "font-size": "3vh",
        "color":"#03DAC5",
        "marginLeft": "1vh",
    },

    "backIconTextStyle": {
        "font-size": "2vh",
        "color":"#232F34",
        "marginLeft": "1vh",
    }

}