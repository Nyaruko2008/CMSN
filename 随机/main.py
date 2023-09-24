import random
import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_number():
    excluded_numbers = {3, 6, 7, 8, 10, 39, 41, 42}
    available_numbers = [num for num in range(1, 56) if num not in excluded_numbers]
    if available_numbers:
        return random.SystemRandom().choice(available_numbers)
    else:
        return None

if __name__ == "__main__":
    num_runs = 10
    for _ in range(num_runs):
        clear_screen()  # 清除屏幕
        random_number = generate_random_number()
        if random_number is not None:
            print(f"随机抽取的数字是：{random_number}")
            sys.stdout.flush()  # 强制刷新输出，以便立即显示结果
            time.sleep(0.3)
        else:
            print("没有符合条件的数字可选。")
        if _ < num_runs - 1:
            time.sleep(0.5)

    # 所有运行完成后等待5秒后关闭
    print("所有随机抽取已完成。程序将在5秒后关闭。")
    time.sleep(5)
