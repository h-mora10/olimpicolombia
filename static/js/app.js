/**
 * Created by danielordonez on 9/4/16.
 */
var OlimpiColombiaApp = angular.module('OlimpiColombiaApp', [
    'ngRoute',
    'sportsModule',
    'athletesModule',
    'ngCookies'
]);

OlimpiColombiaApp.config([ '$routeProvider',
    function( $routeProvider) {
        $routeProvider
            .otherwise('/');
    }
]);