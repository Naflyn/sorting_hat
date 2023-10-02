import os


while True:
    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Slytherin = 0

    print('=====================')
    print('= * The            *=')
    print('= *    Sorting     *=')
    print('= *           Hat  *=')
    print('=====================')

    print('Q1) Do you like Dawn or Dusk?')
    print('    1) Dawn')
    print('    2) Dusk')
    q1 = int(input('enter answer (1-2): '))
    if q1 == 1:
        Gryffindor += 1
        Ravenclaw += 1
        os.system('cls')
    elif q1 == 2:
        Hufflepuff += 1
        Slytherin += 1
        os.system('cls')
    else:
        print('Wrong input')
        break
    
    print('=====================')
    print('= * The            *=')
    print('= *    Sorting     *=')
    print('= *           Hat  *=')
    print('=====================')

    print("Q2) When i'm dead, I want people to remember me as:")
    print('    1) The Good')
    print('    2) The Great')
    print('    3) The wise')
    print('    4) The bold')
    q2 = int(input('enter answer (1-4): '))
    if q2 == 1:
        Hufflepuff += 2
        os.system('cls')
    elif q2 == 2:
        Slytherin += 2
        os.system('cls')
    elif q2 == 3:
        Ravenclaw += 2
        os.system('cls')
    elif q2 == 4:
        Gryffindor += 2
        os.system('cls')
    else:
        print('Wrong input')
        break
    
    print('=====================')
    print('= * The            *=')
    print('= *    Sorting     *=')
    print('= *           Hat  *=')
    print('=====================')
    
    print("Q3) Which kind of instrument most pleases your ear?")
    print('    1) The violin')
    print('    2) The trumpet')
    print('    3) The piano')
    print('    4) The drum')
    q3 = int(input('enter answer (1-4): '))
    if q3 == 1:
        Slytherin += 4
        os.system('cls')
    elif q3 == 2:
        Hufflepuff += 4
        os.system('cls')
    elif q3 == 3:
        Ravenclaw += 4
        os.system('cls')
    elif q3 == 4:
        Gryffindor += 4
        os.system('cls')
    else:
        print('Wrong input')
        break

    houses = {
        'Gryffindor': Gryffindor,
        'Ravenclaw': Ravenclaw,
        'Hufflepuff': Hufflepuff,
        'Slytherin': Slytherin
        }
    phrase = {
        'where dwell the brave at heart.': Gryffindor,
        'where the wise are honored.': Ravenclaw,
        'where the loyal are true.': Hufflepuff,
        'where the cunning ones live.':Slytherin
        }
    max_points = max(houses.values())
    name_house = max(houses, key=houses.get)
    max_phrase = max(phrase, key=phrase.get)

    print(f'{name_house}: {max_points}')
    print(f'You belong in {name_house} {max_phrase}')

    break


    




