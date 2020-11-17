// client/src/setupProxy.js
const proxy = require('http-proxy-middleware');
console.log('setupproxy');
module.exports = app => {
    app.use(proxy('/api', {
    target: 'http://localhost:52154',
    changeOrigin: true,
 }));
};