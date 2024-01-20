# class BankAccount:
#     def __init__(self,number,name,money):
#         self.a = number
#         self.b = name
#         self.c = money
#
#     def deposit(self, money):
#         self.c += money
#         print('입금')
#
#     def withdraw(self, money):
#         if(self.c < money):
#             print('잔고가 부족합니다')
#     def checkBalance(self):
#         print(f"잔액은 {self.c} 남았습니다")
#
# jeon = BankAccount(100,'jeon',1000000)
#
# jeon.deposit(50000)
# jeon.checkBalance()
# jeon.withdraw(500000)
# jeon.withdraw(30000)
# jeon.checkBalance()


class Cart:
    def __init__(self):
        self.itemList = []
        self.total = 0

    def addItem(self, item):
        self.itemList.append(item)
        print(f"{item['name']}추가")
    def removeItem(self):
        for index, item in enumerate(self.itemList):
            print(f"{index}. {item}")
        num = int(input("삭제할 상품의 번호를 선택하세요:"))
        self.itemList.pop(num)
        print('삭제 되었습니다')
    def totalAmout(self):
        total = 0
        for i in self.itemList:
            total += i['price']
        print(f"총 금액은 {total}입니다")




myCart = Cart()
myCart.addItem({'name':'샴푸','price':5000})
myCart.addItem({'name':'린스','price':10000})
myCart.addItem({'name':'트리트먼트','price':8000})
myCart.addItem({'name':'에센스','price':7000})
myCart.removeItem()
myCart.totalAmout()