$(document).ready(function() {

	$('#questionInput').keypress(function(event) {
		$.ajax({
			data : {
				question : $('#questionInput').val(),
			},
			type : 'POST',
			url : '/conversation'
		})
		.done(function(data) {

            $('#response').text(data.question).show();
			}
		});
		event.preventDefault();

	});