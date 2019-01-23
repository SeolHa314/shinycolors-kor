chrome.webRequest.onBeforeRequest.addListener(
    function (details) {
        if (details.url.includes("shinycolors.enza.fun/produce"))
            return {
                redirectUrl: "https://maxkss.github.io/shinycolors-perfect/produce.js"
            };
    }, {
        urls: ["*://shinycolors.enza.fun/*.js"]
    },
    ["blocking"]
);