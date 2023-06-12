#!/usr/bin/node
const request = require('request')
const starwars = 'https://swapi-api.alx-tools.com/api/films/'+process.argv[2]
request.get(starwars, function(error, response, body){
	if (error) {
		console.log(error)
		return
	}
	else if (response.statusCode === 200){
		const responseJSON = JSON.parse(body)
		console.log(responseJSON.title)
	}
	else {
		console.log("error")
	}
})
