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

## Developer experience

This template ships with the tooling to run it like a real published native
addon:

- **Linting** — flat ESLint config built on `@eslint/js` and
  `typescript-eslint` recommended sets, plus the project rules (tabs, double
  quotes). `npm run lint` / `npm run lint:fix`.
- **C++ formatting** — `clang-format` (config in `.clang-format`) via
  `npm run format`, enforced on commit and checked in CI.
- **API docs** — [TypeDoc](https://typedoc.org) renders HTML docs from your
  TSDoc comments into `docs/` (`npm run docs`).
- **Conventional Commits** — `commitlint` enforces the
  [Conventional Commits](https://www.conventionalcommits.org) format, and
  [git-cliff](https://git-cliff.org) turns that history into `CHANGELOG.md`
  (`npm run changelog`).
- **Git hooks** — [lefthook](https://lefthook.dev) runs ESLint on staged
  JS/TS and `clang-format` on staged C/C++ before each commit, then lints the
  commit message. Installed automatically by the `prepare` script on
  `npm install` (inside a git repo).
- **CI** — `.github/workflows/ci.yml` builds the native addon + TypeScript,
  lints, type-checks, and tests across Linux/macOS/Windows on Node 22 & 24,
  checks C++ formatting, builds the docs, and uploads the build artifact.
- **Editor config** — `.vscode/` recommends ESLint, Todo Tree, clangd and
  clang-format extensions, and wires up format-on-save via ESLint.

### Scripts

| Script | What it does |
| --- | --- |
| `npm run build` | Build the native addon (`node-gyp`) and compile TypeScript. |
| `npm run build:debug` | Build the native addon with debug symbols. |
| `npm run clean` | Remove native build output and `dist/`. |
| `npm run dev` | Build, then run with nodemon. |
| `npm test` | Build, then run the Jest suite. |
| `npm run typecheck` | Type-check without emitting. |
| `npm run lint` / `lint:fix` | Run ESLint (optionally auto-fixing). |
| `npm run format` | Format C/C++ sources with clang-format. |
| `npm run docs` | Generate HTML API docs into `docs/`. |
| `npm run changelog` | Regenerate `CHANGELOG.md` from the commit history. |

### Releasing

`./release.sh v[X.Y.Z]` bumps the version in `package.json`, regenerates
`CHANGELOG.md`, commits, and creates an annotated tag. Then
`git push && git push --tags`.

Only `dist/`, `build/Release`, `src/` and `binding.gyp` are published (the
`"files"` allowlist in `package.json`).

