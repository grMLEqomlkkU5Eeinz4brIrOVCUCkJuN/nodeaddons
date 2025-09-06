{
  "targets": [
	{
	  "target_name": "addon",
	  "cflags!": [ "-fno-exceptions" ],
	  "cflags_cc!": [ "-fno-exceptions" ],
	  "sources": [ "src/addon.cc" ],
	  "include_dirs": [
		"<!@(node -p \"require('node-addon-api').include\")",
"../node_modules/node-addon-api",                                                    
"node_modules/node-addon-api",                                                       
"/usr/include/node",                                                                 
"/usr/local/include/node",                   
	  ],
	  "libraries": [],
	  "dependencies": [
		"<!(node -p \"require('node-addon-api').gyp\")"
	  ],
	  "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ]
	}
  ]
}
