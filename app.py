"""
Flask app for scoring a model
"""

###########################
# Imports
###########################
from flask import Flask, render_template, request, jsonify, abort
from model import score_model
from jsonschema import validate

###########################
## Data schema
###########################

# This is the schema our application expects
# in order to score.

schema = {
    "type": "object",
    "properties": {
        "x1": {"type": "number"},
        "x2": {"type": "number"}
    }
}

###########################
## Utility functions
###########################

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/score', methods=['POST'])
def score():
    """
    Score data from request

    Parameters
    ----------
    None

    Returns
    -------
    results: str
        json response
    """
    # Get JSON data from request
    score_data = request.json

    # Validate JSON matches expected schema
    try:
        validate(instance=score_data, schema=schema)
    except:
        abort(400, 'Bad Data')

    # Score data:
    results = score_model(score_data)

    # Return results as JSON
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)