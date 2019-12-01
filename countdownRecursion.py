def countdown(i):
    print(i)
    if i <= 0:
        print('Blastoff!')
        return
    else:
        countdown(i-1)

countdown(10)
