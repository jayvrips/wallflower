
//import {createStore} from '/deps/redux.min';
//'use strict';
//const React = require('react')
//import React from 'https://unpkg.com/react@16/umd/react.development.js';
//import React, { Component } from '/deps/react.development.js';
//import ReactDOM from 'react-dom';

const {createStore} = Redux;


function wallflowerReducer(state, action) {
    switch (action.type) {
        case "INITIALIZE":
            return {
                users: []
            };

        case "GET_USERS":
            // TODO: if we've already got users in the store, return it
            // otherwise...
            return [...state, {users: get_users()}];

        default:
            return state;
    }
}

function get_users(state) {
    $.ajax("http://192.168.136.3:8000/users",
        {
            success: function(data) {
                return data;
            },
            error: function(xhr, textStatus, errorThrown) {
                return state;
            }
        }
    );
}

const store = createStore(wallflowerReducer);

$(function() {
        store.dispatch({
            type: "INITIALIZE"
        });
    }
);


