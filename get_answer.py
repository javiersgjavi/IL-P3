def clean_text(text):
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    text = text.lower()
    return text


def check_animal(names, question):
    for name in names:
        if name in question:
            return name
    return None


def main(data, question):
    names = data.index
    question = clean_text(question)
    animal = check_animal(names, question)

    if animal:
        if any(word in question for word in ['especie', 'nombre cientifico']):
            res = data.loc[animal, 'Especie']

        elif any(word in question for word in ['longitud', 'mide', 'centimetros']):
            res = data.loc[animal, 'Longitud']

        elif any(word in question for word in ['peso', 'pesa', 'kilos']):
            res = data.loc[animal, 'Peso']
        elif any(word in question for word in ['encontrar', 'encuentra', 'area', 'zona', 'habitat', 'donde', 'areas', 'frecuenta', 'frecuentar', 'habitats', 'bioma', 'biomas', 'territorios', 'terrenos']):
            res = data.loc[animal, 'Habitat']
        elif any(word in question for word in ['vive', 'vivir', 'vida', 'morir', 'longevidad']):
            res = data.loc[animal, 'Longevidad']
        elif any(word in question for word in ['alimentacion', 'come', 'comer', 'dieta', 'alimenta']):
            res = data.loc[animal, 'Alimentacion']
        elif any(word in question for word in ['salir de cuentas', 'parir', 'parto', 'epoca', 'da a luz', 'dar a luz', 'nacer', 'nace', 'pare', 'nacen', 'paren', 'dan a luz']):
            res = data.loc[animal, 'Parto']
        elif any(word in question for word in ['sexual', 'madurez', 'adulto', 'adulta', 'adultez', 'reproducir', 'descendencia', 'aparearse', 'crecer', 'hijos', 'crias', 'sexualmente']):
            res = data.loc[animal, 'Madurez']
        elif any(word in question for word in ['amenaza', 'amenazas', 'problema', 'problemas', 'riesgo', 'enfrenta', 'enfrentar', 'enfrentan', 'arriesgan', 'arriesguen', 'amenacen']):
            res = data.loc[animal, 'Problematicas']
        elif any(word in question for word in ['familia', 'grupo', 'clado', 'tipo', 'clasifica', 'clasificar']):
            res = data.loc[animal, 'Familia']
        else:
            res = 'No se encontró respuesta, reformule la pregunta por favor.'

    else:
        res = 'No se ha encontrado ningún animal con ese nombre, intente de nuevo.'

    return res


if __name__ == '__main__':
    main(None, None)
