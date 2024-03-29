from flask import Flask, request, jsonify
import util


app= Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def Classify_Image():
    image_data = request.form['image_data']

    response=jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    #app.run(port=8080, debug=True)

    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=8080, debug=True)