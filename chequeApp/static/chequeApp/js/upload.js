/**
 * Created by root on 19/9/16.
 */
   //Adding a submit function to the form
$(document).ready(function () {

	$('#begin').change(function()
	{
    alert("hello1");
		$('#test').submit();
	});

	$('#test').submit(function(e){
    alert('hello2');
	//Preventing the default behavior of the form
	//Because of this line the form will do nothing i.e will not refresh or redirect the page
	e.preventDefault();

	//Creating an ajax method
	$.ajax({
		//Getting the url of the uploadphp from action attr of form
		//this means currently selected element which is our form
		url: $(this).attr('action'),

		//For file upload we use post request
		type: "POST",

		//Creating data from form
		data: new FormData(this),

		//Setting these to false because we are sending a multipart request
		contentType: false,
		cache: false,
		processData: false,
		success: function(data){
			//If the request is successfull we will get the scripts output in data variable
			//Showing the result in our html element
			alert('uploaded sucessfully');
			$('#ladybug1').attr(src,"data:image/jpg;base64," + "{% static '' %}{{ ip }}/abc.jpg");
			
		},
		error: function(data){
			alert('Error happenink');
		}
	});
});

});

