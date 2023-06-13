#!/usr/bin/node
const request = require('request')
request(process.argv[2], (error, response, body) => {
	if (error) {
		console.log(error)
	}
	else {
		const responseJSON = JSON.parse(body)
		const completed = {}
		responseJSON.forEach((task) => {
			if (task.completed === true)
				completed[task.userId]? completed[task.userId]++ : completed[task.userId] = 1
		})
		console.log(completed)
	}
})
