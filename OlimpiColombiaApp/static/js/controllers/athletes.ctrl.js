/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng) {
    var mod = ng.module('athletesModule');

    mod.controller('AthletesCtrl', ['$scope', 'athletesService', function ($scope, svc) {
            $scope.athletesRecords = [];

            this.fetchRecords = function () {
                return svc.fetchRecordsBySport().then(function (response) {
                    $scope.athletesRecords = response.data;

                    return response;
                });
            };

            this.fetchRecords();
        }]);
})(window.angular);