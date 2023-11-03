import json
from util import parse_attribute_string

# 给定 example_json_str = """{"prefix": "糖糖: 嘿嘿，最近我在想要不要改变直播风格，你觉得我应该怎么做呀？", "options": [{"user": "你可以试试唱歌直播呀！", "reply": "糖糖: 哇！唱歌直播是个好主意！我可以把我的可爱音色展现给大家听听！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做一些搞笑的小品，逗大家开心。", "reply": "糖糖: 哈哈哈，小品确实挺有趣的！我可以挑战一些搞笑角色，给大家带来欢乐！谢谢你的建议！", "attribute_change": "Stress: -1.0"}, {"user": "你可以尝试做游戏直播，和观众一起玩游戏。", "reply": "糖糖: 游戏直播也不错！我可以和观众一起玩游戏，互动更加有趣！谢谢你的建议！", "attribute_change": "Stress: -1.0"}]}"""

# 我希望建立一个DialogueEvent类

# 这个类可以凭空初始化

# 也可以通过DialogueEvent(str)的方式来初始化

# 并且json_str解析后，会以self.data的字典形式存储在类中

# 并且可以通过类似 event["options"]的方式进行调用

# 请用python为我实现

class DialogueEvent:
    def __init__(self, json_str=None, user_role = None):
        if json_str:
            try:
                self.data = json.loads(json_str)
            except json.JSONDecodeError:
                print("输入的字符串不是有效的JSON格式。")
                self.data = {}
        else:
            self.data = {}

        if "Condition" not in self.data:
            self.data["Condition"] = ""

        if "prefix" in self.data:
            self.data["prefix"] = self.data["prefix"].replace("：",":")

        for option in self.data["options"]:
            if "user" in option:
                option["user"] = option["user"].strip(" ：")
            if "reply" in option:
                option["reply"] = option["reply"].replace("：",":")


        if user_role is None:
            self.user_role = "男主"


    def __getitem__(self, key):
        return self.data.get(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return str(self.data)

    def get_most_neutral( self ):
        options = self.data["options"]

        if len(options) == 0:
            print('warning! no options can be selected')
            return 0

        i = 0
        min_change = 99999

        for i, option in enumerate(options):
            attr_change = parse_attribute_string(option["attribute_change"])
            current_change = 0
            for k in attr_change:
                current_change += abs( attr_change[k] )

            if current_change < min_change:
               min_change = current_change
               choice_id = i

        return choice_id


    def transfer_output( self, choice_id ):
        ans = self.data["prefix"] + "\n"
        user_text = self.user_role + ": " + self.data["options"][choice_id]["user"] + "\n"
        ans += user_text
        ans += self.data["options"][choice_id]["reply"] + "\n"

        # print(self.data["options"][choice_id]['attribute_change'])
        return ans

    def most_neutral_output(self):
        return self.transfer_output( self.get_most_neutral() )