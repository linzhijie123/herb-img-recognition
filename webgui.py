from flask import Flask, render_template

app = Flask(__name__)


def switch(choice):
    if choice == 1:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 2:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 3:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 4:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 5:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 6:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 7:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 8:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 9:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 10:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 11:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 12:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 13:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 14:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 15:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 16:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 17:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 18:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 19:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 20:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 21:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 22:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 23:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 24:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 25:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 26:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 27:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 28:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 29:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 30:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 31:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 32:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    elif choice == 33:
        user = {'username': 'John Doe'}
        c = {'qw': 'e'}
        d = {'as': 'r'}
        a = {'zx': 'rt'}
    else:
        print("default Case")


@app.route('/')


def index():


    user = {'username': 'John Doe'}
    c={'qw': 'e'}
    d={'as': 'r'}
    a={'zx': 'rt'}


    return render_template('2.html', title='Home', user=user,c=c)

if __name__ == '__main__':
    a=1
    print(a=='1')
    app.run()