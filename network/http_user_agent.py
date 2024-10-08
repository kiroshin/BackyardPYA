#  http_user_agent.py
#  Created by Kiro Shin <mulgom@gmail.com> on 2023.

USER_AGENT_MOBILE = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1"
USER_AGENT_DESKTOP = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"

#
# User-Agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
#   - Mozilla/5.0       : 접속한 브라우저가 Mozilla와 호환.
#   - platform          : 브라우저가 실행되는 운영체제 환경
#   - rv: geckoversion  : Gecko 버전
#   - Gecko/geckotrail  : 브라우저가 Gecko 기반인지 여부. 데스크탑일 경우 geckotrail은 20100101이라는 스트링값으로 고정된다.
#   - Firefox/firefoxversion : 브라우저가 파이어폭스라는 의미 그리고 파이어폭스의 버전.
#
#
# Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15
# Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.6 Mobile/15E148 Safari/604.1
# Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1
