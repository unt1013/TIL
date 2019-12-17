# git 설정 순서

> - 기본적으로 작업 전에 pull, 작업 후에 push 하는 것을 원칙으로 한다
>
>   ```bash
>   $ git pull origin master
>   $ git push origin master
>   ```



## git 디렉토리 설정 방법 - (1) 처음 시작하기

> - 자신의 디렉토리 중 Master로 설정할 폴더로 이동한다
>
>   ```bash
>   $ cd Master
>   ```
>
> - 폴더를 깃으로 관리하겠다고 선언한다 ( Master 선언 )
>
>   ```bash
>   $ git init
>   ```
>
> - 폴더에 원격저장소를 연결시킨다
>
>   ```bash
>   $ git remote add origin url
>   ```
>
> - 자신의 정보를 갱신시킨다
>
>   ```bash
>   $ git config--global user.email "github email"
>   $ git config--global user.name "name"
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



## git 디렉토리 설정 방법 (2) 작업 중 설정하기

> - 저장소에 있는 파일을 pull 해온다
>
>   ```bash
>   $ git pull origin master
>   ```
>
> - 수정하고 push 한다
>
>   ```bash
>   $ git push origin master
>   ```

