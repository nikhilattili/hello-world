from flask import Flask, render_template, request, Blueprint, send_from_directory,jsonify,abort

app = Flask(__name__, static_folder='sample-project/dist/sample-project')

angular = Blueprint('sample-project', __name__,
                    template_folder='sample-project/dist/sample-project')
app.register_blueprint(angular)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)