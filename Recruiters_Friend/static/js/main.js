$(document).ready(function(){
	$('button#submit').click(function(event){
		event.preventDefault();
		//$("div#jd_description_append").html($('textarea').val());// this can be removed (uselessly added)
        data_validation();
	});
});

function data_validation() {

    var data_to_validate=$("textarea#job_description").val();
    alert(data_to_validate);

    console.log("data send is working!"); // sanity check
   $.ajax({
        url : "/rating/", // the endpoint
        type : "GET", // http method
        data : { jd : data_to_validate}, // data sent with the post request
        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console ; to be removed later
            console.log("success");
            $('div#rating').html("<p> Rating :"+json['rating']+"</p>"); 
            $('div#suggestions').html("<p>Suggestions : Add "+ json['suggestions'].toString()+" to improve your Job description");
             // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('body').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



var csrftoken = getCookie('csrftoken');
 
/*
The functions below will create a header with csrftoken
*/
 
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
 
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
