$(document).ready(function () {
  // register validation
  $("#fname-error-message").hide();
  $("#lname-error-message").hide();
  $("#email-error-message").hide();
  $("#pass-error-message").hide();
  $("#confpass-error-message").hide();

  var error_fname = false;
  var error_lname = false;
  var error_email = false
  var error_pass = false;
  var error_conf_pass = false;

  $("#fname_in").focusout(function () {
    check_fname();
  });
  $("#lname_in").focusout(function () {
    check_lname();
  });
  $("#email_in").focusout(function () {
    check_email();
  });
  $("#pass_in").focusout(function () {
    check_pass();
  });
  $("#conf_pass_in").focusout(function () {
    check_confpass();
  });

  function check_fname() {
    var pattern = /^[a-zA-Z]*$/;
    var fname = $("#fname_in").val();
    if (pattern.test(fname) && fname !== '') {
      $("#fname-error-message").hide();
      $("#fname_in").css("border-bottom", "2px solid #34F458");
    } else {
      $("#fname-error-message").html("Should contain only Characters");
      $("#fname-error-message").show();
      $("#fname_in").css("border-bottom", "2px solid #F90A0A");
      error_fname = true;

    }
  }

  function check_lname() {
    var pattern = /^[a-zA-Z]*$/;
    var lname = $("#lname_in").val();
    if (pattern.test(lname) && lname !== '') {
      $("#lname-error-message").hide();
      $("#lname_in").css("border-bottom", "2px solid #34F458");
    } else {
      $("#lname-error-message").html("Should contain only Characters");
      $("#lname-error-message").show();
      $("#lname_in").css("border-bottom", "2px solid #F90A0A");
      error_lname = true;

    }
  }

  function check_email() {
    var pattern = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
    var email = $("#email_in").val();
    if (pattern.test(email) && email !== '') {
      $("#email-error-message").hide();
      $("#email_in").css("border-bottom", "2px solid #34F458");
    } else {
      $("#email-error-message").html("Invalid Email");
      $("#email-error-message").show();
      $("#email_in").css("border-bottom", "2px solid #F90A0A");
      error_email = true;

    }
  }

  function check_pass() {
    var password_length = $("#pass_in").val().length;
    if (password_length < 8) {
      $("#pass-error-message").html("at least 8 Characters");
      $("#pass-error-message").show();
      $("#pass_in").css("border-bottom", "2px solid #F90A0A");
      error_pass = true;
    } else {
      $("#pass-error-message").hide();
      $("#pass_in").css("border-bottom", "2px solid #34F458");
    }
  }

  function check_confpass() {
    var password = $("#pass_in").val();
    var confirm_pass = $("#conf_pass_in").val();
    if (password !== confirm_pass) {
      $("#confpass-error-message").html("Password not Match!");
      $("#confpass-error-message").show()
      $("#conf_pass_in").css("border-bottom", "2px solid #F90A0A");
      error_conf_pass = true;
    } else {
      $("#confpass-error-message").hide();
      $("#conf_pass_in").css("border-bottom", "2px solid #34F458");
    }
  }

  $("#register_form").submit(function () {
    error_fname = false;
    error_lname = false;
    error_email = false
    error_pass = false;
    error_conf_pass = false;

    check_fname();
    check_lname();
    check_email();
    check_pass();
    check_confpass();

    if (error_fname === false && error_lname === false && error_email === false && error_pass === false && error_conf_pass === false) {
      return true;
    } else {
      return false;
    }

  });


});

//send request without refrishing the page
function httpGet(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false); // false for synchronous request
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

function buttonFunction(id) {
  var url = "/live/";
  var response = httpGet(url + id);
  //document.getElementById("ID").innerHTML = response;
}

// var disableButton5k = (e) => {
//   console.log("it happen");
//   $('#240fps').prop('disabled', true);
//   $('#240fps').toggleClass('btn btn-secondary');
//   //$('#120fps').prop('disabled', true);
//   //$('#60fps').prop('disabled', true);
// };

// var disableButton4k = (e) => {
//   console.log("va");
//   $('#240fps').prop('disabled', true);
//   $('#120fps').prop('disabled', true);
// };

// var disableButton2k = (e) => {
//   $('#240fps').prop('disabled', true);
//   $('#24fps').prop('disabled', true);
//   $('#30fps').prop('disabled', true);
// };

// $(document).on('click', '5k', disableButton5k);

