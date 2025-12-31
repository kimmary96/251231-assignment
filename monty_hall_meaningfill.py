import random

def simulate_one_game(switch):
    """
    몬티홀 문제 1회 시뮬레이션
    switch: True면 문 바꿨을 때, False면 유지했을 때
    Returns: 자동차를 얻으면 True, 염소면 False
    """
    # 3개 문 뒤에 car 1개, goat 2개 랜덤 배치
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)
    
    # 참가자가 랜덤으로 문 선택 (0, 1, 2 중 하나)
    first_choice = random.randint(0, 2)
    
    # 몬티가 goat가 있는 문 하나 열기
    # (참가자가 선택 안 한 문 + car 아닌 문)
    available_doors = [i for i in range(3) 
                      if i != first_choice and doors[i] == 'goat']
    monty_opens = random.choice(available_doors)
    
    # 문 바꾸기 여부에 따라 최종 선택
    if switch:
        # 남은 문으로 변경
        remaining = [i for i in range(3) 
                    if i != first_choice and i != monty_opens]
        final_choice = remaining[0]
    else:
        # 처음 선택 유지
        final_choice = first_choice
    
    # 승리 여부 반환
    return doors[final_choice] == 'car'


if __name__ == "__main__":
    # 테스트
    print("Switch:", simulate_one_game(True))
    print("Stay:", simulate_one_game(False))
