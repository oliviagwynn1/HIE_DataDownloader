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
        "text-align": "center",
        "height": "100vh",
        "backgroundColor":"#344955"

    },
    "headerStyle": {
        "font-size": "2vh",
        "color": "white",
        "padding": "2.5vh",
        "backgroundColor":"#232F34"
    },
    "paperStyle": {
        "height": "75vh",
        "width": "75vh",
        "marginTop": "5vh",
        "display": "inline-block",
        "backgroundColor":"#344955",

    },
    "viewStyle": {
        "marginTop": "20vh",
        "font-size": "2vh",
    },
    "connectButtonStyle": {
        "font-size": "3vh",
        "backgroundColor":"#03DAC5"

    }

}