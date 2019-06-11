# cau_2019_NIPIR_team-project

document 데이터는 raw데이터에서 test set을 제외한 데이터입니다.
rating 별로 특수문자 제거, 형태소 분석 후 word frequency를 계산하였으며 
frequency가 50이하인 word를 제거하였습니다.
pickle 을 이용하여 dictionary로 저장하였습니다.

test 데이터는 raw데이터에서 rating 별로 random하게 100개씩 리뷰를 추출한 데이터 입니다.
_list 파일은 형태소 분석까지 만 진행한 데이터이고
_dict 파일은 형태소 분석후 word frequency를 계산한 데이터입니다
pickle 을 이용하여 list와 dictionary로 저장하였습니다.
