# SSS slack bot

이 Repository는 SSS Slack에 있는 SSS bot을 위해 만들어졌습니다.

`Issues`나 `Pull requests`를 통해서 여러 기능을 추가해주세요.

문의사항은 vaporize93@gmail.com으로 보내주세요.

# Usage

slack에서 Bot을 추가한 뒤에 나오는 token `config.py`파일의 `SLACK_TOKEN`에 넣어주세요.
이후 아래와 같이 실행해 주세요.
```shell
$ pip install -r Requirements.txt
$ python bot.py
```

슬랙에 접속해서 봇에게 DM이나 봇이 있는 채널에서 명령을 내리면 됩니다.
`![명령]` 명령은 apps에 있는 `.py`파일명과 동일합니다.
