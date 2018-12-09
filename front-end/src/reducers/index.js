import { combineReducers } from 'redux';
import ViewReducer from './view-reducer';
const rootReducer = combineReducers({
    view: ViewReducer,
});
export default rootReducer;
