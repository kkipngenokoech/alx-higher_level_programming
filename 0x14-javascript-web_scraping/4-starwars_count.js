#!/usr/bin/node
const request = require('request')
request.get(process.argv[2], (error, response, body) => {
	if(error)
		console.log(error)
	else {
		const responseJSON = JSON.parse(body).results
		console.log(responseJSON.reduce((count, movie) => {
			return movie.characters.find((character) => character.endsWith('/18/'))
				? count + 1
				: count;
		}, 0));
	}
})
