/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng) {
    var mod = ng.module('sportsModule');

    mod.controller('SportsCtrl', ['$scope', 'sportsService', function ($scope, svc) {
            $scope.sportsRecords = [];

            this.fetchRecords = function () {

                return svc.fetchRecords().then(function (response) {
                    $scope.sportsRecords = response.data.sports;

                    return response;
                });
            };

            this.fetchRecords();
        }]);
})(window.angular);