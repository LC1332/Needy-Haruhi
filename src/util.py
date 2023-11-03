import re


# 我希望实现一个字符串解析函数，输入是一个string，输出是一个dict，如果字符串中出现
# "Strees:", "Affection:"或者"Darkness:"，则把后面的一个有正负的浮点数作为value，对应的字符串作为key，记录在dict中

# 如果后面是？或者非数字，则记录成0

# example input:
# Stress: -1.0, Affection: +0.5
# example output:
# {"Stress":-1,"Affection":0.5 }

# exmple input:
# Affection: +4.0, Stress: -2.0, Darkness: -1.0
# example output:
# {"Stress":-1,"Affection":0.5 }

# example input:
# Affection: +2.0, Stress: -1.0, Darkness: ?
# example output:
# {"Affection": 2, "Stress": -1, "Darkness": 0 }

# example input:
# Stress: -1.0
# example output:
# {"Stress":-1}

def parse_attribute_string(attribute_str):
    result = {}
    patterns = {
        "Stress": r"Stress:\s*([+-]?\d+(\.\d+)?)?",
        "Affection": r"Affection:\s*([+-]?\d+(\.\d+)?)?",
        "Darkness": r"Darkness:\s*([+-]?\d+(\.\d+)?)?"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, attribute_str)
        if match:
            value = match.group(1)
            if value is None:
                result[key] = 0
            else:
                result[key] = float(value)

    return result

# 我希望实现一个字符串解析函数，输入是一个string，输出是一个tuple，

# max_value = 100，字符串中可能会包含Darkness，Stress或者Affection属性中的一种，

# 如果输入为"Affection 61+", 则输出 ("Affection", 61, 100)

# 如果输入为"Darkness 0-39"，则输出 ("Darkness", 0, 39)

# 输出字符串中包含的属性，区间的最小值和最大值。

# 如果不包含任何属性，则输出None

# example_input:
# Random Noon Event: Darkness 0-39
# example_output
# ("Darkness", 0 , 39)

# example_input:
# Random Noon Event: Stress 0-19
# example_output
# ("Stress", 0 , 19)

# example_input:
# Random Noon Event: Affection 61+
# example_output
# ("Affection", 61, 100)

import re

def parsing_condition_string(s):
    max_value = 100  # 定义最大值
    # 正则表达式匹配'属性 最小值-最大值'或'属性 最小值+'
    pattern = re.compile(r'(Darkness|Stress|Affection)\s+(\d+)(?:-(\d+)|\+)')

    match = pattern.search(s)
    if match:
        attribute = match.group(1)  # 属性
        min_value = int(match.group(2))  # 最小值
        # 如果有最大值就直接使用，没有就用默认的max_value
        max_value = int(match.group(3)) if match.group(3) else max_value
        return (attribute, min_value, max_value)
    
    return None  # 如果没有匹配则返回None
