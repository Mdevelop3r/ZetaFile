while True:
    try:
        save = input('\nвведите название файла (вместе с расширением) чтобы прочитать ')
        
        with open(save, 'r') as f: 
            for read in f:
                print('прочитанные данные: ',read, end='')

    except FileNotFoundError:
        print('сохранение не найдено :(')
