# CLI

Commend Line Interface

# 터미널 명령어들

- `ls`  : 폴더 내부의 파일 & 폴더를 나열해 준다
  - `-a` 를 붙이면 숨김 파일 & 폴더까지 볼 수 있다
- `pwd` : 현재 폴더 경로를 출력해준다
- `mkdir` [폴더 명] : 폴더 생성
- `cd` [폴더 명] : Change Directory. 폴더 변경
- `cd ..` : 상위 폴더로 이동
- `git init` : 깃 시작 명령어
- `git status` : 깃의 현재 상태를 알려준다
- `touch [파일 명]` : 파일을 생성한다
- `rm [파일 명]` : 파일을 삭제한다
  - `-r` : 폴더를 삭제한다
- `git add` : 파일을 스테이지에 올린다
- `git commit -m "message"` : 메시지로 설명하고 커밋한다
- `git config--global user.email 깃허브 가입 "이메일"` : github 이메일 설정
- `git config--global user.name "이름"` : 사용자 이름 설정
- `git log` : 커밋에 대한 정보를 가져올 수 있다
  - `git log --oneline` : 한줄로 로그를 뽑는다
- `git checkout 커밋명` :  해당 커밋까지 돌아간다
- `git checkout master` : 다시 원상태로 돌린다
- `git remote` : 원격 저장소 관련 명령어 접두사
  - `add "별명"` : 저장소 별명을 지어 연결한다
  - `-v` : 저장소 상태를 본다
- `git push "별명" "master"` 저장소에 파일을 푸시한다
- `git clone` : 저장소에 있는 자료를 받아오는 기능
- `mv A/ B` : A 파일/폴더를 B 파일/폴더로 이동시킨다.
- `git branch` : 현재 존재하는 branch 확인 가능
- `git branch "이름"` : branch 생성
  - `git branch -d "이름"` : 삭제
- `git switch "이름"` : branch 변경
-  `git merge "병합할 branch 이름"` :  병합