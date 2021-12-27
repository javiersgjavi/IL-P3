import os
import pandas as pd
import numpy as np

def get_animal_info(path, file):
    name = file.split('.')[0]
    with open(f'{path}/{file}', 'r') as f:
        info =  f.read() 

    # familia = encuentra familia
    # especie = encuentra especie

    return name, [0, 0, 0, 0, 0, 0, 0, 0, 0]


def main(path):
    colums = ['Familia', 'Especie', 'Longitud', 'Peso', 'Longevidad', 'Alimentacion', 'Madurez', 'Habitat', 'Problematicas']
    data = pd.DataFrame(columns=colums)

    for file in np.sort(os.listdir(path)):
        name, info = get_animal_info(path, file)
        data.loc[name, :] = info

    data.to_csv(f'{path}/data.csv', index=True)
    return data

if __name__=='__main__':
    main('./datos')