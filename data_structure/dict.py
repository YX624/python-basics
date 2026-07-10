#定义字典---{key:value}---（key不能重复，若重复，后面的只会覆盖前面的值）
# key必须是不可变类型（str,tuple,int,float)
# dict1={'王琳':670,'离散':580,'uiy':592}
# print(dict1)
# print(type(dict1))
# a=dict1['离散']
# print(a)
# dict1['yu']=598
# print(dict1)
#
# del dict1['yu']
# print(dict1)
#
# c=dict1.get("uiy")
# print(c)
# dict1['uiy']=236
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]}:{item[1]}")

#案例---->购物车管理系统
shopping_cart={}

print("欢迎使用购物车管理系统~")

menu="""
######### 购物车管理系统 ##########
#         1.添加购物车           #
#         2.修改购物车           #
#         3.删除购物车           #
#         4.查询购物车           #
#         5.退出购物车           #
################################

"""

while True:
    # 1.制作菜单

    # 2.具体执行操作
    choice = input("请选择你要执行的操作: ")
    match choice:
        case "1":  # 添加购物车
            goods_name = input("请输入商品的名称：")
            goods_price = float(input("请输入商品的价格："))
            goods_num = input("请输入商品的数量：")

            if goods_name in shopping_cart:
                print("商品已添加")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕")

        case "2":  # 修改购物车
            goods_name = input("请输入要修改商品的名称：")
            goods_price = float(input("请输入商品最新的价格："))
            goods_num = input("请输入商品最新的数量：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改完毕")

        case "3":  # 删除购物车
            goods_name = input("请输入要删除的商品名称：")

            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")

        case "4":  # 查询购物车
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name}, 商品价格：{goods_info["price"]}, 商品数量：{goods_info["num"]}")

        case "5":
            print("Bye~")
            break
        case _:
            print("非法操作不支持")

























