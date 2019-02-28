chrome.webRequest.onBeforeRequest.addListener(
    function (details) {
        if( details.url.includes("shinycolors.enza.fun/app")){
            return {
                redirectUrl: "https://maxkss.github.io/shinycolors-helper/app.js"
            }
        }
    }, {
        urls: ["*://shinycolors.enza.fun/app*"]
    },
    ["blocking"]
);
console.log("hey2")
var state = true;
chrome.storage.local.get("state", function (result) {
    state = result.state
});

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      sendResponse ({
          'success' : true,
          'state' : state
      })
});

chrome.storage.onChanged.addListener(function(changes, area) {
    if ("state" in changes) {
        state = changes.state.newValue
    }

    chrome.tabs.query({}, function(tabs){
        for(var i = 0; i<tabs.length; i++){
            if(tabs[i].url.includes("shinycolors.enza.fun")){
                chrome.tabs.sendMessage(tabs[i].id, {state : state}, null);  
            }
        }
    });
});