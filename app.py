from flask import Flask, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Read the contents of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Endpoint for the home page
@app.route('/')
def index():
    # Render the index.html template when the home page is accessed
    return render_template('index.html')

# Endpoint for data1
@app.route('/data1')
def get_data1():
    # Read data from 'data1.txt' and return it as JSON along with an image filename
    data = read_file('data1.txt')
    return jsonify({'data': data, 'image': 'html.jpg'})

# Endpoint for data2
@app.route('/data2')
def get_data2():
    data = read_file('data2.txt')
    return jsonify({'data': data, 'image': 'js.jpg'})

# Endpoint for data3
@app.route('/data3')
def get_data3():
    data = read_file('data3.txt')
    return jsonify({'data': data, 'image': 'python.jpg'})

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)