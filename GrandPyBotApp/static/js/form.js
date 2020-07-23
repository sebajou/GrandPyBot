$(document).ready(function() {

    $('form').on('submit', function(event) {
		$.ajax({
			data : {
				question : $('#questionInput').val(),
			},
			type : 'POST',
			url : '/conversation'
		})
		.done(function(data) {
            $('#response').html(data.question).show();
            $('#loading').hide();
			});
		event.preventDefault();
		});
	});
