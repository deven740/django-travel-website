$(document).ready(function () {
    var image_id_array = [];

    $("img").click(function () {
        image_id = $(this).data("image-id");
        if ($.inArray(image_id, image_id_array) != -1) {
            image_index = image_id_array.indexOf(image_id);
            image_id_array.splice(image_index, 1);
            $(this).css("border", "None");
        } else {
            image_id_array.push(image_id);
            $(this).css("border", "3px solid blue");
        }
    });

    $("#delete-images").click(function () {
        if (image_id_array.length == 0) {
            window.alert("Please select atleast 1 image");
        } else {
            $.ajax({
                type: "POST",
                url: "/site-admin/ajax/delete-images",
                data: { image_list: image_id_array },
                headers: {
                    "X-CSRFTOKEN": window.CSRF_TOKEN,
                },
                success: function (response) {
                    window.location.reload();
                },
            });
        }
    });
});
