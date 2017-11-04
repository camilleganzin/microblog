$(document).ready( function() {
	var csrftoken = $("input[name='csrfmiddlewaretoken']").val();
	$('.post-form').submit(function() {
		var submitButton = $(':submit', this);
		submitButton.attr('disabled', true);
		$.ajax({
			url: '/microblog/post/new/',
			type: 'POST',
			dataType: 'json',
			data: $(this).serialize(),
			crossDomain: false,
			beforeSend: function(xhr, settings) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}, 
		}).done(function(data) {
			if(data.success){
				console.log(data);
				$(location).attr('href', '/microblog');
				socket.send('new message')
			} 
		}).fail(function(data) {
			alert(data.status + ':' + data.statusText);
		}).always(function() {
			submitButton.attr('disabled', false);
		});
		return false;
	});

	var ws = new WebSocket('ws://'+ location.host + '/my_ws');
	ws.onopen = function() {
		console.log('coucou WS')
		ws.send({event: 'open', data: {foo: 'bar'}});
		console.log('CONNECTION: open');
	}
	ws.onclose = function() {
		console.log('Connection: ERROR');
	};
	ws.onerror = function(error) {
		console.log('Connection: CLOSED', error);
	};

});