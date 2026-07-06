import random


def play_game() -> None:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("1부터 100 사이의 숫자를 맞춰보세요!")

    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
        except ValueError:
            print("숫자만 입력해주세요.")
            continue
        except EOFError:
            print("\n게임을 종료합니다.")
            return

        attempts += 1

        if guess < secret_number:
            print("더 큰 숫자입니다.")
        elif guess > secret_number:
            print("더 작은 숫자입니다.")
        else:
            print(f"정답입니다! {attempts}번 만에 맞추셨습니다.")
            break


if __name__ == "__main__":
    play_game()