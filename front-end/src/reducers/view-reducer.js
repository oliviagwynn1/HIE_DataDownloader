import { CHANGE_VIEW } from '../actions/index';
import { viewIDs } from "../component-map";

export default function(state = {viewID: viewIDs.home}, action) {
    switch(action.type) {
        case CHANGE_VIEW:
            return Object.assign({}, state, {viewID: action.viewID});
    }
    return state;
}
