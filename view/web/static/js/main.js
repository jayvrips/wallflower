
//import {createStore} from '/deps/redux.min';
//'use strict';
//const React = require('react')
//import React from 'https://unpkg.com/react@16/umd/react.development.js';
//import ReactDOM from 'react-dom';

const {createStore} = Redux;


const initialState = {
    users: []
}

function wallflowerApp(state, action) {
    if (typeof state === 'undefined') {
        return initialState;
    }

    switch (action.type) {
        case "INITIALIZE":
        default:
            return state;
    }
}

const store = createStore(wallflowerApp);

$(function() {
        store.dispatch({
            type: "INITIALIZE"
        });
    }
);

class User extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            users: null
        };
    }

    componentDidMount() {
        self = this
        $.ajax("http://192.168.136.3:8000/users",
            {
                success: function(data) {
                    self.setState({users: data});
                },
                error: function(xhr, textStatus, errorThrown) {
                    self.setState({users: textStatus});
                }
            }
        );
    }
    render() {
        var stuff = "Nothing yet";
        if (this.state.users)
            stuff = "Name: " + this.state.users[0].fullname;
        return React.createElement("div", null, stuff);
    }
}

