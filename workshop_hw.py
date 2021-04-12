

input_won = float (input('원화를 입력하세요: '))

trans_usa = format(input_won/1124.9,'0.2f')
trans_uae = format(input_won/1337.63,'0.2f')
trans_jap = format(input_won/10.27,'0.2f')
trans_chi = format(input_won/171.78,'0.2f')

print(trans_usa + '달러')
print(trans_jap + '엔')

