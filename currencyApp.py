from flask import Flask, jsonify
import sel_script  # Assume this is your script with the scrape_data function

app = Flask(__name__)


@app.route('/scrape',methods=['GET'])
def scrape():
    data = sel_script.scrape_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)