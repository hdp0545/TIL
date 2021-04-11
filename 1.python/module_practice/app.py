from flask import Flask

app = Flask(__name__)

# 직접 실행시 : __main__
# 누군가에 의해 import 되면 app 으로 이름이 정해짐
print(__name__) 

# if __name__ == '__main__':
#     pass