//https://maxkss.github.io/shinycolors-helper/version.txt

chrome.storage.local.get("state", function(result){
    if(result.state == undefined){
        chrome.storage.local.set({"state": true})
    }
    chrome.storage.local.get("state", function(result){
        if(result.state){ // on
            $(".active-btn").addClass('active')
            $(".state").text("WORKING!")
        }
        else { //off
            $(".active-btn").removeClass('active')
            $(".state").text("STOPPED")
        }
    });
    
});

$(".active-btn").on("click", function(e){
    $(".active-btn").toggleClass('active')

    if($(".active-btn").hasClass('active')){
        chrome.storage.local.set({"state": true})
        $(".state").text("WORKING!")
    }
    else{
        chrome.storage.local.set({"state": false})
        $(".state").text("STOPPED")
    }
})

$('#update-btn').on("click", function(e){
    $.ajax({
        url: 'https://maxkss.github.io/shinycolors-helper/version.txt',
        type: 'get',
        success: function (data) {
            var latest = parseFloat(data);
            var version = parseFloat($('#now-version').text())
            
            if (latest == version){
                $('#go-download').text("최신버전 입니다")
            }
            else if(latest > version){
                $('#go-download').text("최신버전이 있습니다 (클릭 시 이동)")
                $('#go-download').attr('href', 'http://naver.com')
            }
            $('#go-download').show();
        },
    });
})

$("#go-download").on("click", function(e){
    chrome.tabs.create({url: $(this).attr('href')});
})