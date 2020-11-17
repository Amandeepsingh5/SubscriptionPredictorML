// client/.babel-plugin-macrosrc.js
const {execSync} = require('child_process');
const urlMap = JSON.parse(execSync('./flaskmapjson.bash'));
module.exports = {
 flaskURLs: {
 urlMap
 }
};