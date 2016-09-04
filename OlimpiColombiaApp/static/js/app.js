/**
 * Created by danielordonez on 9/4/16.
 */
var mysoApp = angular.module('OlimpiColombiaApp', [
    'ui.router',
    'sportsModule',
    'athletesModule'
]);

mysoApp.config(['$stateProvider', '$urlRouterProvider', '$locationProvider',
    function($stateProvider, $urlRouterProvider, $locationProvider) {
        $urlRouterProvider
            .otherwise('/');
    }
]);