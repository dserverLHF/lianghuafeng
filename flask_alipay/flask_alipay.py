from flask import Flask
from flask import redirect
from flask import jsonify
from alipay import alipay_url

app = Flask(__name__)


@app.route('/pay')
def pay():
    return redirect(alipay_url())


@app.route('/alipy_notify/')
def alipy_notify():
    # alipay = request.registry['alipay']
    # if alipay.verify_notify(**request.params):
    #     # this is a valid notify, code business logic here
    #     print(alipay.verify_notify(**request.params))
    # else:
    #     # this is a invalid notify
    #     pass
    return jsonify({'name': 'czw'})


if __name__ == '__main__':
    app.run(port=5001)
