
class restaurant():
    def __init__(self):
        """
        nutrition
        """
        # (In grams / kilograms)
        self.carbohydrate = [7.5]
        self.protein = [1, 1.5]
        self.fat = [1, 1.5]

        # vitamin (In milligrams)
        self.vitaminA = [0.8]
        self.vitaminB3 = [10]
        self.vitaminB6 = [1.2]
        self.vitaminC = [100]
        self.vitaminD = [0.0005, 0.01]
        self.vitaminE = [12]

        # inorganic salt (In milligrams)
        self.calcium = [800, 1000]
        self.sodium = [1500, 2300]
        self.potassium = [2000]
        self.chlorine = [1.5]    
        self.iron = [10, 20]
        self.zinc = [12, 16]
        self.phosphorus = [700, 900]
        self.magnesium = [300, 350]
        self.copper = [2]

        # inorganic salt (In grams)
        self.iodine = [150]
        self.selenium = [50]
        self.chromium = [50]

        # (In grams)
        self.cellulose = [10, 30]

    def welcome(self):
        # print('欢迎来到 -味の力 ⭐ 定义- 美食餐厅')
        print('欢迎来到 --味の力 * 新定义-- 美食餐厅')
        print('您可以下单喜欢的菜品')

    def receipts(self):
        tea = {'苏式龙井茶'}
        juice = {'蜂蜜柠檬茶': "honney:60g, lemmon:50g"}
        print('1. 苏式龙井茶 2. 柠檬蜂蜜茶')
    

    def ingredients(self):
        # change to sql charts later
        # the unit of ingredients need to in accordance with the unit of nutrition
        lemmon = {'heat': 358,
                  'carbohydrate': 81.8,
                  'fat': 3.1,
                  'protein': 1.5,
                  'cellulose': 1.3,
                  'vitaminA': 0.010, 
                  'vitaminB1': 0.05,
                  'vitaminB2': 0.07,
                  'vitaminB3': 0.7,
                  'vitaminB12': 0,
                  'vitaminC': 25,
                  'vitaminE': 1.14,
                  'folicaci': 0,
                  'calcium' : 105,
                  'magnesium': 39,
                  'iron': 1.8,
                  'potassium': 237,
                  'zinc': 1.02,
                  'selenium': 0.65,
                  'iodine': 0
                 }
        honney = {'heat': 321,
                  'carbohydrate': 75.6,
                  'fat': 1.9,
                  'protein': 0.4,
                  'cellulose': 0,
                  'vitaminA': 0, 
                  'vitaminB1': 0,
                  'vitaminB2': 0.05,
                  'vitaminB3': 0,
                  'vitaminB12': 0,
                  'vitaminC': 3,
                  'vitaminE': 0,
                  'folicaci': 0,
                  'magnesium': 2,
                  'calcium' : 4,
                  'iron': 1,
                  'potassium': 28,
                  'zinc': 0.37,
                  'selenium': 0.15,
                  'iodine': 0,
                 }

    def calculate(self):
        """
        加一个菜就把菜的各组成成分输入进程序进行计算 传参a, b, c, d, e ...
        """
        # a.protein.content + b.protein.content
        total_protein = 1.5 * (50/100) + 0.4 * (50/100)

        # times weights
        expected_protein = ((self.protein[0] + self.protein[1]) / 2) * 60
        percent_protein = (total_protein / expected_protein) * 100
         
        print("蛋白质摄入量占一天总蛋白质摄入量的%.2f%%" % percent_protein)
        print("...")

    def viewer(self):
        print("各项营养成分的充能柱状图")


myrestaurant = restaurant()
myrestaurant.welcome()
myrestaurant.receipts()
myrestaurant.calculate()
myrestaurant.viewer()