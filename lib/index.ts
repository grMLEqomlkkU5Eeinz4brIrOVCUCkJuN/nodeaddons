// Native addons (.node files) cannot be imported as ESM — use createRequire to load them.
import { createRequire } from "module";

const require = createRequire(import.meta.url);

const addon = require("../build/Release/addon") as { hello(): string };

export function hello(): string {
	return addon.hello();
}

console.log(hello());
