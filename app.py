from flask import Flask, request, jsonify

app = Flask(__name__)

# Load your trained model here
# model = ...

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    employee_code = data.get('employee_code')
    # Use the model to make a prediction
    # prediction = model.predict(...)

    return jsonify({'employee_code': employee_code, 'prediction': 'Your prediction here'})

@app.route('/employee_profile/<employee_code>', methods=['GET'])
def employee_profile(employee_code):
    # Fetch employee profile using the employee code
    # profile = ...

    return jsonify({'employee_code': employee_code, 'profile': 'Employee profile data here'})

if __name__ == '__main__':
    app.run(debug=True)