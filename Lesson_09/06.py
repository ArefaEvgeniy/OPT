def talk(type='shout'):
    def shout(word='Yes'):
        return word.upper() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    if type == 'shout':
        return shout
    else:
        return whisper


print(talk('rttr')('Dima'))
