$(document).ready(function() {
	$('form').on('submit', function(event) {
		$.ajax({
			data : {
				question : $('#question').val(),
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