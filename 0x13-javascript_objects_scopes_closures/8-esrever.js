#!/usr/bin/node
exports.esrever = function (list){
	listreversed = []
	for (let index = list.length-1; index >= 0; index --){
		listreversed.push(list[index])
	}
	return listreversed
}
