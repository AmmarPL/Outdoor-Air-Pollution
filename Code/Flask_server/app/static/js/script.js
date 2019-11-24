$("#addD").click(function () {

    var latitude = $('#lat').val();
    var longitude = $('#lon').val();
    var todo = $('#todo').val();
    if (latitude != "" && longitude != "" && todo != "") {
        $.ajax({
            url: 'http://0.0.0.0:5000/loc/' + todo,
            method: 'POST',
            data: {
                lat: latitude,
                lon: longitude
            },
            success: function (response) {
                console.log(response);
                res();
            },
            error: function (response) {
                console.log(response);
                alert("An error occured");
                $("#demo").html(response.responseText);
            }
        });
    }
});

$("#del_loc").submit(function (e) {
    e.preventDefault();

    var ID = $("#ID").val();
    if(!isNaN(ID)) {
        $.ajax({
            url: 'http://0.0.0.0:5000/loc/del',
            method: 'GET',
            data: {
                id: ID
            },
            success: function (response) {
                console.log(response);
                res();
            },
            error: function(response) {
                console.log(response);
                alert("An error occured");
            }
        });
    }
});

function res() {
    $('#add_loc').trigger('reset');
    $('#del_loc').trigger('reset');
}

// function tryGeolocation() {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(showPosition,showError,
//           {
//             enableHighAccuracy : true,
//             timeout : 10000, // 10s
//             //maximumAge : 0
//           }
//         );
//     }
//     else {
//       $("#demo").html("Geolocation is not supported by this browser.");
//     }
// }
// function showPosition(position) { 
//     $('#lat').val(position.coords.latitude);
//     $('#lon').val(position.coords.longitude);
//     $("#demo").html("Latitude: " + position.coords.latitude + 
//     "<br>Longitude: " + position.coords.longitude);    
// }
// function showError(error) {
//     switch(error.code) {
//         case error.PERMISSION_DENIED:
//             $("#demo").html("User denied the request for Geolocation.")
//             break;
//         case error.POSITION_UNAVAILABLE:
//             $("#demo").html("Location information is unavailable.")
//             break;
//         case error.TIMEOUT:
//             $("#demo").html("The request to get user location timed out.")
//             break;
//         case error.UNKNOWN_ERROR:
//             $("#demo").html("An unknown error occurred.")
//             break;
//     }
// }

var apiGeolocationSuccess = function(position) {
    alert("API geolocation success!\n\nlat = " + position.coords.latitude + "\nlng = " + position.coords.longitude);
};

var tryAPIGeolocation = function() {
    jQuery.post( "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyAStz8lNTf06qq-puoq1AOAOz9GLqa7bVw", function(success) {
        apiGeolocationSuccess({coords: {latitude: success.location.lat, longitude: success.location.lng}});
  })
  .fail(function(err) {
    alert("API Geolocation error! \n\n"+err);
  });
};

var browserGeolocationSuccess = function(position) {
    alert("Browser geolocation success!\n\nlat = " + position.coords.latitude + "\nlng = " + position.coords.longitude);
};

var browserGeolocationFail = function(error) {
  switch (error.code) {
    case error.TIMEOUT:
      alert("Browser geolocation error !\n\nTimeout.");
      break;
    case error.PERMISSION_DENIED:
      if(error.message.indexOf("Only secure origins are allowed") == 0) {
        tryAPIGeolocation();
      }
      break;
    case error.POSITION_UNAVAILABLE:
      alert("Browser geolocation error !\n\nPosition unavailable.");
      break;
  }
};

var tryGeolocation = function() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        browserGeolocationSuccess,
      browserGeolocationFail,
      {maximumAge: 50000, timeout: 20000, enableHighAccuracy: true});
  }
};
