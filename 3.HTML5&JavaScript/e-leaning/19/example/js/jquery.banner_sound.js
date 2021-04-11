/* jquery.banner_sound.js - 배너 디자인 jQuery 플러그인, 2012 © yamoo9.com
---------------------------------------------------------------- */
;(function($) { // 자바스크립트 자가실행함수

	/*	jQuery 플러그인 banner_sound 작성합니다.
	*	$.fn은 jQuery.prototype을 말합니다.
	*	jQuery 플러그인 작성 기본 구문입니다.
	*/
	$.fn.ban_sound = function(audio_src) { // audio_src : 음원주소
		
		var ban_audio = new Audio(), // 오디오 객체 생성.
			hovered = false;			// hovered 체크변수 설정.
		
		function isSupportWebM() {		// webm 지원여부 검사함수.
			var tester = document.createElement('audio');
			return !!tester.canPlayType('audio/webm');
		};
		
		if(isSupportWebM()) {
			ban_audio.src = audio_src + '.webm'; // webm 지원 브라우저의 경우.
		} else {
			ban_audio.src = audio_src + '.mp3';	// webm 미지원 브라우저의 경우.	
		};

		/*	return this.each()
		*	jQuery 객체로 감싸진 모든 대상요소에 적용합니다.
		*	each()는 Javascript의 for문과 같은 역할을 합니다.
		*/		
		return this.each(function() {	// jQuery 체인 요소에 모두 적용.
			$(this)
				.hover(function() { // 마우스 오버, 아웃에 따른 이벤트 핸들링.
					if(!hovered) { 	// hovered === false일 경우, 처리되는 내용.
                        banner_audio.load(); // 음원 로딩.
						banner_audio.play(); // 음원 재생.
						hovered = true;	// hovered 변경.
					}
				}, function() { 	// hovered === true일 경우, 처리되는 내용.
					banner_audio.pause(); // 음원 일시정지.
					banner_audio.currentTime = 0; // 음원 재생위치 0으로 변경.
					hovered = false;	// hovered 변경.
				});
		});
	};
	
})(window.jQuery);

