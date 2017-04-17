(function() {

  "use strict";

  var App = angular.module("App", [
    "App.controllers",
    "ngRoute",

    "ngCookies",
    "ngResource",
    'ngStorage'

    ]);

  App.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    //$locationProvider.html5Mode(true);
    $routeProvider
      .when('/', {
           templateUrl: 'static/view/home.html',
           controller:'MainCtrl'
          
      })
      .when('/home', {
           templateUrl: 'static/view/form2.html',
           controller:'HomeCtrl',
          
      })
	  
          
      .otherwise({ redirectTo: '/' });
      
  }]);
 
App.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

}());