import requests

def chat():
    print("deepseek (输入 '退出' 结束对话)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["退出", "q", "quit", "exit"]:
            print("聊天结束。")
            break
        
        url = f"https://api.jkyai.top/API/deepseek.php?question={user_input}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            print("deepseek:", response.text)
        except requests.exceptions.RequestException as e:
            print("请求失败:", e)

if __name__ == "__main__":
    chat()
