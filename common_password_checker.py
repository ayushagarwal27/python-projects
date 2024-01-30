def check_password(password: str):
    with open('10-million-password-list-top-100000.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

        for i, common_password in enumerate(common_passwords, start=1):
            if password == common_password:
                print(f'{password}: ❌ (#{i})')
                return
        print(f'{password}: ✅ (Unique)')


if __name__ == '__main__':
    while True:
        user_password:str = input('Enter a password: ')
        if len(user_password) < 5:
            print('Please enter password with more than 4 character')
            continue
        check_password(user_password)
        break
