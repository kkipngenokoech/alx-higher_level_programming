#!/usr/bin/node
count = parseInt(process.argv[2])
if (count){
	let index = 0
	while (index < count){
		console.log('C is fun')
		index++
	}
}
else {
	console.log('Missing number of occurrences')
}
