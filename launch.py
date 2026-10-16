from flask import Flask
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
			level=logging.INFO,
			format="%(asctime)s %(name)s %(levelname)s %(message)s",
			handlers=[
			RotatingFileHandler("system/logs.log", maxBytes=2*1024*1024, backupCount=15, encoding="utf-8"),
											logging.StreamHandler()
										]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def appMain():
	with open('applicationFile/mainPage.html', 'r', encoding='utf-8') as f:
		mainIndex = f.read()
		return mainIndex

@app.route('/registration')
def registration():
	with open('applicationFile/registrationPage.html', 'r', encoding='utf-8') as f:
		registrationIndex = f.read()
		return registrationIndex

@app.route('/test')
def test():
	with open('testQuestions/testIndex.html', 'r', encoding='utf-8') as f:
		testIndex = f.read()
		return testIndex

@app.route("/testQuestion2")
def test2():
	with open('testQuestions/testIndex2.html', 'r', encoding='utf-8') as f:
		testIndex2 = f.read()
		return testIndex2

@app.route('/testQuestion3')
def test3():
	with open('testQuestions/testIndex3.html', 'r', encoding='utf-8') as f:
		testIndex3 = f.read()
		return testIndex3

@app.route('/testQuestion4')
def test4():
	with open('testQuestions/testIndex4.html', 'r', encoding='utf-8') as f:
		testIndex4 = f.read()
		return testIndex4

@app.route('/testQuestion5')
def test5():
	with open('testQuestions/testIndex5.html', 'r', encoding='utf-8') as f:
		testIndex5 = f.read()
		return testIndex5

@app.route('/testQuestion6')
def test6():
	with open('testQuestions/testIndex6.html', 'r', encoding='utf-8') as f:
		testIndex6 = f.read()
		return testIndex6

@app.route('/testQuestion7')
def test7():
	with open('testQuestions/testIndex7.html', 'r', encoding='utf-8') as f:
		testIndex7 = f.read()
		return testIndex7

@app.route('/resultTest')
def testResult():
	with open('applicationFile/resultTest.html', 'r', encoding='utf-8') as f:
		testResult = f.read()
		return testResult
@app.route('/faq')
def faq():
    return '''
    <!doctype html>
    <html><head><meta charset="utf-8"><title>FAQ</title></head>
    <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 20px;">
        <h1>Частые вопросы</h1>
        <p>Скоро здесь появятся ответы на частые вопросы.</p>
        <p><a href="/">← На главную</a></p>
    </body></html>
    '''

@app.route('/terms')
def terms():
    return '''
    <!doctype html>
    <html><head><meta charset="utf-8"><title>Пользовательское соглашение</title></head>
    <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 20px;">
        <h1>Пользовательское соглашение</h1>
        <p>Используя сайт, вы соглашаетесь с тем, что тест носит ознакомительный характер и не является медицинской диагностикой.</p>
        <p><a href="/">← На главную</a></p>
    </body></html>
    '''

@app.route('/contraindications')
def contraindications():
    return '''
    <!doctype html>
    <html><head><meta charset="utf-8"><title>Противопоказания</title></head>
    <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 20px;">
        <h1>Противопоказания</h1>
        <p>Тест не подходит людям с повышенной тревожностью, склонностью к ипохондрии, острыми психическими состояниями.</p>
        <p>Если вам тяжело — обратитесь к специалисту.</p>
        <p><a href="/">← На главную</a></p>
    </body></html>
    '''

@app.route('/help')
def help():
    return '''
    <!doctype html>
    <html><head><meta charset="utf-8"><title>Поддержка</title></head>
    <body style="font-family: sans-serif; max-width: 700px; margin: 40px auto; padding: 20px;">
        <h1>Поддержка</h1>
        <p>Поддержка на отдыхе:)</p>
        <p><a href="/">← На главную</a></p>
    </body></html>
    '''

if __name__ == '__main__':
	app.run(port=5030, debug=True, host="0.0.0.0")
