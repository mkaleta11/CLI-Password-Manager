### This is a simple password generator using my own algorithm that uses the secrets and string module
import secrets
import string

def fisher_yates_shuffle(arr):
    '''
    Shuffling an array using the Fisher Yates algorithm combined with secrets module.
    '''
    for i in range(len(arr)-1, 0, -1):
        j = secrets.randbelow(i+1)
        arr[i], arr[j] = arr[j], arr[i]


def password_generator():
    '''
    Generating a strong password containing 14-18 letters.
    With at least 1 digit, letter and special character.
    '''
    passwordArray = []
    letters = string.ascii_letters
    numbers = string.digits
    specialCharacters = list('!@#$%^&*_+=-[],.?><')
    
    lengthOfPassword = secrets.choice(range(14,19))

    # Include every type of character 
    passwordArray.append(secrets.choice(letters))
    passwordArray.append(secrets.choice(numbers))
    passwordArray.append(secrets.choice(specialCharacters))

    # Adding the remaining characters
    for i in range(lengthOfPassword-3):
        randomIndex = secrets.choice([0,1,2])

        if randomIndex == 0:
            passwordArray.append(secrets.choice(letters))

        elif randomIndex == 1:
            passwordArray.append(secrets.choice(numbers))

        else:
            passwordArray.append(secrets.choice(specialCharacters))
    
    fisher_yates_shuffle(passwordArray)

    return ''.join(passwordArray)
    

if __name__ == '__main__':
    print(f'Generated password: {password_generator()}')