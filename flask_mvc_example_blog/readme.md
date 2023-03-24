startbootstrap-clean-blog-gh-pages : bootstrap example use<br>
url = "mongodb+srv://<id>:<password>~~~~" # write your mongodb url



```
mvc 패턴

model
view (template)
control

1. 사용자가 조작을 한다 (route) (control)
2. model이 갱신된다 (update)
3. 출력한다. (view) (display)

입력 -> 처리 -> 출력
```

```
계획
1. 시나리오 구성
2. 해당 시나리오 필요 엑터 구성
3. 엑터 CRUD 구성
4. 시나리오 개발
```

```
시나리오 (view)
    어드민 로그인 
        1 메인화면
        0 로그인

    메인화면
        list : 카테고리

    카테고리
        list : 게시물
        widget : button : 생성

    게시물
        읽기
        widget : button : 복사
        widget : button : 삭제
        widget : button : 수정
```

```
엑터 (모델)
    계정 CRUD
        계정정보 : 어드민 1개 (sample)
            C : x
            R : o
            U : x
            D : x
    카테고리 CRUD
            C : o
            R : o
            U : x
            D : o
    게시물 CRUD
            C : o
            R : o
            U : o
            D : o
```