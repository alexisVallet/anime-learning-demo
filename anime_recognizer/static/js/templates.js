(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['prediction'] = template({"1":function(depth0,helpers,partials,data) {
    var stack1, helper;

  return "  <a href=\""
    + ((stack1 = helpers['with'].call(depth0,(depth0 != null ? depth0.illust_info : depth0),{"name":"with","hash":{},"fn":this.program(2, data, 0),"inverse":this.noop,"data":data})) != null ? stack1 : "")
    + "\" target=\"_blank\">\n  <img src=\""
    + this.escapeExpression(((helper = (helper = helpers.image || (depth0 != null ? depth0.image : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0,{"name":"image","hash":{},"data":data}) : helper)))
    + "\" class=\"img-responsive\"\n  "
    + ((stack1 = helpers['with'].call(depth0,(depth0 != null ? depth0.illust_info : depth0),{"name":"with","hash":{},"fn":this.program(4, data, 0),"inverse":this.noop,"data":data})) != null ? stack1 : "")
    + ">\n  </a>\n";
},"2":function(depth0,helpers,partials,data) {
    var helper;

  return this.escapeExpression(((helper = (helper = helpers.url || (depth0 != null ? depth0.url : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0,{"name":"url","hash":{},"data":data}) : helper)));
},"4":function(depth0,helpers,partials,data) {
    var helper, alias1=helpers.helperMissing, alias2="function", alias3=this.escapeExpression;

  return "title=\"'"
    + alias3(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"title","hash":{},"data":data}) : helper)))
    + "' by "
    + alias3(((helper = (helper = helpers.author || (depth0 != null ? depth0.author : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"author","hash":{},"data":data}) : helper)))
    + "\"";
},"6":function(depth0,helpers,partials,data) {
    var helper;

  return "  <img src=\""
    + this.escapeExpression(((helper = (helper = helpers.image || (depth0 != null ? depth0.image : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0,{"name":"image","hash":{},"data":data}) : helper)))
    + "\" class=\"img-responsive\">\n";
},"8":function(depth0,helpers,partials,data) {
    var helper, alias1=helpers.helperMissing, alias2="function", alias3=this.escapeExpression;

  return "    <div class=\"progress\" title=\""
    + alias3(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"name","hash":{},"data":data}) : helper)))
    + "\">\n      <div class=\"progress-bar\" role=\"progressbar\" style=\"width: "
    + alias3(((helper = (helper = helpers.confidence || (depth0 != null ? depth0.confidence : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"confidence","hash":{},"data":data}) : helper)))
    + "%\">\n	"
    + alias3(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"name","hash":{},"data":data}) : helper)))
    + "\n      </div>\n    </div>\n";
},"10":function(depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers['with'].call(depth0,(depth0 != null ? depth0.illust_info : depth0),{"name":"with","hash":{},"fn":this.program(11, data, 0),"inverse":this.noop,"data":data})) != null ? stack1 : "");
},"11":function(depth0,helpers,partials,data) {
    var helper, alias1=helpers.helperMissing, alias2="function", alias3=this.escapeExpression;

  return "    <small><a href=\""
    + alias3(((helper = (helper = helpers.url || (depth0 != null ? depth0.url : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"url","hash":{},"data":data}) : helper)))
    + "\">'"
    + alias3(((helper = (helper = helpers.title || (depth0 != null ? depth0.title : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"title","hash":{},"data":data}) : helper)))
    + "'</a> by <a href=\"http://"
    + alias3(((helper = (helper = helpers.author || (depth0 != null ? depth0.author : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"author","hash":{},"data":data}) : helper)))
    + ".deviantart.com\">"
    + alias3(((helper = (helper = helpers.author || (depth0 != null ? depth0.author : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"author","hash":{},"data":data}) : helper)))
    + "</a> is licensed under <a href=\""
    + alias3(((helper = (helper = helpers['license-url'] || (depth0 != null ? depth0['license-url'] : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"license-url","hash":{},"data":data}) : helper)))
    + "\">"
    + alias3(((helper = (helper = helpers['license-name'] || (depth0 != null ? depth0['license-name'] : depth0)) != null ? helper : alias1),(typeof helper === alias2 ? helper.call(depth0,{"name":"license-name","hash":{},"data":data}) : helper)))
    + "</a>.</small>\n";
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
    var stack1, helper, options, buffer = 
  "<div class=\"col-sm-3 item\">\n<div class=\"thumbnail\">\n"
    + ((stack1 = helpers['if'].call(depth0,(depth0 != null ? depth0.illust_info : depth0),{"name":"if","hash":{},"fn":this.program(1, data, 0),"inverse":this.program(6, data, 0),"data":data})) != null ? stack1 : "")
    + "  <div class=\"caption\">\n";
  stack1 = ((helper = (helper = helpers.predictions || (depth0 != null ? depth0.predictions : depth0)) != null ? helper : helpers.helperMissing),(options={"name":"predictions","hash":{},"fn":this.program(8, data, 0),"inverse":this.noop,"data":data}),(typeof helper === "function" ? helper.call(depth0,options) : helper));
  if (!helpers.predictions) { stack1 = helpers.blockHelperMissing.call(depth0,stack1,options)}
  if (stack1 != null) { buffer += stack1; }
  return buffer + ((stack1 = helpers['if'].call(depth0,(depth0 != null ? depth0.illust_info : depth0),{"name":"if","hash":{},"fn":this.program(10, data, 0),"inverse":this.noop,"data":data})) != null ? stack1 : "")
    + "  </div>\n</div>\n</div>\n";
},"useData":true});
templates['test_samples'] = template({"1":function(depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = this.invokePartial(partials.prediction,depth0,{"name":"prediction","data":data,"indent":"  ","helpers":helpers,"partials":partials})) != null ? stack1 : "");
},"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
    var stack1;

  return "<div class=\"container-fluid\">\n<div class=\"row\" id=\"test-samples-grid\">\n"
    + ((stack1 = helpers.each.call(depth0,(depth0 != null ? depth0.test_images : depth0),{"name":"each","hash":{},"fn":this.program(1, data, 0),"inverse":this.noop,"data":data})) != null ? stack1 : "")
    + "</div>\n</div>\n";
},"usePartial":true,"useData":true});
})();
