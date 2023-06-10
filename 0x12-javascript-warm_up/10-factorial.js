#!/usr/bin/node
function factorial(factor, count){
	count *= factor
	factor--
	while(factor > 1){
		factorial(factor, count)
		factor--
		if(factor === 1){
			console.log(count)
		}
	}
}
arg = parseInt(process.argv[2])
factorial(arg, 1)
