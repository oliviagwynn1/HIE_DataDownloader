import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

export const theme = createMuiTheme({
  palette: {
      type:'light',
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
        "backgroundColor": "#F1F1F1",
        "text-align": "center",
        "height": "100vh"

    },
    "headerStyle": {
        "backgroundColor": "#282c34",
        "font-size": "2vh",
        "color": "white",
        "padding": "2.5vh",
    },
    "paperStyle": {
        "height": "75vh",
        "width": "75vh",
        "marginTop": "5vh",
        "display": "inline-block",
        "backgroundColor": "#f9f9f9",

    },
    "viewStyle": {
        "marginTop": "20vh",
        "font-size": "2vh",
    },
    "connectButtonStyle": {
        "font-size": "2vh"
    }

}