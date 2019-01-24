var s = document.createElement('script');
// TODO: add "script.js" to web_accessible_resources in manifest.json
s.src = chrome.extension.getURL('/lib/jquery-3.3.1.min.js');
s.onload = function () {
    this.remove();
};
(document.head || document.documentElement).appendChild(s);