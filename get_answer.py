def check_animal(names, question):
    for name in names:
        if name in question:
            return name

def main(data, question):
    names = data.index
    animal = check_animal(names, question)
    
    if 'que' and 'familia' in question:
        res =  data.loc[animal, 'Familia']

    return res

if __name__=='__main__':
    main(None, None)