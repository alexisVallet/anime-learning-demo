$(function () {
    // Display the random test samples.
    var pred_template = Handlebars.templates['prediction']
    var test_template = Handlebars.templates['test_samples'];
    Handlebars.registerPartial('prediction', pred_template)

    $("#test-samples").html(test_template({
	"test_images": test_predictions
    }));
    $("#test-samples-grid").waitForImages().done(function(){
	$("#test-samples-grid").masonry({
	    itemSelector: '.item'
	});
    });
    // Display user-uploaded images.
    $("#uploaded-samples-grid").masonry({
	itemSelector: '.item'
    });
    // File upload.
    $("#file-upload").change(function(){
	var file_data = $("#file-upload").prop('files')[0];
	// Read the raw data client-side to display without uploading.
	var fr = new FileReader();
	fr.onloadend = function () {
	    // Because the FileReader API is terrible, have to wrap this in a callback.
	    // Call the identification web service.
	    var form_data = new FormData();
	    form_data.append('file', file_data);

	    $.ajax({
		url: '/identify_upload',
		type: 'post',
		data: form_data,
		processData: false,
		contentType: false,
		success: function(pred) {
		    // Pass the prediction results and raw image data to the thumbnail template.
		    var pred_html = jQuery(pred_template({
			image: fr.result,
			predictions: pred.results
		    }));
		    pred_html.hide();
		    $("#uploaded-samples-grid")
			.append(pred_html);
		    pred_html.waitForImages().done(function(){
			pred_html.show();
			$("#uploaded-samples-grid")
			    .masonry('appended', pred_html, true)
			    .masonry('layout');
		    });
		}
	    });
	}
	fr.readAsDataURL(file_data)	
    });
});
