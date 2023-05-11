import time

try:
    num = 1;
    while True:
        # 무한 루프 코드
        print(num)
        num += 2
        time.sleep(1)
        pass

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")