/**
 * Created by Diana on 8/26/16.
 */

 window.fbAsyncInit = function() {
    FB.init({
      appId      : '964171530358798',
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
    } /*else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } */else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      alert("Por favor ingrese sus credenciales");
    }
  }

  function createUserByFacebook(response) {

     FB.api('/me', function(response) {
        JSON.stringify(response);
    });
  }


