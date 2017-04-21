for x in range(5):
    if x == min(range(5)) or x == max(range(5)):
        for x in range(6):
            print('X ', end = '')
        print()
    else:
        for x in range(6):
            if x == min(range(6)) or x == max(range(6)):
                print('X ', end = '')
            else:
                print('  ', end = '' )
        print()
