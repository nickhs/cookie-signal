	$( "#cookie" ).live( "click", function() {
		$.get('/batsignal', function(data) {
		});
		$('#thankyou').css('display','block')
		$('#thankyou').fadeOut(5000, function() {
		    // Animation complete.
		     
		});
	});