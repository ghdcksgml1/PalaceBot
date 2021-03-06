# <img width="33" alt="스크린샷 2021-07-21 오전 1 25 13" src="https://user-images.githubusercontent.com/79779676/126360636-a72e245a-bc2e-4626-b23b-c414e3e1da04.png"> PALACE BOT (Windows 10) <img width="33" alt="스크린샷 2021-07-21 오전 1 25 13" src="https://user-images.githubusercontent.com/79779676/126360693-1ed3982b-28d3-4f29-a538-7a35b8260b91.png">

<br/><br/>


<img width="948" alt="스크린샷 2021-07-21 오전 1 22 35" src="https://user-images.githubusercontent.com/79779676/126360274-f77f8238-76d8-4c8e-b5fe-374f25c3b1cb.png">


<br/><br/><br/>

## <img width="32" alt="스크린샷 2021-07-21 오전 1 27 38" src="https://user-images.githubusercontent.com/79779676/126360982-1201ecc6-0e87-4826-afee-9fe21e2854e1.png"> 프로젝트를 진행하게 된 계기 <img width="32" alt="스크린샷 2021-07-21 오전 1 27 38" src="https://user-images.githubusercontent.com/79779676/126360982-1201ecc6-0e87-4826-afee-9fe21e2854e1.png">

<br/><br/>

저는 옷 중에서 **'PalaceSkateBoards'** 라는 브랜드의 옷을 가장 좋아하고 즐겨 입습니다.

이 브랜드의 매력은 시즌별로 옷을 한정판매 한다는 점입니다.

