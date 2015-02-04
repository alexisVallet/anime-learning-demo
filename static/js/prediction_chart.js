$(function () {
    var template = Handlebars.templates['test_samples'];

    $("#test-samples").html(template({
	"test_images": test_predictions
    }));
    $("#cascading-grid").imagesLoaded(function(){
	$("#cascading-grid").masonry({
	    itemSelector: '.item'
	});
    });
});
