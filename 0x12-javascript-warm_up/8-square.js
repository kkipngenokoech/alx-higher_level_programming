#!/usr/bin/node
square = parseInt(process.argv[2])
if (square){
	index = 0
	for (;index < square; index++)
		for (count = 0; count < square; count++)
			console.log('X')
}
else {
	console.log('Missing size')
}
