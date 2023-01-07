# Flask Demo

Implementing a model in real or near-real time is typically done using a web service in the form of a REST API. Flask is a lightweight platform for building REST APIs in Python. Here we demo a very simple Flask app the listens for model scoring requests on a given port. The request posts a JSON payload that the application parses, transforms the inputs and then returns the result as a JSON payload.