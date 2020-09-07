console.log("Hello world! 1");

$('form').on('submit', function(event) {
    $.ajax({
        // Get data from back
        data : {
            question : $('#questionInput').val(),
            imgUrlList1 : $('#imgUrlList1').val(),
            imgUrlList2 : $('#imgUrlList2').val(),
            imgUrlList3 : $('#imgUrlList3').val(),
        },
        type : 'POST',
        url : '/conversation'
    })
    // Do if AJAX done
    .done(function(data) {
        // Hide loading gif
        $('#loading').hide();
        // Display data from back
        $('#response').html(data.question).show();
        // Display map from url from back
        document.getElementById("imgUrlList1").src = data.imgUrlList1;
        document.getElementById("imgUrlList2").src = data.imgUrlList2;
        document.getElementById("imgUrlList3").src = data.imgUrlList3;

        console.log("Hello world! 2");

        // => Functions for memorise conversation in sessionStorage
        // Recuperation of field to record
        var recField = document.getElementById("resp");

        // Display recorded data if record already exist
        if (sessionStorage.getItem("sessionSave")) {
            document.getElementById("memSession").innerHTML = sessionStorage.getItem("sessionSave");
            console.log(sessionStorage.getItem("sessionSave"));
        }

        // Record request and response
        sessionStorage.setItem("sessionSave", recField.innerHTML);

        });
    event.preventDefault();
    });
