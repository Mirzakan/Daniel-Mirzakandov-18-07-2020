var app = new Vue({
	el: "#app",
	delimiters: ['[[', ']]'],
	data: {
		activeItem: 'Sent',
		msgData: msgData,
		useID: ''
	},
	methods: {
		isActive ( menuItem ) {
			return this.activeItem === menuItem
		},
		setActive ( menuItem ) {
			this.activeItem = menuItem
		},
		getMessages ( e ) {
			// get vue instace
			let _ = this;
			// clear the delay
			clearTimeout(window.delay);
			// prevent multiple ajax because it is listening to each input event
			window.delay = setTimeout(function() {
				_.useID = e.target.value;
				// set up our HTTP request
				var xhr = new XMLHttpRequest();
				// setup our listener to process completed requests
				xhr.onload = function () {
					// sucess - change the vue data source
					if ( xhr.status >= 200 && xhr.status < 300 ) {
						_.msgData = JSON.parse(xhr.response);
					// faild
					} else {
						console.log('The request failed!');
					}
				};
				// create request
				xhr.open('GET', '/getMessages?userId='+_.useID);
				// send request
				xhr.send();
			},300);
		}
	}
})