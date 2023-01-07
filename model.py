"""
A module for scoring some sort of model
"""

def score_model(data):
    """
    All we're doing for now is adding the values together.
    But you can use your imagination about what we could do instead.
    """
    return {"sum":data["x1"] + data["x2"]}