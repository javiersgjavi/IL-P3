import os
import pandas as pd
import numpy as np


def get_animal_info(path, file):
    name = file.split('.')[0]
    with open(f'{path}/{file}', 'r') as f:
        info = f.read()

    # print(info.split('Especie:'))
    especie = info.split('Especie:')[1].split('\n')[0].strip()
    longitud = info.split('Longitud del cuerpo:')[1].split('\n')[0].strip()
    peso = info.split('Peso:')[1].split('\n')[0].strip()
    longevidad = info.split('Longevidad')[1].split('\n')[0][2:].strip()
    alimentacion = info.split('Alimentación')[1].split('\n')[0][2:].strip()

    return name, [0, especie, longitud, peso, longevidad, alimentacion, 0, 0, 0]


def main(path):
    colums = ['Familia', 'Especie', 'Longitud', 'Peso', 'Longevidad', 'Alimentacion', 'Madurez', 'Habitat',
              'Problematicas']
    data = pd.DataFrame(columns=colums)

    for file in np.sort(os.listdir(path)):
        if file.endswith('.txt'):
            name, info = get_animal_info(path, file)
            data.loc[name] = info

    data.to_csv(f'{path}/data.csv', index=True)
    return data


if __name__ == '__main__':
    main('./datos')
