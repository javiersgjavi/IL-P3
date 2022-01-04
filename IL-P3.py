import load_data
import get_answer


def main():
    data = load_data.main('./datos')

    question = ''
    while question != 'exit' and question != 'salir':
        question = input('Pregunta: ')
        if question == 'exit' or question == 'salir':
            pass
        else:
            answer = get_answer.main(data, question)
            print('Respuesta:', answer)


if __name__ == '__main__':
    main()
