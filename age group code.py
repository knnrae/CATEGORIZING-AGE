def classify_age(num):
    while True:
        num = int(input('Type your age to know your age group. '))
        if num >= 13 and num <= 12:
            print('You are a child. ')
        elif num >= 13 and num <= 19:
            print('You are a teen. ')
        elif num >= 20 and num <= 64:
            print('You are an adult. ')
        elif num >= 65:
            print('You are a senior. ')
        else:
            print('Invalid input! Please enter your numeric age')
classify_age(100)