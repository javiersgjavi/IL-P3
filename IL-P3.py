import  load_data
import get_answer

def main():
    data = load_data.main('./datos')

    question = ''
    while question != 'exit':
        question = input('Ingrese una opcion: ')
        answer = get_answer.main(data, question)
        print(answer)

if __name__=='__main__':
    main()