from scanner import (isValidUserName,
                     isValidPasswordName,
                     isValidKey,)
from parser import readYAMLAsStr
from graphtaint import getYAMLFiles


def method_fuzzer():

    key_1 = '     rekeyboarded     '
    fuzz_1 = isValidKey(key_1)
    print('Fuzzing isValidKey(' + "'" + key_1 + "'" + ')')

    if fuzz_1:
        print('Successful fuzz: '
              'isValidKey() accepts leading and trailing spaces which is bad practice for security.\n\n')
    else:
        print('Unsuccessful fuzzing: '
              'try another input to find errors.\n\n')

    key_2 = ''
    fuzz_2 = isValidUserName(key_2)
    print('Fuzzing isValidUserName(' + "'" + key_2 + "'" + ')')

    if fuzz_2:
        print('Successful fuzz: '
              'isValidUserName() accepts commonly unaccepted username inputs (empty string username).\n\n')
    else:
        print('Unsuccessful fuzzing: '
              'try another input to find errors.\n\n')

    key_3 = ''
    fuzz_3 = isValidPasswordName(key_3)
    print('Fuzzing isValidPasswordName(' + "'" + key_3 + "'" + ')')

    if fuzz_3:
        print('Successful fuzz: '
              'isValidPasswordName() accepts sub-par (regarding security) password inputs (empty string input).\n\n')
    else:
        print('Unsuccessful fuzzing: '
              'try another input to find errors.\n\n')

    key_4 = 'README.MD'
    fuzz_4  = readYAMLAsStr(key_4)
    print('Fuzzing readYAMLAsStr(' + "'" + key_4 + "'" + ')')

    if fuzz_4:
        print('Successful fuzz: '
              'readYAMLAsStr() reads in any file with a valid path, not only YAML files.\n\n')
    else:
        print('Unsuccessful fuzzing: '
              'try another input to find errors.\n\n')

    key_5 = '.github'
    fuzz_5 = getYAMLFiles(key_5)
    print('Fuzzing getYAMLFiles(' + "'" + key_5 + "'" + ')')

    if fuzz_5:
        print('Successful fuzz: '
              'getYAMLFiles() validates YAML files that would be rejected by checkIfWeirdYAML().\n\n')
    else:
        print('Unsuccessful fuzzing: '
              'try another input to find errors a.\n\n')


def automatic_fuzzer():

    method_fuzzer()

if __name__ == '__main__':

    automatic_fuzzer()