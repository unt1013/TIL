# git 설정 순서

> - 기본적으로 작업 전에 pull, 작업 후에 push 하는 것을 원칙으로 한다
>
>   ```bash
>   $ git pull origin master
>   $ git push origin master
>   ```



## git 디렉토리 설정 방법

> - 자신의 디렉토리 중 하나를 마스터브랜치로 설정한다
>
>   ```bash
>   $ git cd MasterDirectory
>   ```
>
> - 폴더를 깃으로 관리하겠다고 선언한다
>
>   ```bash
>   $ git init
>   ```
>
> - 작업 후 변경사항을 add, commit, push 한다
>
>   ```bash
>   $ git status
>   $ git add blahblah
>   $ git commit -m "blahblah"
>   $ git push origin master
>   ```
>
> - 원격 저장소에서 url 을 받아와 clone을 생성한다
>
>   ```bash
>   $ git clone url
>   ```
>
> - git Project 안에 다른 git Project를 중첩시키지 않도록 한다

