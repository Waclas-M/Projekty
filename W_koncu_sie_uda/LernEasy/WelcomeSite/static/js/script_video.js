
let touchEvent = 'ontouchstart' in window ? 'touchstart' : 'click';

var video = document.querySelector('.video');
var btn = document.getElementById('play-pause');

function togglePlayPause() {
    if(video.paused) {
        btn.className = "pauseButton";
        video.play();
    } else {
        btn.className = "playButton";
        video.pause();
    }
}

// Bind event
btn.addEventListener(touchEvent, togglePlayPause);