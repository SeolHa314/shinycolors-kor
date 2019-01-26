var s = document.createElement('script');
s.src = chrome.extension.getURL('/lib/jquery-3.3.1.min.js');
s.onload = function () {
    this.remove();
};
(document.head || document.documentElement).appendChild(s);

$(document).ready(function(){
    chrome.runtime.sendMessage({}, function(response) {
        if(response.success){
            var state = document.createElement("p")
            $(state).attr("id", "patchState").text(response.state).hide().appendTo($("body"))
        }
    });
});

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        $("#selectPointElement").text(request.point)
        $("#patchState").text(request.state)
});