/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng) {
    var mod = ng.module('athletesModule');

    mod.controller('AthletesCtrl', ['$scope','$cookies', 'athletesService','$http', function ($scope,$cookies, svc, $http) {
            $scope.athletesRecords = [];
            $scope.sport={name:"Deporte",img_url:""};
            $scope.booleano = true;

            $scope.fetchRecords = function () {
                return svc.fetchRecordsBySport($cookies.get('sport')).then(function (response) {
                    $scope.athletesRecords = response.data.athletes;
                    $scope.sport = response.data.sport;
                    loadAllvideos();
                    return response;
                });
            };
            function loadAllvideos(){
                for(var i = 0; i<$scope.athletesRecords.length;i++)
                {
                    $scope.loadVideo($scope.athletesRecords[i].id);
                }
            }
            $scope.fetchRecords();
            $scope.loadVideo = function(some)
            {
                if($scope.booleano) {
                    $scope.booleano = true;
                    console.log("mrimairmaimraimr" + some);
                    console.log("hola jaime");
                     $http.get("/calendar/athlete/video/" + some + "/").success(
                         function (data) {
                             console.log(data);
                             var srcCont = document.getElementById('vidsource' + some);
                             srcCont.src = 'https://s3-us-west-2.amazonaws.com/olimpicolombiag4/media/' + data.video_url;
                             var vidCont = document.getElementById('vidcont' + some);
                             vidCont.load();
                         });
                }
            }

        }]);
})(window.angular);