#!/usr/bin/node
const arguments = process.argv.slice(2)
if (arguments != 0){
	arguments.forEach((arg, index)=>{
		console.log(`${arg}`)
	})
}
else {
	console.log('No argument')
}
