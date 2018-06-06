
//'use strict';
//const React = require('react')
//import React from 'https://unpkg.com/react@16/umd/react.development.js';
//import ReactDOM from 'react-dom';


const initialState = {
    users: []
}

function wallflowerApp(state, action) {
    if (typeof state === 'undefined') {
        return initialState
    }

    return state
}

$().ready() {
    const store = createStore(wallflowerApp)

}

class User extends React.Component {
    render() {
        return React.createElement("div", null, "blah");
    }
}

