movie = {
   1: { 'name': '일반영화',
    'price': 10000,
       },
    2: {'name': '3D영화',
       'price': 12000
       },
    3: {'name': '4DX영화',
       'price': 15000,
       }
}
sit = {
    1: {'price': 0,
       },
    2: {'price': 3000,
       },
    3: {'price': 5000,
       }
}
snack = {
    1: {'price': 3000,
       },
    2: {'price': 5000,
       },
    3: {'price': 8000,
       },
}

choice0 = int(input('당신이 원하는 영화의 종류를 말하시오(1.일반영화,2.3D영화,3.4DX영화)'))
choice1 = int(input('당신이 원하는 좌석등급을 말하시오(1.일반석,2.프리미엄석,3.VIP석'))
choice2 = int(input('당신이 원하는 간식 콤보 옵션을 말하시오(1.기본콤보,2.프리미엄 콤보,3.VIP콤보'))
age = int(input('당신의 나이를 입력하시오'))

if age <= 12:
    print(f"""당신이 고르신 영화는 {movie[choice0]['name']}이고 총 가격은 {(sit[choice1]['price']+snack[choice2]['price']+movie[choice0]['price'])*0.5} 입니다""")
elif 13 < age < 18:
    print(f"""당신이 고르신 영화는 {movie[choice0]['name']}이고 총 가격은 {(sit[choice1]['price']+snack[choice2]['price']+movie[choice0]['price'])*0.8} 입니다""")
elif age >= 65:
    print(f"""당신이 고르신 영화는 {movie[choice0]['name']}이고 총 가격은 {(sit[choice1]['price']+snack[choice2]['price']+movie[choice0]['price'])*0.7} 입니다""")
else:    print(f"""당신이 고르신 영화는 {movie[choice0]['name']}이고 총 가격은 {sit[choice1]['price'] + snack[choice2]['price'] + movie[choice0]['price']} 입니다""")