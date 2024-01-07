exercise = str(input("원하는 운동루틴 써(띄어쓰기)"))
exercise_list = exercise.split()
exercise_list.sort()
print(exercise_list)

neeeews = ("""지난해 미국 방문 당시 불거진 윤석열 대통령의 ‘비속어 발언 보도’와 관련해 외교부가 문화방송(MBC)을 상대로 낸 정정보도 청구소송에서 외부 음성 감정인이 ‘바이든-날리면’ 여부에 대해 “감정 불가”라고 판단했다. 다만 음성 감정인은 윤 대통령이 ‘새끼’라고 한 사실은 확인된다고 했다. 대통령실은 비속어를 쓰지 않았다고 부인한 바 있다.
서울서부지법 민사합의12부(재판장 성지호)는 22일 외교부가 문화방송을 상대로 낸 정정보도 청구소송 마지막 변론기일을 진행했다. 이날 재판부는 지난 19일 나온 윤 대통령 발언에 대한 음성 감정 결과를 확인하고 이에 대한 양쪽의 의견을 들었다. 앞서 외교부는 지난달 31일 윤 대통령의 발언에 대한 감정 신청용 첨부 자료를 제출하고, 지난 2일엔 감정인 선정에 관한 의견서를 제출했다.
그러나 이날 재판에는 음성감정 결과에 대한 양쪽의 직접적인 발언은 등장하지 않았다. 외교부 쪽은 최종 구두변론에서 “저희는 이 사건 보도가 과연 필요성, 당위성 측면에서 급하게 해야 했던 기사인지 의문이다. 피고 쪽은 진실을 밝히는 게 책무라고 하지만, 그 점에서 부족한 점이 있었다는 지적도 있다”라고 했다.
문화방송 쪽은 “해당 보도는 영상만 보고 한 게 아니라 대통령실 확인 공식적으로 거쳐 사실상 시인했기에 보도된 것”이라며 “원고는 대통령 특정 발언이 무슨 말을 한 것이었는지조차 밝히지 않고 영상 기술적 분석만 하고 있다”고 했다.""")

word = input("당신이 찾고 있는 단어는?:")
news2 = neeeews.count(word)
print(f"찾고 싶은 단어 {word}는 {news2}개 있습니다")

email = input("이메일 주소를 입력해주세요")
email1= email.split('@')
print(f"이메일 아이디:{email1[0]},이메일 도메인:{email1[1]}")

word1 = str(input("원하는 문자를 입력하시오"))  #mega
word_list = list(word1)    #[m,e,g,a]
word_list.reverse()
reverse = word = ''.join((word_list))
print(reverse)

word_sort_list = list(word1)
word_sort_list.sort()
sort_word = ''.join((word_sort_list))
print(sort_word)