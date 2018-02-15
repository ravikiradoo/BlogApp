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
$("#lform").submit(function(){

var data=$("#lform").serialize();
$.ajax({
url: "/login",
type: "POST",
data: data,

success: function(data)
{

if(data=="false")
 alert("User could not matched")
else
   {alert("User matched")

    window.location.href="/"}

}
});


return false;

});
$("#Pform").submit(function(){

var data=$("#Pform").serialize();
$.ajax({
url: "/post",
type: "POST",
data: data,

success: function(data)
{

if(data=="pass")
 {alert("Post submitted successfully")
     window.location.href="/"}
else
   {alert("Something went wrong")

    window.location.href="/"}

}
});


return false;

});


$("#logout").click(function(){

$.ajax({
url:"/Logout",
type:"GET",
success:function(data)
{
if(data=='pass')
{
window.location.href="/"
}
else
{
alert("somthing wnet wrong")}
}

})
return false;
});

$("#sform").submit(function(){
var form=$("#sform").serialize();

$.ajax({
url:"/update",
type:"POST",
data:form,
success:function(data)
{
if(data=="pass")
{
alert("Profile updated successfully");
}
}


});
return false
});

$(".commentform").submit(function(){
var form = $(this).serialize();

$.ajax({
url:"/comment",
type:"POST",
data:form,
success:function(data)
{
if(data=="pass")
{
alert("Comment added successfully");}

else
{alert("Comment added successfully");}
}
});
return false

});



$(".dform").submit(function(){

var form = $(this).serialize();
alert(form);
$.ajax({

url:"/deletePost",
type:"POST",
data:form,
success:function(data){
if(data=="pass")
{
alert("Deleted Successfully");
window.location.href="/HomeFeed"
}
else
{
alert("something went wrong");
}
}

});
return false;
});

});



