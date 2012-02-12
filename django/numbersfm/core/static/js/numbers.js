$(function() {
    AudioPlayer.setup("/static/audio-player/player.swf", {  
        width: 290
    });
    
    $('a.audio').each(function(index) {
        var player_id = 'sound-player-' + index;
        var $player = $('<div id="' + player_id + '"></div>');

        $(this).after($player);
        AudioPlayer.embed(player_id,
                          {
                              soundFile: $(this).attr('href')
                          });
    });
});