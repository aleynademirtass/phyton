from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "jenkins"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80)



# Uygulamayı Docker ile çalıştırmak için terminalde sırasıyla şu komutları çalıştır:
# docker build -t  flask-deneme .
# docker run -d -p 5055:80 --name flask-test flask-deneme