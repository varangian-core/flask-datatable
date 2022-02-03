// jquery is used to run the validator function on  the form
* jquery.validate plagin added using cdn. Go to jqueryvalidation.org to see what methods are provided */
/* Create custom validation method */
$.validator.addMethod("startWithA", function(value, element) {
	return /^A/.test(value);
}, "Field must start with A");
$("form").validate({
	rules: {
		fullname: {
			required: true
			//minlength: 5,
			//maxlength: 10,
			//email: true
			//startWithA: true
		},
		password: {
			required: true
		},
		pet: {
			required: true,
			maxlength: 2
		}
	},
// Custom message for error
	messages: {
		fullname: {
			required: "You must enter your fullname"
		}
	},
	messages: {
		pet: {
			required: "You must select at least 1 box",
			maxlength: "You must select no more then 2 boxes"
		}
	},
	highlight: function(element, errorClass) {
		$(element).closest(".form-group").addClass("has-error");
	},
	unhighlight: function(element, errorClass) {
		$(element).closest(".form-group").removeClass("has-error");
	},
	errorPlacement: function (error, element) {
		error.appendTo(element.parent().next());
	},
	errorPlacement: function (error, element) {
		if(element.attr("type") == "checkbox") {
			element.closest(".form-group").children(0).prepend(error);
		}
		else
			error.insertAfter(element);
	}
});
