while True:
    try:
        save = input('\nвведите название файла (без расширения) чтобы прочитать ')
        save = save + '.txt'
        
        with open(save, 'r') as f: 
            for read in f:
                print('прочитанные данные: ',read, end='')

    except FileNotFoundError:
        print('сохранение не найдено :(')
