/**
 * Created by Diana on 8/26/16.
 */

window.fbAsyncInit = function() {
    FB.init({
        appId      : '964168440359107',
        xfbml      : true,
        version    : 'v2.7'
    });
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


function checkLoginState() {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    })
}

function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
        // Logged into your app and Facebook.
        createUserByFacebook(response);
        document.getElementById("normalLoginButton").style.visibility = "hidden";
        document.getElementById("normalLogoutButton").style.visibility = "hidden";
        document.getElementById("registerButton").style.visibility = "hidden";
    } /*else if (response.status === 'not_authorized') {
     // The person is logged into Facebook, but not your app.
     document.getElementById('status').innerHTML = 'Please log ' +
     'into this app.';
     } */else {
        document.getElementById("normalLoginButton").style.visibility = "visible";
        document.getElementById("normalLogoutButton").style.visibility = "visible";
        document.getElementById("registerButton").style.visibility = "visible";
        // The person is not logged into Facebook, so we're not sure if
        // they are logged into this app or not.
        alert("Por favor ingrese sus credenciales");
    }
}

function checkFacebookStatus(){
    FB.getLoginStatus(function(response) {

        if(response.status === 'connected'){
            alert("connected");
            document.getElementById
            return true;
        }
        else{
            alert("disconnected");
            return false;
        }

    })
}

function createUserByFacebook(response) {

    FB.api('/me',{fields: 'name,first_name,last_name,email'}, function(response) {

        $.ajax({
            method: "GET",
            url: 'student/'+response.id,
                        statusCode: {
                            200: function() {
                                console.log( "OK" );
                                location.reload()
                            },
                            400: function() {
                                console.log( "page bad request" );
                            },
                            403: function() {
                                alert ("Acceso Prohibido")
                            },
                            404: function() {
                                console.log( "page not found" );
                                var csrftoken = getCookie('csrftoken');
                                $.ajax({
                                     beforeSend: function(xhr, settings) {
                                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                                        }
                                    },
                                    method:"POST",
                                    url: "accounts/registration/",
                                    data: JSON.stringify(response)
                                })
                                .done(function (response) {
                                    alert ("registro exitoso")
                                    location.reload()

                                })
                                .fail(function (response) {
                                    alert ("falló registro")
                                })
                            }
                        }
        })
    });
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}




