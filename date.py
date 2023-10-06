import datetime

# Sample user database represented as a dictionary
user_database = {
    'user1@example.com': {
        'password': 'password123',
        'last_sign_in': None,
    },
    'user2@example.com': {
        'password': 'securepass',
        'last_sign_in': None,
    },
}

def update_last_sign_in(email):
    if email in user_database:
        user_database[email]['last_sign_in'] = datetime.datetime.now()
        print(f'Welcome back, {email}! Last sign-in: {user_database[email]["last_sign_in"]}')
    else:
        print('User not found.')

def main():
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if email in user_database and user_database[email]['password'] == password:
        update_last_sign_in(email)
    else:
        print('Invalid email or password.')

if __name__ == "__main__":
    main()
