# 입력 받아야 하는 것: 플레이어의 이름
# 임의로 지정되는 것: 플레이어의 HP, MP, 일반/마법 파워, 일반/마법공격 대미지, 몬스터의 HP, 일반공격 대미지

# random 모듈 사용
import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# 플레이어 캐릭터의 클래스
class Player(Character):
    def __init__(self, name, hp, mp, power, mpower):
        super().__init__(name, hp, power)
        self.max_mp = mp
        self.mp = mp
        self.power = power
        self.mpower = mpower

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other):
        # MP가 부족할 때
        if self.mp < 10:
            print("MP가 부족합니다.")
            return
        # 마법공격을 일반공격보다 강하게 들어가도록 설정
        damage = random.randint(self.power + 2, self.mpower + 6)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 피해를 입혔습니다.")
        other.hp -= damage
        self.mp -= 10

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# 몬스터 캐릭터의 클래스
class Monster(Character):
    def __init__(self, name, hp, power, critical_power):
        super().__init__(name, hp, power)
        self.critical_power = critical_power
        self.turn_count = 0

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    # 몬스터가 3턴마다 필살기를 사용하도록 구현
    def critical_attack(self, other):
        damage = random.randint(self.power + 6, self.power + 10)
        other.hp -= damage
        print(f"{self.name}의 필살기! {other.name}에게 {damage}의 데미지를 입혔습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# 스테이터스 출력 함수 정의
def print_status():
    print(f"{player.name}의 상태: HP {player.hp}/{player.max_hp}, MP {player.mp}/{player.max_mp}")
    print(f"{monster.name}의 상태: HP {monster.hp}/{monster.max_hp}")


# 캐릭터 이름 입력 받기, 몬스터 랜덤 등장
player_name = input("플레이어의 이름을 입력하세요. : ")
monster_name = random.choice(["세피로스", "젝트", "아덴", "신룡"])

# 플레이어와 몬스터 생성
print(f"{player_name}의 앞을 {monster_name}이(가) 막아섰습니다!")
player = Player(player_name, 100, 50, 10, 10)
monster = Monster(monster_name, 100, 10, 10)

print("======= Activating Combat Mode =======")
print_status()
print("========================")

# while문을 사용하여 턴제 전투 구현
while True:
    # 턴 수 카운트
    monster.turn_count += 1

    print("1. 일반 공격  2. 마법 공격")
    player_choice = input("공격 타입을 선택하세요. : ")

    if player_choice == "1":
        player.attack(monster)
    elif player_choice == "2":
        player.magic_attack(monster)
    else:
        print("1 또는 2를 선택하세요.")
        continue

    # 둘 중 하나의 HP가 0이 되면 전투 종료
    print("========================")
    print_status()
    print("========================")
    if player.hp <= 0:
        print("======= GAME OVER... =======")
        break
    elif monster.hp <= 0:
        print("======= YOU WIN! =======")
        break

    # 3턴마다 필살기를 사용하도록, 3으로 나눠서 나머지가 0일 때 필살기를 실행하게끔 작성
    if monster.turn_count % 3 == 0:
        monster.critical_attack(player)
    else:
        monster.attack(player)

    print("========================")
    print_status()
    print("========================")
    if player.hp <= 0:
        print("======= GAME OVER... =======")
        break
    elif monster.hp <= 0:
        print("======= YOU WIN! =======")
        break
