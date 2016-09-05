/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng) {
    var mod = ng.module('sportsModule');

    mod.controller('SportsCtrl', ['$cookies','$scope', 'sportsService', function ($cookies,$scope, svc) {
            $scope.sportsRecords = [];
            this.fetchRecords = function () {

                return svc.fetchRecords().then(function (response) {
                    $scope.sportsRecords = response.data.sports;

                    return response;
                });
            };

            this.fetchRecords();
        $scope.setActualSport = function(sportId) {
            console.log("Este entra:"+sportId);
                  $cookies.put('sport',sportId)  ;
            console.log($cookies.get('sport'));
                }
        }]);
})(window.angular);