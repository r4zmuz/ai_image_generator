import create as cr
import convert as co
from clean_folder import delete_json_files


def main():
    print('Welcome to AI image generator')
    while(True):
        PROMPT = input('Enter image description:')
        if PROMPT != "":
            cr.create(PROMPT)
            co.decode_json_files()
            print('')
            delete_json_files()
            print('image generating done')
            return False
        else:
            print('')
            print('Enter valid description')

if __name__ == '__main__':
    main()

