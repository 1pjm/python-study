### 클래스 생성, 생성자, 소멸자 예제 ###

class Character:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        print(f'캐릭터 {self.name}이(가) 생성되었습니다. 체력은 {self.hp}, 힘은 {self.strength} 입니다.')

    def attack(self, other_character):
        print(f'{self.name}이(가) {other_character.name}을(를) 공격합니다.')
        other_character.hp -= self.strength

    def __del__(self):
        print(f'{self.name}이(가) 사망했습니다.')

Naymar = Character('Naymar', 300, 50)
Son = Character('Son', 400, 150)

Son.attack(Naymar)
print(f'Naymar의 남은 체력은 {Naymar.hp} 입니다.')

Naymar.attack(Son)
print(f'Son의 남은 체력은 {Son.hp} 입니다.')

Son.attack(Naymar)
print(f'Naymar의 남은 체력은 {Naymar.hp} 입니다.')

# Naymar 캐릭터의 체력이 0이 되면 제거
if Naymar.hp <= 0:
    del Naymar