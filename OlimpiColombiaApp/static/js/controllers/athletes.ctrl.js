/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng) {
    var mod = ng.module('athletesModule');

    mod.controller('AthletesCtrl', ['$scope','$cookies', 'athletesService', function ($scope,$cookies, svc) {
            $scope.athletesRecords = [];
            $scope.sport={name:"Deporte",img_url:""};

            this.fetchRecords = function () {
                 //TODO falta pasar el id
                return svc.fetchRecordsBySport($cookies.get('sport')).then(function (response) {
                    $scope.athletesRecords = response.data.athletes;
                    $scope.sport = response.data.sport;
                    return response;
                });
            };
            this.fetchRecords();

        }]);
})(window.angular);