const addon = require("../build/Release/addon");

export function hello(): string {
	return addon.hello();
}

console.log(hello());