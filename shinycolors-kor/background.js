var state = true;
chrome.storage.local.get("state", function (result) {
    state = result.state
});

chrome.webRequest.onBeforeRequest.addListener(
    function (details) {
        if (details.url.includes("shinycolors.enza.fun/app")) {
            if (state) {
                return {
                    redirectUrl: "https://maxkss.github.io/shinycolors-helper/app.js"
                }
            }
        }
    }, {
        urls: ["*://shinycolors.enza.fun/*"]
    },
    ["blocking"]
);

chrome.storage.onChanged.addListener(function(changes, area) {
    if ("state" in changes) {
        state = changes.state.newValue
    }
});