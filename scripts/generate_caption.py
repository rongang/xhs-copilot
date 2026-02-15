import os
import openai
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 获取 OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("请在 .env 文件中设置 OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

def generate_xhs_caption(topic, keywords=None):
    """
    生成小红书风格的文案
    :param topic: 主题 (例如: "OOTD 秋季穿搭")
    :param keywords: 关键词列表 (例如: ["显瘦", "高级感", "韩系"])
    :return:生成的文案
    """
    prompt = f"""
    请你作为一名专业的小红书博主，为主题“{topic}”写一篇爆款笔记。
    
    要求：
    1. 标题吸引人，包含点击率高的关键词。
    2. 正文语气活泼，多用 Emoji 表情 (💄, ✨, 💖 等)。
    3. 内容要包含痛点/爽点，能引发共鸣。
    4. 结尾加上相关的热门话题标签 (Hashtags)。
    5. 如果有关键词，请融入：{', '.join(keywords) if keywords else '无'}
    
    输出格式：
    【标题】
    ...
    【正文】
    ...
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # 或者 gpt-4
            messages=[
                {"role": "system", "content": "你是一个懂流量密码的小红���文案专家。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"生成失败: {e}"

if __name__ == "__main__":
    # 测试用例
    test_topic = "周末探店：上海静安寺的一家复古咖啡馆"
    test_keywords = ["拍照出片", "拿铁好喝", "氛围感"]
    
    print("正在生成文案...\n")
    caption = generate_xhs_caption(test_topic, test_keywords)
    print(caption)