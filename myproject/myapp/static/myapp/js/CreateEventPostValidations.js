
$(document).ready(function(){



	function fnJSInject(val) 
	{
	    val = val.replace(/&/g, '&amp;');
	    val = val.replace(/</g, '&lt;');
	    val = val.replace(/>/g, '&gt;');
	    return val;
	}

	function fnResetFieldCSS()
	{
		$("#emailid").css('border-color', '');
		$("#user").css('border-color', '');
		$("#subject").css('border-color', '');
		$("#msg").css('border-color', '');
	}



	//$("#errid").css('visibility', 'hidden');


	$("#closebtn").click(function()
	{
		$("#emailid").val('');
		$("#user").val('');
		$("#subject").val('');
		$("#msg").val('');
		fnResetFieldCSS();
		$(".collapse").collapse('hide');

	});

	$("#submitbtn").click(function()
	{
		var emailid = fnJSInject($.trim($("#emailid").val()));
		var user = fnJSInject($.trim($("#user").val()));
		var subject = fnJSInject($.trim($("#subject").val()));
		var msg = fnJSInject($.trim($("#msg").val()));
		
		var disableFLag = false;

		if(emailid.length == 0)
		{
			$("#emailid").css('border-color', 'red');
			$("#emailid").val('');		
			//$("#saveNoteBtn").css('visibility', 'visible');	
			//$("#msgid").text('CC Numb');
			disableFLag = true;
		}
		else
		{
			$("#emailid").css('border-color', '');	
			if(!disableFLag)
			{
				disableFLag = false;	
			}
		}

		if(user.length == 0)
		{
			$("#user").css('border-color', 'red');
			$("#user").val('');		
			//$("#saveNoteBtn").css('visibility', 'visible');
			disableFLag = true;
		}    	
		else
		{
			$("#user").css('border-color', '');	
			
			if(!disableFLag)
			{
				disableFLag = false;	
			}
		}

		if(subject.length == 0)
		{    		
			$("#subject").css('border-color', 'red');
			$("#subject").val('');		
			//$("#saveNoteBtn").css('visibility', 'visible');
			disableFLag = true;
		}    
		else
		{
			$("#subject").css('border-color', '');
			if(!disableFLag)
			{
				disableFLag = false;	
			}
		}   
		
		if(msg.length == 0)
		{    		
			$("#msg").css('border-color', 'red');
			$("#msg").val('');
			//$("#saveNoteBtn").css('visibility', 'visible');
			disableFLag = true;
		}    
		else
		{
			$("#msg").css('border-color', '');
			if(!disableFLag)
			{
				disableFLag = false;	
			}
		} 
		
		if(disableFLag)
		{
			return;	
		}

		var x = document.getElementsByName('newmsg');
		x[0].submit();

	});



});