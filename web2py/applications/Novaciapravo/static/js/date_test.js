test

n =  new Date();
	console.log()
	date = n.getDate() + "." + n.getMonth() + "." + n.getFullYear() + "," + ' ' + n.getHour() + ":" + n.getMinutes();
	document.getElementById("created_on").value = date;