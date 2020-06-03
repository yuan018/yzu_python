import lesson08.exception.Myexception as me

def login(username, password):
    if username == 'admin' and password == '1234':
        pass
    else:
        raise me.LoginException('登入失敗!')

if __name__ == '__main__':
    try:
        password = int(input('請輸入密碼:'))
        login('admin', 'password')
    except me.LoginException as e:
        print(e)
        e.howToDo()