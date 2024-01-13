# # # # 문법적 설탕(syntatic sugar)
# # # # comprehension
# # # a = [i**2 for i in range(10)]
# # # double_a = [i**2 for i in range(10)]
# # # num = [i+3 for i in range(10)]
# #
# # #comprehension + condition
# # # a = [i for i in range(99999999999999) if i % 2 ==0]
# # # print(a)
# #
# # #유저에게 정수의 범위를 물어보고
# # # #두 숫자의 정수를 입력받고
# # # #해당 벙위의 정수까지의 공배수의 리스트를
# # # #만드는 프로그램 작성
# # #
# # # word = ['coffee','cookie','sandwich']
# # # a = [len(i) for i in word]
# # # print(a)
# #
# news = """India's first solar observation mission is set to reach its final destination in a few hours.
#
# On Saturday, the space agency Isro will attempt to place Aditya-L1 in a spot in space from where it will be able to continuously watch the Sun.
#
# The spacecraft has been travelling towards the Sun for four months since lift-off on 2 September.
#
# It was launched just days after India made history by becoming the first to land near the Moon's south pole.
#
# India's first space-based mission to study the solar system's biggest object is named after Surya - the Hindu god of the Sun, who is also known as Aditya. And L1 stands for Lagrange point 1 - the exact place between the Sun and Earth where the spacecraft is heading.
#
# According to the European Space Agency, a Lagrange point is a spot where the gravitational forces of two large objects - such as the Sun and the Earth - cancel each other out, allowing a spacecraft to "hover".
#
# L1 is located 1.5 million km (932,000 miles) from the Earth, which is 1% of the Earth-Sun distance. Isro recently said that the spacecraft had already covered most of the distance to its destination.
#
# The year India reached the Moon - and aimed for the Sun
# How important are India's Moon mission findings?
# India makes historic landing near Moon's south pole
# An Isro official told the BBC that "a final manoeuvre" will be performed on Saturday at around 16:00 India time (10:30 GMT) to place Aditya in L1's orbit.
#
# Isro chief S Somanath has said they will trap the craft in orbit and will occasionally need to do more manoeuvres to keep it in place.
#
# Once Aditya-L1 reaches this "parking spot" it will be able to orbit the Sun at the same rate as the Earth. From this vantage point it will be able to watch the Sun constantly, even during eclipses and occultations, and carry out scientific studies."""
# #
# word_List = news.split()
# a = [i for i in word_List if i.isalpha()]
# a.sort()
# # print(a)
# #
#
# #조건문 심화
# # # print([i if i % 2 == 0 else 'A' for i in range(101)])
# # print(['👋' if str(1 % 10) in '369' or str(i // 10) in '369' else i for i in range(1,101)])
#
# a = [i.upper() if len(i) >= 5 else i.lower() for i in a]
# no_repeat_List = [i for i in a if a.count(i) == 1]
# print(a)


# print([i+j for i in range(3) for j in range(3)])
# 1) i:0 j:0
# 2) i:0 j:1
# 3) i:0 j:2

# 1) i:1 j:0
# 2) i:1 j:1
# 3) i:1 j:2

# 1) i:2 j:0
# 2) i:2 j:1
# 3) i:2 j:2

# print([f"{i} * {j} = {i*j}" for i in range(2,10) for j in range(2,10)])

# celsius = [0,10,20,30,40]
# # print([i * 9/5 +32 for i in celsius])
print([i for i in range(100) if i % 2 == 0])


