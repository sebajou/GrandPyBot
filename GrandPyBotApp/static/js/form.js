$(document).ready(function() {

    $('form').on('submit', function(event) {
		$.ajax({
			data : {
				question : $('#questionInput').val(),
				imgUrlList1 : $('#imgUrlList1').val(),
			},
			type : 'POST',
			url : '/conversation'
		})
		.done(function(data) {
            $('#loading').hide();
            $('#response').html(data.question).show();
            document.getElementById("imgUrlList1").src = data.imgUrlList1;
            $('#imgUrlList1').text(data.imgUrlList1).show();
			});
		event.preventDefault();
		});
	});
