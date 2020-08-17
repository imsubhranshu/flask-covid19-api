try:
    from flask import Flask, request, render_template, jsonify
    import api
except Exception as identifier:
    print(identifier)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route("/state")
def state_data():
    data = {
        "result":api.get_states()
    }
    return jsonify(data)

@app.route("/district/<string:param>")
def district_data(param):
    data = {
        "result":api.get_district(param)
    }
    return jsonify(data)

@app.route("/data/<string:state>/<string:dist>")
def final_data(state,dist):
    data = {
        "result":api.get_result(state, dist)
    }
    return jsonify(data)


app.run()