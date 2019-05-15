#记录所有的名片字典
card_list = []

def show_memu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print(" ")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print(" ")
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("新增名片")
    print("*" * 50)
    #1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq号码：")
    email_str = input("请输入邮箱：")
    #2.使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    #3.将名片添加到列表里
    card_list.append(card_dict)
    #print(card_list)
    #提示用户添加成功
    print("添加 %s 的名片成功" % name_str)

def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    #判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        return
    #打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t\t")
    print(" ")
    #打印分割线
    print("=" * 50)
    #遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

def serach_card():
    """搜索名片"""
    serach_name = input("请输入要查询的名字")
    for card_dict in card_list:
        if serach_name == card_dict["name"]:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print(" ")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            #针对找到的名片记录执行修改删除的操作
            deal_card(card_dict)
            break
    else:
        print("%s 的名片不存在" % serach_name)
    print("*" * 50)

def deal_card(find_dict):
   action_str = input("请选择要执行的操作： 1 修改 2 删除 0 返回上级菜单")
   if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名[回车不修改]")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话[回车不修改]")
        find_dict["qq"] = input_card_info(find_dict["qq"], "qq[回车不修改]")
        find_dict["email"] = input_card_info(find_dict["email"], "email[回车不修改]")
        print("修改名片成功")
   elif action_str == "2":
        card_list.remove(find_dict)
def input_card_info(dict_value, tip_message):
    #1.提示用户输入内容
    result_str = input(tip_message)
    #2.针对用户输入的进行判断，如果用户输入了内容，直接返回
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
    #3.如果用户没有输入内容，返回'字典中原有的值'