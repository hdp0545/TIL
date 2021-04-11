/* banner.js - 배너 디자인 스크립트, 2012 © yamoo9.com	
---------------------------------------------------------------- */
;(function($){
	$(function() { // $(document).ready(); 문서가 준비되면... 실행.
		
		var banner_audio= new Audio(),		// Audio 객체 생성.
			webm		= isSupportWebM(),	// webm 포멧 지원 검사.
		
		if(webm) {	// webm 지원 시.
			banner_audio.src = 'media/banner_sound.webm';
		} else {	// webm 미지원 시.
			banner_audio.src = 'media/banner_sound.mp3';
		};
			
		$('.ban')
			.bind('mouseover focusin', function() { // 마우스오버, 포커스인 시, 이벤트 핸들링.
				ban_audio.load(); // audio 로드.
				ban_audio.play(); // audio 재생.
			})
			.bind('mouseout focusout', function() { // 마우스아웃, 포커스아웃 시, 이벤트 핸들링.
				banner_audio.pause(); 			// audio 일시정지.
				banner_audio.currentTime = 0;	// audio 재생위치 초기화.
			});
		
	});
})(window.jQuery);

// webm 포멧 지원 검사 함수.
function isSupportWebM() {
	var tester = document.createElement('audio');
	return !!tester.canPlayType('audio/webm');
};
