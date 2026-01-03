from flask import Flask, render_template
import os
app = Flask(__name__)
@app.route('/')
def home():

    return render_template('index.html')

# Control and start the execution of the application
if __name__ == "__main__":
    # Get the port number of the web server (default 5000)
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=port)
