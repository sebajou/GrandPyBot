$(document).ready(function() {
    $('form').on('submit', function(event) {
		$.ajax({
			data : {
				question : $('#questionInput').val(),
				imgUrlList1 : $('#imgUrlList1').val(),
				imgUrlList2 : $('#imgUrlList2').val(),
				imgUrlList3 : $('#imgUrlList3').val(),
			},
			type : 'POST',
			url : '/conversation'
		})
		.done(function(data) {
            $('#loading').hide();
            $('#response').html(data.question).show();
            document.getElementById("imgUrlList1").src = data.imgUrlList1;
            document.getElementById("imgUrlList2").src = data.imgUrlList2;
            document.getElementById("imgUrlList3").src = data.imgUrlList3;
			});
		event.preventDefault();
		});
	});
