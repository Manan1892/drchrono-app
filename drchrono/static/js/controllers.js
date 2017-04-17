(function() {
    "use strict";
    var App = angular.module("App.controllers", []).run(function($rootScope,$http,$cookies) {
        
    });
    
    

    //Main controller
    App.controller("MainCtrl", ["$scope","$http","$location","$localStorage", function ($scope,$http,$location,$localStorage){
              

            


    }]);

    App.controller("HomeCtrl", ["$scope","$http","$location","$localStorage", function ($scope,$http,$location,$localStorage){
              $scope.dateflag = false;

              var time = new Date();
              var hours = time.getHours();
              time = time.toLocaleString('en-US', { hour: 'numeric',minute:'numeric', hour12: true });
              if(time.indexOf('PM') > -1){
              	if(hours >= 5){
              		$http({method:"get",
	                   url:"/sendmail",
	                   headers: {'Content-Type': 'application/x-www-form-urlencoded'}
	                   }).success(function(resp){
	                    	console.log(resp.message);
	                  });
              		
              	}

              }

				
              $http({method:"get",
                url:"/Home",
                 headers: {'Content-Type': 'application/x-www-form-urlencoded'}
                 }).success(function(resp){
                  if(resp.status == "Failed"){
                    $location.path("/");
                  }
                  else{
                    $localStorage.user_id = resp.username;
                    $scope.date = resp.date;

                    $scope.patients = resp.patients;
                  }

              });
                 $scope.getallpatients = function(){
                  $scope.dateflag = true;
                 }
                 
                 $scope.getpatients = function(){
                  $scope.dateflag = false;
                 }

                 $scope.sendwishes = function(patients){
	                  $http({method:"get",
	                   url:"/sendmail",
	                   headers: {'Content-Type': 'application/x-www-form-urlencoded'}
	                   }).success(function(resp){
	                    	alert(resp.message);
	                  });

                 }
                 $scope.getpatientinfo = function(patient){
                 	$scope.fname = patient.first_name;
                 	$scope.lname = patient.last_name;
                 	$scope.dob = patient.date_of_birth;
                 	$scope.pic = patient.patient_photo;

                 }

            


    }]);

    
  
        
  
}());
