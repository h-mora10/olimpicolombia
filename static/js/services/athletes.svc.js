/**
 * Created by danielordonez on 9/4/16.
 */
/**
 * Created by danielordonez on 9/4/16.
 */
(function (ng)
{
    var mod = ng.module('athletesModule');

    mod.service('athletesService', ['$http', 'athletesContext', function ($http, context) {
            this.fetchRecords = function () {
                console.log(context);
                return $http.get(context);
            };
            this.fetchRecordsBySport = function(sportId){
                console.log("Mira el api "+sportId);
                return $http.get("/sportJSON/"+sportId)     //TODO <--- no estoy muy seguro de este cuando definamos apis corregimos
            }
            this.fetchRecord = function (id) {
                return $http.get(context + "/" + id);
            };
            this.saveRecord = function (currentRecord) {
                if (currentRecord.id) {
                    return $http.put(context + "/" + currentRecord.id, currentRecord);
                } else {
                    console.log(currentRecord);
                    return $http.post(context, currentRecord);
                }
            };
            this.deleteRecord = function (id) {
                return $http.delete(context + "/" + id);
            };
        }]);
})(window.angular);