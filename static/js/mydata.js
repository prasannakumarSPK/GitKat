$(document).ready(function() {

	$('form').on('submit', function() {
		
		$.ajax({
			data : {
				name : $('#RollNo').val(),
				
			},
			
			type : 'POST',
			url : '/execute'
		})
		.done(function(data) //it means what should happen after AJAX call
		{	console.log('checking');
			if(data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				console.log('checking');
			}
			else {
				// var obj = JSON.parse(data.name);
				console.log(data);
				console.log('checking');
				$('#successAlert').html(data.name).show();
				// // $('#successAlert').html(JSON.parse(data.name)).show();
				$('#errorAlert').hide();
				}			
		}
			);

		event.preventDefault();//this prevent form to get submitted twice(*VVIMP)

	});

});



