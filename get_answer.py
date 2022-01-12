import re

species_keywords = ['especie', 'nombre cientifico']
length_keywords = ['longitud', 'mide', 'metros', 'largo', 'cm', 'tamaño']
weight_keywords = ['peso', 'pesa', 'kilos', 'masa', 'gramos', 'kg']
diet_keywords = ['come', 'dieta', 'alimenta', 'alimento', 'comida']
habitat_keywords = ['encuentra', 'encontrar', 'area', 'zona', 'habitat', 'donde', 'frecuenta',
                     'bioma' 'territorio', 'terreno']
longevity_keywords = ['vive', 'vivir', 'vida', 'morir', 'longevidad', 'año']
birth_keywords = ['salir de cuentas', 'parir', 'parto', 'epoca', 'a luz', 'nace', 'pare']
maduration_keywords = ['sexual', 'madurez', 'adulto', 'adulta', 'adultez', 'reproducir', 'descendencia', 'aparearse',
                       'crecer', 'hijos', 'cria']
problems_keywords = ['amenaza', 'mortandad', 'mortalidad', 'problema', 'riesgo', 'enfrenta', 'arriesgan', 'arriesguen', 'amenacen', 'peligro']
family_keywords = ['familia', 'grupo', 'clado', 'tipo', 'clasifica']
list_keywords = [['cuales', 'que', 'listado', 'cuantos'], ['animales', 'especies']]


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


def clean_answer(original_text, category):
    cleaner_text = re.sub("[\(\[].*?[\)\]]", "", original_text)
    if category != 'Peso' and category != 'Longitud':
        sentences = cleaner_text.split('.')
        cleaner_text = best_sentence(sentences, category)
    cleaner_text = cleaner_text.rstrip('. ')
    cleaner_text = cleaner_text.lstrip()
    cleaner_text = cleaner_text + '.'
    cleaner_text = cleaner_text.capitalize()
    return cleaner_text


def best_sentence(sentences, category):
    for sentence in sentences:
        if category == 'Especie':
            if any(word in sentence for word in species_keywords):
                return sentence
        elif category == 'Longitud':
            if any(word in sentence for word in length_keywords):
                return sentence
        elif category == 'Peso':
            if any(word in sentence for word in weight_keywords):
                return sentence
        elif category == 'Habitat':
            if any(word in sentence for word in habitat_keywords):
                return sentence
        elif category == 'Alimentacion':
            if any(word in sentence for word in diet_keywords):
                return sentence
        elif category == 'Parto':
            if any(word in sentence for word in birth_keywords):
                return sentence
        elif category == 'Madurez':
            if any(word in sentence for word in maduration_keywords):
                return sentence
        elif category == 'Problematicas':
            if any(word in sentence for word in problems_keywords):
                return sentence
        elif category == 'Longevidad':
            if any(word in sentence for word in longevity_keywords):
                return sentence
        elif category == 'Familia':
            if any(word in sentence for word in family_keywords):
                return sentence
    else:
        return sentences[0]


def main(data, question):
    names = data.index
    question = clean_text(question)
    animal = check_animal(names, question)
    category = ''
    if animal:
        if any(word in question for word in species_keywords):
            category = 'Especie'
            res = data.loc[animal, category]

        elif any(word in question for word in length_keywords):
            category = 'Longitud'
            res = data.loc[animal, category]

        elif any(word in question for word in weight_keywords):
            category = 'Peso'
            res = data.loc[animal, category]
        elif any(word in question for word in habitat_keywords):
            category = 'Habitat'
            res = data.loc[animal, category]
        elif any(word in question for word in longevity_keywords):
            category = 'Longevidad'
            res = data.loc[animal, category]
        elif any(word in question for word in diet_keywords):
            category = 'Alimentacion'
            res = data.loc[animal, category]
        elif any(word in question for word in birth_keywords):
            category = 'Parto'
            res = data.loc[animal, category]
        elif any(word in question for word in maduration_keywords):
            category = 'Madurez'
            res = data.loc[animal, category]
        elif any(word in question for word in problems_keywords):
            category = 'Problematicas'
            res = data.loc[animal, category]
        elif any(word in question for word in family_keywords):
            category = 'Familia'
            res = data.loc[animal, category]
        else:
            res = 'No se encontró respuesta, reformule la pregunta por favor.'

    else:
        if any(word in question for word in list_keywords[0]) and any(word in question for word in list_keywords[1]):
            animals = data.index
            res = f'Existen {len(animals)} especies disponibles: ' + ', '.join(data.index)
        else:
            res = 'No se ha encontrado ningún animal con ese nombre, intente de nuevo.'

    return clean_answer(res, category)


if __name__ == '__main__':
    main(None, None)
