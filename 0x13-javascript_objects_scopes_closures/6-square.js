#!/usr/bin/node
const Vsquare = require("./5-square.js")
class Square extends Vsquare{
	constructor (size) {
		super(size)
	}
	charPrint(c='X'){
		for (let index = 0; index < this.height; index++){
			console.log(c.repeat(this.width))
		}
	}
}
module.exports = Square
