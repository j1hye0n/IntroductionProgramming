class Order :
    shop_name='SnowCafe'
    dict_prices={'아메리카노':3000, '카페모카' : 4000, '케이크' :5000}

    def __init__(self, num_table, name_customer ):
        self.num_table = num_table
        self.name_customer = name_customer
        self.order = dict()

    def display_info(self):
        print('*** 주문 현황 ***')
        print('테이블 {}반'.format(self.num_table))
        print('고객 이름 : {}'.format(self.name_customer))
        print('주문 현황 : {}'.format(self.order))

    def display_menu(self) :
        print('*** {}님, {}에서 주문 가능한 메뉴입니다. ***'.format(self.name_customer,self.shop_name))
        for key in self.dict_prices :
            print('{}: {}'.format(key,self.dict_prices{key}))
        print('*****************************************')

    def place_order(self, menu, quantity) :
        print('{}님이 {}번 테이블에서 {} {}개 주문이요.'.format(self.name_customer,self.num_table,menu,quantity))
        if menu not in self.order :
            self.order[menu] = 0
        self.order[menu] = self.order[menu] + quantity
    
    def calculate_total(self) :
        total_price = 0

        for menu, quantity in self.order.items() :
            price = self.dict_prices[menu]
            total_price += price*quantity

        return total_price
    
    def join(self, other) :
        print('{}번 좌석과 {}번 테이블의 주문을 합치겠습니다.'.format(self.num_table, other.num_table))
        for menu, quantity in other.order.items() :
            self.place_order(menu, quantity)

    # def __del__(self) :
    #     print('{}번 테이블 판매가 끝났습니다. {} 고객님, 감사합니다.'.format(self.num_table, self.name_customer))

        # print(f'{self.name_customer} 고객님 환영합니다.')


# order1 = Order(1, 'hha')  ## class 호출
# order1.place_order('카페모카',1) ## 주문
# order1.display_info() ## 주문 내역 확인