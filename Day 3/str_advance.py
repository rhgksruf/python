# #문자열 연산
# #1) 연결 (+)
# a = ('123')
# b = ('123')
# c = a + b#123123
# #2)반복
# d = "축의금 10만"
# print(d*3)
#
# #3) 인덱싱(색인)
# coffee = "americano"
# coffee[0]
# print(coffee[-1])
#
# #4) 슬라이싱
# test = "python"
# print(test[1:3]) #  1 2
#
# #문자열 함수
# #1. 대문자화, 소문자화
# mega= 'megastUdy'
# upper_mega = mega.upper() #대문자화
# lower_mega = mega.lower() #소문자화
#
# #2.all 대문자 입니까? all 소문자 입니까?
# isMegaAllLower = mega.islower() #모두 소문자
# isMegaAllUpper = mega.isupper() #모두 대문자
#
# #3. 공백 제거
# marriage = "오늘 결혼식 추카"
# newMarriage = marriage.strip()
# # print(newMarriage)
#
# #4. split 찢다 리스트
# con = "오늘!결혼!축하해!"
# test = con.split("!")
# print(test)
#
# num = """22일 여권에 따르면 비대위 내 여성 위원 후보로는 지난달 국민의힘에 영입된 이수정 경기대 범죄심리학과 교수가 유력하게 거론되고 있다. 한 전 장관과 이 교수는 성범죄 재발 방지책의 필요성에 한목소리를 낸 바 있다. 한 전 장관이 올해 10월 고위험 성범죄자의 거주지를 제한하는 ‘한국형 제시카법’을 입법 예고했을 때도 이 교수는 “국민의힘 성폭력대책특위에서 활동하면서 요구했던 보호수용법이 변형된 것”이라며 환영 입장을 내놨다.
# """
# test1 = num.split()
# print(test1)
#
# #5.replace 대신 넣기
# article = """The move is more than just a change of date from 7 January - the date for Christmas in the Julian calendar, which Russia uses.
#
# It's the continuation of a significant cultural shift in the country - the latest attempt to eradicate Moscow's influence in Ukraine.
#
# The adoption of the Western, Gregorian calendar is also a sign of Kyiv's continuing bid to align itself with Europe.
#
# Whether in war or peacetime, Christmas always comes.
#
# Klavdievo-Tarasove's decorations factory, in a small town outside Kyiv, used to be one of three which supplied the whole of the Soviet Union.
#
# "We used to have many people - not any more," Leokadia tells us. She's worked on this production line since 1978.
#
# She effortlessly blows glass baubles using a gas burner fixed to her desk. It's a welcome source of heat in these cold, industrial surroundings."""
# newArticle = article.replace("Ukraine", "Russia")
# print(newArticle)
#
# #find (찾기), rfind(뒤에서 찾기)
# location = article.find("Leokadia")
# print(location)


#7. startswith (시작),endswith()

#8.join (연결) ❗
# menu = ['아아', '라떼','디카페인']
# result = '매우'.join(menu)
# print(result)

article1 = """토요일인 23일에도 영하 10도를 밑도는 최강 한파가 이어질 전망이다. 다만 오후부터는 기온이 올라 추위가 다소 누그러질 것으로 보인다.
기상청 자료를 보면, 아침 기온은 수도권을 비롯해 강원 내륙과 산지, 충청 북부, 경북 북부 내륙은 영하 15도 안팎, 그 밖의 중부지역과 남부 내륙은 영하 10도 안팎을 보이겠다.
최근 며칠 간 이어졌던 강추위는 이날 아침까지 여전하다가 낮부터 점차 기온이 오를 전망이다. 예보된 낮 최고기온은 -3~5도다. 다만, 평년(최고 3~10도)보다는 낮다.
전국이 대체로 맑겠고 오후부턴 가끔 구름이 많을 전망이다. 전라권과 제주도는 대체로 흐리다..전라 서해안은 늦은 새벽까지, 제주도는 아침까지 눈이 올 것으로 보인다.
예상 적설량은 전북 서해안·전남 서해안 2∼7㎝, 제주도 산지는 3∼8㎝, 산지를 제외한 제주도는 1∼5㎝다.
미세먼지 농도는 원활한 대기 확산으로 전국이 ‘좋음’에서 ‘보통’ 수준을 보이겠다."""

# word = input("넣고 싶은 단어:")
# new = article1.replace(' ', ' '+word+' ')
# result1 = '꿀잼'.join(word)
# print(new)



#9. is 시리즈
# isdigit(), isalpha(), isalnum()

#10. count 단어 세주기
a = article1.count("영하")
# print(a)









