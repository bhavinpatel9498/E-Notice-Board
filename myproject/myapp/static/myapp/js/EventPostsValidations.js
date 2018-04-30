		$(document).ready(function(){

		window.onscroll = function() {myFunction()};

		var header = document.getElementById("myHeader");
		var sticky = header.offsetTop;

		function myFunction() {
		  if (window.pageYOffset >= sticky) {
		    header.classList.add("sticky");
		  } else {
		    header.classList.remove("sticky");
		  }
	
		  	var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
	  		var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
	  		var scrolled = (winScroll / height) * 100;
	  		document.getElementById("myBar").style.width = scrolled + "%";
		}
			


	$("#officialpostbtn").click(function()
	{

		window.location.href = "/myapp/createeventpost";

	});






});