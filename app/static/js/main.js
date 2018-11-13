//initialization
$('#greeting').fadeIn(1000, function () {
  $(this).fadeOut(4000)
})

// toast
$('#toast-body').fadeIn(1000);
$('#toast-text').text('This video was submited by the last user, you would be able to submit after finish this video!');

$('#toast-btn').click(function () {
  $('#toast-body').fadeOut(1000)
});

//setTimeout(function () {
//  $('#toast-body').fadeOut(200)
//}, 100000);

$('#toast-btn1').click(function () {
  $('#toast-body1').fadeOut(1000)
});
setTimeout(function () {
  $('#toast-body1').fadeOut(200)
}, 200000)


//Global Variable
let msg; //



//


//spectre modal
$('#btn').click(function () {
  $('#modal-id').addClass('active');
});

$('.btn-clear').click(function () {
  $('#modal-id').removeClass('active')
});


// Load the IFrame Player API code asynchronously.
var tag = document.createElement("script");
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName("script")[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
// Replace the 'ytplayer' element with an <iframe> and
// YouTube player after the API code downloads.
var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player("ytplayer", {
    height: "360",
    width: "640",
    // videoId: 0,
      events: {
	  'onReady': function(e){e.target.mute(); onPlayerReady();}

    },
    playerVars: {
	autoplay: 1,
	controls: 0,
	enablejsapi: 1,
	disablekb: 1, // disable keyboard
	modestbranding: 1,
	cc_load_policy: 1, // load cc
	showinfo: 0, // not display information
	rel: 0 //show related video at end
    }
  });
}

//check if video ended
function check_player(videoId) {
  let setCheck = setInterval(endPlayer, 2000)

  function endPlayer() {
    if (player.getPlayerState() != 0) {
	player.playVideo(); // play video
	unMute();


    } else { //video ended

      clearInterval(setCheck); //clear interval

      //remove video for user queue database
      let videoFinished = $.post('/finishVideo', {
        'videoId': videoId
      });

      videoFinished.done(function () {

        let checkbox_val = $(":checkbox").prop('checked');

        if (checkbox_val) {

          getVideoId();

        } else {
          // go to submit container
          $('#checkbox').fadeOut(1000) //remove chebox

          // clear input 
          document.getElementById('videoInput').value = "";
          $('.emojionearea-editor').text('');

          $('#ytplayer').fadeOut(1000, function () {
            $('#submit').fadeIn(800); // show submit container
            $('#toast-body1').fadeOut(500);

            $('#toast-body').fadeOut(1000, function () {
              $('#toast-text').text('Please Submit your video!');
              $('#toast-text').addClass('text-center')
              $('#toast-body').fadeIn(1000);
            });
          });
        };

      });


    };
  };
}






// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
  $('#content').css({
    'padding-top': '0%'
  }); // return body padding
  $('#checkbox').fadeIn(2000); // show checkbox
  getVideoId();
}


// submit btn click event
$('form').submit(function (event) {
  postVideoId(event);
  //send form to to server.
  $('#submit').fadeOut(1000);
  $('#toast-body').fadeOut(1000);
  $('#greeting').text('👊Thank You 👊').fadeIn(1000, function () {
    $('#content').addClass('loading');
    $('#greeting').fadeOut(1000, function () {
      getVideoId();


    });
  });
});



// Video finished
function videoFinished(videoId, callback) {
  $.post('/finishVideo', {
    'videoId': videoId
  });
}

// un-mute video
function unMute(){
document.addEventListener('click', function(event){
 player.unMute();
}, {'once': true});
};


//emoticon
$(document).ready(function() {
$("#msg").emojioneArea({
  pickerPosition: "left",
  tonesStyle: "bullet"
});
});
