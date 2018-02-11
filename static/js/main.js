$(document).ready(function(){
$("#form").submit(function(){

var data=$("#form").serialize();
alert(data)
$.ajax({
url: "/PostData",
type: "POST",
data: data,

success: function(data)
{

alert(data)

}
});


return false;

});
});



