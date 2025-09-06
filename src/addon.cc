// gets N-API that interfaces with V8
#include <napi.h>

// declares the output of a function would be a string, this function name will
// be called hello. Hello takes in a parameter called &info which is actually
// the reference of the object that is a readonly value from the NAPI callback
// info object somewhere
Napi::String Hello(const Napi::CallbackInfo &info) {

	// returns the NAPI enviroment handles
	Napi::Env env = info.Env();
	return Napi::String::New(env, "Hello from C++!");
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
	exports.Set(Napi::String::New(env, "hello"),
				Napi::Function::New(env, Hello));
	return exports;
}

NODE_API_MODULE(addon, Init)