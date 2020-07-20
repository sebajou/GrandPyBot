$(document).ready(function() {

    $('form').on('submit', function(event) {
		$.ajax({
			data : {
				question : $('#questionInput').val()
			},
			type : 'POST',
			url : '/conversation'
		})
		.done(function(data) {

            $('#response').text(data.question).show();
			});
		event.preventDefault();
		});
	});