# Node.js Addons Playground

This repo is where I'm learning how Node.js addons work.

I'm experimenting with native modules (mostly using N-API and C++) to understand how to extend Node.js beyond JavaScript. Right now, I'm still figuring things out, but I'm starting to build my own small libraries as I go.

I may or may not build something more similar to [a template repository like this really good example by xan](https://github.com/xan105/node-addons/)

Nothing here is final, so it's all just part of the learning process.

## ESM Support

This project is configured to use ECMAScript Modules (ESM) for modern JavaScript compatibility:

- Uses `"type": "module"` in package.json
- TypeScript configured for ESNext modules
- Proper exports field for ESM imports
- Build process generates ESM-compatible output
- Uses `createRequire()` for native addon integration

## Usage

```bash
# Build the native addon and TypeScript
npm run build

# Run tests
npm test

# Development mode
npm run dev
```

