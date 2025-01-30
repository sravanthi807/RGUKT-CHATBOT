from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Function to write user details to a text file
def write_to_file(email, password, gender, department):
    try:
        # Open the file in append mode and ensure it closes properly using 'with' statement
        with open('users.txt', 'a') as file:
            file.write(f'{email},{password},{gender},{department}\n')
            app.logger.info(f"Successfully written to file: {email},{password},{gender},{department}")
    except Exception as e:
        app.logger.error(f"Error writing to file: {e}")

# Route to render the sign-in page
@app.route('/')
def signin_form():
    return render_template('signin.html')

# Route to handle sign-in form submission
@app.route('/signin', methods=['POST'])
def signin():
    try:
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        department = request.form['department']
        
        # Log received data
        app.logger.info(f"Received email: {email}")
        app.logger.info(f"Received password: {password}")
        app.logger.info(f"Received gender: {gender}")
        app.logger.info(f"Received depatment: {department}")

        
        # Store user details in text file
        write_to_file(email, password, gender, department)
        
        # Verify that the data was written by reading the file
        with open('users.txt', 'r') as file:
            contents = file.read()
            app.logger.info(f"File contents after write: {contents}")
        
        # Return JSON response with success message
        return jsonify({'message': 'Data received and stored successfully!'})
    except Exception as e:
        app.logger.error(f"Error in signin route: {e}")
        return jsonify({'message': 'An error occurred!'}), 500

if __name__ == '__main__':
    # Ensure the log level is set to debug
    app.logger.setLevel("DEBUG")
    
    # Create users.txt if it does not exist
    if not os.path.exists('users.txt'):
        open('users.txt', 'w').close()
    
    app.run(port=5001, debug=True)
