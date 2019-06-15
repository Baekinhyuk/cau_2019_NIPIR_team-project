# cau_2019_NLPIR_team-project

## 팀소개
### 오늘도밤샘각
    조장 : 김현빈
    팀원 : 김민조, 백인혁, 함지훈, 손상혁
 
 
## 프로젝트 소개

### 영화리뷰를 통한 감성분석

#### 감성분석이란?
      주어진 문장에서 사람들의 태도, 의견, 혹은 성향과 같은 정보를 알아내는 기법
      
#### 목적
     우리는 새로운 영화리뷰가 들어왔을 때, 그 리뷰의 점수가 긍정(10~8점) or 부정(1~3점)인지 예상합니다.
             
## 진행과정

### 영화리뷰 분석

    1.KoNLPy의 OKT분석기를 사용하여 형태소 분해
    
### 여러가지 CASE의 vsm 제작
   ![image](https://user-images.githubusercontent.com/33536706/59546397-ad18d500-8f67-11e9-984f-760fc8d52e4b.png)
    
    case1. : 전처리 하지않고 그대로 사용
    case2. : 등장빈도 50번 미만인 단어들 제거, 의미없는 특수문자 제거, 정규화
    case3. : case2 + 레이팅과 상관없이 유사하게 등장한 단어들 제거
    
    
### tf 방식비교
   ![KakaoTalk_20190612_195016569](https://user-images.githubusercontent.com/33536706/59546405-cb7ed080-8f67-11e9-9a34-c5111232f5bf.png)

    Tf 방식에 따른 정확도를 확인해 보고자, n(natural)방식과 a(argmented)방식 2가지를 선택해 비교해보았다.


## 결과

|  <center> </center> |  <center>case1</center> |  <center>case2</center> |  <center>case3</center> |
|:--------|:--------:|--------:|--------:|
|<center>Tf-n </center> | <center>0.678</center> |<center>0.685</center> |<center>0.744</center> |
|<center>Tf-a </center> | <center>0.66</center> |<center>0.688</center> |<center>0.751</center> |
    
    
## 결과분석
    Case 1과 Case 2의 경우, tf-idf값을 적용하지 않고, tf값만을 이용하고 50번 이상 등장한 단어들만 모은 경우다 보니,
    단순 tf값을 비교한다는 한계점은 여실히 보여주게 됨
    VSM을 단순하게 빈도수를 이용해 줄인 건 정확도면에서 크게 의미가 없다.
    
    반면 Case 3의 경우 idf값을 사용하지 않는 대신, 모든 문서에서 공통적으로 비슷한 비율로
    등장한 단어를 찾아 제거해 준 결과 case 1, 2에 비해서 정확도가 올라가는 효과가 존재한다.


    
