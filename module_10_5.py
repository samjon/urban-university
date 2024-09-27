from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == '__main__':

    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Измерение времени линейного вызова
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    time_linear = datetime.now() - start_time
    print(f"Линейный: {time_linear}")

    # Измерение времени многопроцессного вызова
    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    time_multiprocessing = datetime.now() - start_time
    print(f"Многопроцессный: {time_multiprocessing}")

