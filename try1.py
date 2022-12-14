s = '123'
try:                        # 에러 테스트
    print(int(s) + 1)
    print(int(s) / 1)

except ValueError as ve:              # exception 이름 ve
    print(' value error!', ve)

except ZeroDivisionError as de:                  
    print(' 0 divide error!', de)

except:                               # 모든에러 or 위에 안걸린 나머지 에러 
    print('error!')

else:                                 #에러가 안났으면 처리
    print('else')

finally:                              #무조건 실행
    print('finally')