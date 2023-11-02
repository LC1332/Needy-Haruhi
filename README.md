# Needy-Haruhi
AIGC-Galgame via Dynamic Memory


# Agent

用于记录糖糖当前的状态，暂时感觉是一个字典也可以
可以使用
agent["Attribute_Name"]的方式进行set和get属性

apply_attribute_change( attribute_change )


# DialogueEvent
DialogueEvent Data和memory是相关的，用来记忆

- Name， Event的Name
- Prefix， 糖糖的问话
- Options，预设的选项，其中每个选项包括
  - User_Message 用户的对话
  - Reply 糖糖的回复
  - Attribute_Change 这个选项下糖糖的属性修改
- Condition 这个还没想好，事件出现的condition，不行就复用原游戏的设定。condition可以根据当前的Attribute_Change来指定输出不同的DialogueEvent。

当然我们也支持用户的自由对话
这个时候reply由chatbot给出， attribute_change由evaluator给出

# AttributeChange

用一个dict表示 比如{"Stress":1, "Darkness":-1}
DialoguePlayer

- init 或者load 会载入一个dialogueEvent，这样就可以进一步游玩了
- get_prefix 获得prefix， 同时在history中append prefix
- render_options  获得需要给玩家回复的选项 这里具体是输出str还是输出list of str要到时候看一下
- chat(text) 这里会回复response，如果玩家选择text， 会同时将text和response append 到history
- get_attribute_change() 评估当前history下，对角色产生的影响（原则上只在len(history)>=3的时候运行)
- self.chatbot 这个类需要依赖一个chatbot来获取回复
- get_whole_text() 返回完整的对话，用于回头更新memory来用

# Memory
每个memory会包括如下字段

- Name， Event的Name，用来后续如果玩家进行游戏修改的话可以根据
- Text， 这个event下完整的对话文本
- Embedding， text的embedding
- Condition， 这个event对应的出现条件
- Emoji， 这个memory的缩写显示emoji

# MemoryPool
- 成员add_memory(memory)
- 成员change_memory( memory_name, new_text )
会将memory_name对应的事件改为new_text
- 成员retrieve( agent, text )， 根据agent的属性，以及玩家的话，对memory进行搜索
- self.embedding 记录embedding函数

# EventPool

-  成员 add_event( event )
- 会记录每个事件是否出现过
- get_random_event( agent ) 根据agent的属性和条件获取事件

# 展示玩法
slideBar控制 agent的属性
然后玩家可以正常对话，对话会使用MemoryPool.retrieve( agent, text ) 来调用记忆库 给出对话
（思考 ： 如何展现对比？双开？）
随机事件，会调用EventPool.retrieve 给出一句初始回复

# MemoryWindow
用emoji 展示当前reply中，检索到的记忆
（是否需要同步展示当前属性下可以被搜索到的记忆？）

# Print的玩法
外部有个GameManager的状态机控制器来进行控制



# Animation怎么办
是否特定的attribute change会有特定的animation？
