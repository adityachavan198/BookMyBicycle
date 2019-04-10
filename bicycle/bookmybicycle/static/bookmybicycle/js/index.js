$(document).ready(function () {

$("#logo").hover(function(){
    // {% load static %}

    $(this).attr('src',"static/bookmybicycle/images/5.png")
    }, function(){
    $(this).attr('src',"static/bookmybicycle/images/6.png")
});


window.onscroll = function() {myFunction()};
var header = document.getElementById("myHeader");
var sticky = header.offsetTop;
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}


$('#from_datepicker').datepicker();
$('#to_datepicker').datepicker();

function from_state() {
    var optionSelected = $(this).find("option:selected");
    var state_name   = optionSelected.text();

    console.log(state_name);
    sname = {'state' : state_name };

    $("#from_location option").remove();
    $.ajax('/get_city',{method: 'GET',data:sname}).done(function(result){
          console.log(result);
           $("#from_city option").remove();
           for (var i = result.length - 1; i >= 0; i--) {
               $("#from_city").append('<option>'+ result[i].scity +'</option>');
           };

        }).fail(function () {
      alert('Server down Cities not available');
    });
}

function to_state() {
    var optionSelected = $(this).find("option:selected");
    var state_name   = optionSelected.text();

    console.log(state_name);
    sname = {'state' : state_name };
     $("#to_location option").remove();
    $.ajax('/get_city',{method: 'GET',data:sname}).done(function(result){
           console.log(result);
           $("#to_city option").remove();
           for (var i = result.length - 1; i >= 0; i--) {
               $("#to_city").append('<option>'+ result[i].scity +'</option>');
           };
        }).fail(function () {
       alert('Server down Cities not available');
    });
}
function from_city() {
    var optionSelected = $(this).find("option:selected");
    var city_name   = optionSelected.text();

    var state_name   = $('#from_state').find("option:selected").text();

    console.log(state_name);
    sname = {'state' : state_name };
    console.log(city_name);
    cname = {'city' : city_name,'state' : state_name  };

    $.ajax('/get_loc',{method: 'GET',data:cname}).done(function(result){
          console.log(result);
           $("#from_location option").remove();
           for (var i = result.length - 1; i >= 0; i--) {
               $("#from_location").append('<option>'+ result[i].sloc +'</option>');
           };

        }).fail(function () {
      alert('Server down locations not available');
    });
}

function to_city() {
    var optionSelected = $(this).find("option:selected");
    var city_name   = optionSelected.text();

    var state_name   = $('#to_state').find("option:selected").text();


    console.log(city_name);
    cname = {'city' : city_name,'state' : state_name };

    $.ajax('/get_loc',{method: 'GET',data:cname}).done(function(result){
          console.log(result);
           $("#to_location option").remove();
           for (var i = result.length - 1; i >= 0; i--) {
               $("#to_location").append('<option>'+ result[i].sloc +'</option>');
           };

        }).fail(function () {
      alert('Server down locations not available');
    });
}

$('#from_state').change(from_state);


$('#to_state').change(to_state);


$('#from_city').change(from_city);

$('#to_city').change(to_city);

$('#from_state').click(from_state);


$('#to_state').click(to_state);


$('#from_city').click(from_city);

$('#to_city').click(to_city);

});
