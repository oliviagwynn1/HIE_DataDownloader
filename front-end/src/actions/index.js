export const CHANGE_VIEW = 'CHANGE_VIEW';

export function changeView(viewID) {
    return {
        type: CHANGE_VIEW,
        viewID
    }
}