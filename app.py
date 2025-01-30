from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to save feedback to a text file
def save_feedback(email, feedback):
    with open('feedback.txt', 'a') as f:
        f.write(f"Email: {email}\n")
        f.write(f"Feedback: {feedback}\n\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback_data = request.json.get('feedback')
    feedback_data = request.json.get('e')

    
    
    if feedback_data:
        email = feedback_data.get('email')
        feedback = feedback_data.get('feedback')
        
        if email and feedback:
            save_feedback(email, feedback)
            return jsonify({'message': 'Feedback received!'}), 200
        
    return jsonify({'message': 'Feedback received!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
