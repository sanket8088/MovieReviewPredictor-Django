


$(document).ready(function () {
    var textArea = document.getElementById("textarea")
    var submitButton = document.getElementById("submitReview")
    var output = document.getElementById("output")
    $("#submitReview").click(function (event) {

        $.ajax({
            type: "POST",
            url: "/prediction/",
            data: {
                'statement': textArea.value.trim() // from form
            },
            success: function (data) {
                data = JSON.parse(data)
                console.log(data["value"])
                output.innerText = data["value"]

            }
        });
        return false; //<---- move it here
    });

});