//- require('offline-plugin/runtime').install();  // offline service-worker plugin


// ------------------------------------- Libs -------------------------------------
import 'jquery'; window.$ = $; window.jQuery = jQuery;
import 'lodash'; window._ = _;
import 'vue'; import Vue from 'vue'; window.Vue = Vue;
import 'bootstrap';
import 'jquery-confirm';
import 'reconnecting-websocket';
import 'promise-polyfill/src/polyfill';

import 'fullcalendar';
import 'bootstrap-datepicker';
import 'bootstrap-grid';

import 'waypoints/lib/jquery.waypoints.js';
// import 'waypoints'; import Waypoint from 'waypoints'; window.Waypoint = Waypoint;

import 'typeface-roboto-condensed';
import 'typeface-roboto';
// import 'material-design-icons';
import '@fortawesome/fontawesome';
import '@fortawesome/fontawesome-free-brands';


// ---------------------------------- Modules -------------------------------------
// import '../scss/index.scss';

import './datepicker-init';
import './feedback';
import './header';
import './clockpicker';
import './vue-env';

// import './ws'
import './common';
