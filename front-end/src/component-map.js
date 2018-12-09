import Devices from './devices';
import Home from './home';


// viewIDs represent the identifiers of various view components
const viewIDs = {
    home: "HOME",
    devices: "DEVICES",
};

// componentMap maps viewIDs to corresponding components
const componentMap = {
    [viewIDs.home]: Home,
    [viewIDs.devices]: Devices,
};

export {
    componentMap,
    viewIDs,
};