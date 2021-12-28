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
        if 'que' and 'familia' in question:
            res = data.loc[animal, 'Familia']

        elif any(word in question for word in ['especie', 'nombre cientifico']):
            res = data.loc[animal, 'Especie']

        elif any(word in question for word in ['longitud', 'mide', 'centimetros']):
            res = data.loc[animal, 'Longitud']

        elif any(word in question for word in ['peso', 'pesa', 'kilos']):
            res = data.loc[animal, 'Peso']
        elif any(word in question for word in ['vive', 'vivir', 'vida' 'años', 'longevidad']):
            res = data.loc[animal, 'Longevidad']
        elif any(word in question for word in ['alimentacion', 'come', 'comer' 'dieta', 'alimenta']):
            res = data.loc[animal, 'Alimentacion']

        else:
            res = 'No se encontró respuesta, reformule la pregunta por favor.'

    else:
        res = 'No se ha encontrado ningún animal con ese nombre, intente de nuevo.'

    return res


if __name__ == '__main__':
    main(None, None)
