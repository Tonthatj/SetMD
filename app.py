from os import environ
from flask import abort, Flask, jsonify, make_response, request, send_from_directory, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/predict', methods=['POST'])
def create_client:    
