# Codebase Overview - Legacy Todo Application (TodoMVC - Backbone.js)

## Age
First release in 2010, last major update in 2016. The Backbone.js framework itself
has not received significant updates since 2016, making it effectively legacy by
modern JavaScript standards.

## Size
~3,200 LOC across JavaScript, HTML, and CSS files.
- JavaScript: ~2,100 LOC
- HTML templates: ~400 LOC
- CSS: ~700 LOC

## Dependencies
- Backbone.js 1.3.3 (no longer actively maintained)
- Underscore.js 1.8.3 (utility library, mostly replaced by native ES6+ methods)
- jQuery 1.11.1 (outdated major version with known security vulnerabilities)
- RequireJS 2.1.10 (module loader, replaced by ES6 native modules and bundlers)
- localStorage API (no server-side persistence layer)

## Known Issues and Pain Points

### Architecture
- Tightly coupled Views and Models with no clear separation of concerns
- No component-based architecture; entire UI rebuilt on every model change
- Global state management through Backbone events is difficult to trace and debug

### Code Quality
- No automated tests (unit, integration, or end-to-end)
- Inconsistent coding style mixing ES5 and early ES6 patterns
- Heavy reliance on jQuery for DOM manipulation instead of modern APIs
- Callback-based async patterns instead of Promises or async/await

### Security
- jQuery 1.11.1 contains known XSS vulnerabilities (CVE-2015-9251)
- No input sanitization on user-submitted todo items
- No Content Security Policy (CSP) headers configured

### Performance
- Full DOM re-render triggered on every minor model update
- No lazy loading or code splitting
- All dependencies loaded synchronously, increasing initial page load time

### Maintainability
- No TypeScript or type annotations; runtime errors are hard to catch early
- Documentation is minimal and outdated
- No linting or formatting tools configured (no ESLint, Prettier)
- Build tooling relies on outdated Grunt tasks with no modern bundler (Webpack/Vite)