이 브랜드의 옷을 구매하기 위해서는 [팔라스 공식홈페이지](https://shop.palaceskateboards.com/) 에서

정해진 시간 (토요일 / 00:00)에 새로운 상품이 추가되어 선착순으로 주문을 해 가져가는 방식입니다.

구매방식이 선착순인 탓에 손이 빠른사람이 상품을 구매할 확률이 높습니다.

저는 손이 느려 많이 실패해서, 원가에 프리미엄 가격을 붙여파는 리셀(resell)로 상품을 많이 구매했습니다.

**'나도 정가에 구매해보자'** 라는 생각으로 이 프로젝트를 진행하게 되었습니다.

<br/><br/><br/>

## <img width="34" alt="스크린샷 2021-07-21 오전 2 13 44" src="https://user-images.githubusercontent.com/79779676/126367076-88232979-61e2-40dc-bd12-8c5131ba072f.png"> 사용 기술 <img width="34" alt="스크린샷 2021-07-21 오전 2 13 44" src="https://user-images.githubusercontent.com/79779676/126367084-bc671469-1b6f-49a9-a686-72cda0646b78.png">

<br/><br/>

### ![icons8-python-48](https://user-images.githubusercontent.com/79779676/126363111-57fdad9e-f8e6-4d4f-908d-2dc0dba9a606.png)Python 3.9 + Module ( selenium, bs4, tkinter )
### ![icons8-google-48](https://user-images.githubusercontent.com/79779676/126363753-5eded8a9-8dee-4b0f-9906-bfca4d24ac78.png) chormedriver

- 설치되어 있는 크롬의 버전과 설치할 webdriver의 버전이 일치해야 합니다. ( 오류의 원인 )

<img width="1192" alt="스크린샷 2021-07-21 오전 2 33 07" src="https://user-images.githubusercontent.com/79779676/126369549-8f36df56-9b23-4e6e-80a2-1162128bf9e1.png">

<br/>

### 다운로드 링크
* python : https://www.python.org/downloads/
* chrome driver : https://chromedriver.chromium.org/downloads

<br/><br/><br/>

## <img width="34" alt="스크린샷 2021-07-21 오전 2 15 38" src="https://user-images.githubusercontent.com/79779676/126367395-8d351fb2-0078-4eda-aa2b-0def6d391270.png"> 진행 과정 <img width="34" alt="스크린샷 2021-07-21 오전 2 15 38" src="https://user-images.githubusercontent.com/79779676/126367385-f0577050-fe0e-4a56-9c2a-b4829db34982.png">

<br/><br/>

처음에는 팔라스 봇을 만들고 싶다고 생각만 했을 뿐 어떤 기술을 이용해 만들어볼지는 생각을 하나도 하지 못했습니다.

단순하게, 마우스로 클릭해서 카트에 담고 결제를 하면되니까 마우스를 자동으로 클릭해주는 프로그램을 찾아보자! 라고 해서 찾은게

오토핫키 (Auto HotKey) 였습니다. 하지만, 오토핫키로는 다양한 변수들이 생겼을 때의 대응을 하기 힘들었습니다.

<br/>

그렇게 세월을 보내다가 한 강의를 접하게 되었습니다.

[나동빈님 selenium 강의](https://www.youtube.com/watch?v=UenvOvag0B4) 를 보고서 selenium으로 팔라스 봇을 만들어봐야겠다는

> 생각이 딱 들었습니다. 처음에는 소스코드로만 구현해서 상품이나 사이즈를 바꾸려면 직접 파일을 열어 바꿔줘야 했기 때문에 불편함이 있었다. (V.1.0)

<br/><br/><br/>

> 하지만, 대학교 1학년 때 Python 수업에서 배운 tkinter를 이용해 조금은 허접하지만 사용자가 원하는 입력값을 넣을 수 있게 GUI를 구현해봤다. (V.1.1)

![image](https://user-images.githubusercontent.com/79779676/126366291-8a3eae4c-253a-46e9-8a7a-d5c47332758a.png)

<br/><br/><br/>

> **+추가** 이번에 Desktop을 MacOS 로 바꿔서 Mac 버전 추가 , wevdriver의 경로를 선택할 수 있는 버튼 추가 (V.1.2)

<img width="595" alt="스크린샷 2021-07-21 오후 8 59 00" src="https://user-images.githubusercontent.com/79779676/126485208-8290b8c1-0d77-45bc-9af6-6396667c453b.png">

<br/><br/><br/>

> **+추가** 이번 버전에서는 UI개편과 기능에따라 Frontend.py와 Backend.py로 나누었습니다. 실행은 frontend.py로 실행해주세요. (V.1.3)

<img width="595" alt="Screen Shot 2021-08-04 at 11 28 29 AM" src="https://user-images.githubusercontent.com/79779676/128112423-8d85d541-6f4b-44f1-9199-67d453a53c7b.png">

향후 추가해볼 기능은 PALACESKATEBOARDS 홈페이지의 PREVIEW에서 상품을 클릭하면,

상품 이름이 자동으로 ITEM의 textbox에 기록되는 기능을 추가하려고합니다.

아직 공부가 많이 필요해서 해당 기능은 시간이 조금 걸릴 것 같습니다.

## <img width="33" alt="스크린샷 2021-07-21 오전 1 25 13" src="https://user-images.githubusercontent.com/79779676/126367492-febbd146-e20d-4c84-8951-3b75498596fd.png"> 작동 원리 <img width="33" alt="스크린샷 2021-07-21 오전 1 25 13" src="https://user-images.githubusercontent.com/79779676/126367503-bdca280b-5a98-403e-9116-d696c03aa8b7.png">

<br/><br/>
 
작동 원리는 정말 간단합니다. 

1. Python을 이용해 chrome webdriver로 크롬 브라우져를 켠다.
2. [팔라스 공식 홈페이지](https://shop.palaceskateboards.com/) 로 들어간다.
3. 입력해둔 상품을 찾아 들어간다.
4. 사이즈를 선택한 뒤 카트에 담는다.
5. 카트를 클릭해 결제 창으로 들어간다.
6. 입력해둔 결제 정보 (주소, 전화번호 등)을 입력시킨다.
7. 로봇인지 아닌지 검사하는 창이 뜨면 그때부터 사용자가 문제를 푼 뒤 결확인 버튼만 눌러준다.

<br/><br/><br/>

## <img width="32" alt="스크린샷 2021-07-21 오전 1 27 38" src="https://user-images.githubusercontent.com/79779676/126369268-4549562e-f66c-4e03-b9a7-698223c322ad.png"> 작동 영상 <img width="32" alt="스크린샷 2021-07-21 오전 1 27 38" src="https://user-images.githubusercontent.com/79779676/126369282-37593aa1-c618-427c-bf99-b246ea1d720f.png">

<br/><br/>

[![홍찬희](http://img.youtube.com/vi/7eU2HVaY0HM/0.jpg)](https://youtu.be/7eU2HVaY0HM?t=0s) 

<br/><br/>

### 실제 구동 영상

ㅋㅋㅋㅋㅋㅋ 바로 봇에 막혔씁니다!

링크 : https://www.youtube.com/shorts/aC9IFRwePeI

<br/><br/>


* **조회 버튼** - chrom webdriver를 실행 시킨 뒤, [팔라스 공식홈페이지](https://shop.palaceskateboards.com/) 로 들어갑니다. 
* **시작 버튼** - label에 모든 정보를 입력하고 시작 버튼을 클릭하게 되면, 새로운 상품이 갱신되기 전에는 [상품개시 전 이미지](https://user-images.githubusercontent.com/79779676/126430857-8739641e-6e55-4b55-8ea8-0b131dc2d3d2.png) 와 같이 화면이 뜹니다. 정시에 상품을 구매할 수 있는 창이 뜨게 되므로, [상품개시 후 이미지](https://user-images.githubusercontent.com/79779676/126431038-4aa5832d-f0dd-4bc8-a429-c768315ca214.png) 가 뜰때까지 계속 새로고침을 한 후, 공식 홈페이지가 뜨게 되면 상품을 찾아 결제 창까지 이동해줍니다.



<br/><br/><br/>

## <img width="34" alt="스크린샷 2021-07-21 오전 2 13 44" src="https://user-images.githubusercontent.com/79779676/126369299-afe12980-2af2-4cc5-ab1d-3e325e654286.png"> 오류발생 원인 <img width="34" alt="스크린샷 2021-07-21 오전 2 13 44" src="https://user-images.githubusercontent.com/79779676/126369325-d7e8a2fb-3396-46c8-81b0-49211a240a64.png">

<br/><br/>

### 🚀 모듈 미설치


모듈을 설치하지 않으면 동작하지 않습니다.


    필수 모듈 : selenium, bs4, tkinter


<br/>


### 🚀 크롬과 크롬드라이버의 버전이 다름


크롬 드라이버를 최신버전으로 깔았을 때


크롬과 버전이 다르면 실행이 되지 않습니다.


따라서, 크롬에 옵션으로 들어가 버전을 확인 후 버전에 맞는 크롬 드라이버 설치를 하시기 바랍니다.


~~크롬 웹드라이버는 다음과 같은 경로에 저장해주세요.~~


~~C:\Chrome_Driver\chromedriver.exe~~


<br/>

### 🚀 new 상품 카테고리의 하단에 있는 상품으로 설정

보통 모자같은 악세사리류는 하단에 스크롤해서 내려야나오기 때문에

스크롤 하지 않은 상태에서의 상품만 카트에 담을 수 있습니다.

<br/>

### 🚀 chrome_driver MacOS에서 다음과 같은 오류가 뜨면서 실행이 되지 않을 때

<img width="200" alt="스크린샷 2021-07-21 오후 8 35 55" src="https://user-images.githubusercontent.com/79779676/126482660-621f3f7c-bd04-4741-8839-77a0a959071f.png">

MacOS의 보안 정책 때문에 낯선 곳에서 다운받은 파일을 변형시켜 실행시키는데 제한되기 때문에 오류가 뜨게 됩니다.

webdriver가 설치된 경로까지 이동합니다. ex) 저같은 경우는 /Desktop/Chrome_driver/ 가 웹드라이버의 위치입니다.

    $ cd /웹드라이버 설치 경로/
    
권한 설정을 바꿔 줍니다.

    $ sudo chmod -R 755

<br/><br/><br/>

## <img width="34" alt="스크린샷 2021-07-21 오전 2 15 38" src="https://user-images.githubusercontent.com/79779676/126370281-2922dfd4-66b8-4fa7-9217-54b5e2b6b48e.png"> 느낀점 <img width="34" alt="스크린샷 2021-07-21 오전 2 15 38" src="https://user-images.githubusercontent.com/79779676/126370288-c38a1cab-677e-4b1a-938d-37d3e18ce976.png">

<br/><br/>

몇년 전부터 계속 만들어보고 싶었던 프로그램을 내 손으로 직접 만들어 보았다.

내가 원하고 재밌는 일을 하니까 몇 시간이 걸리고, 어떤 오류가 뜨더라도 지치지 않을 수 있었다.

일상에서 불편하고 어려웠던 것을 이렇게 프로그래밍적으로 해결해 나가는게 정말 재밌고, 성취감도 많이 느낀다.

누군가에게는 허접한 프로그램으로 보일 순 있지만, 그동안 시행착오를 거쳐오면서 처음으로 끝낸 프로젝트라 너무 뜻깊은 프로젝트였다.

<br/><br/>

* * *
