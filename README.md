 F1 Driver Stats Flask Server – Project Summary
This is a simple Flask-based backend server built using Python. Its main purpose is to respond to requests for information about Formula 1 drivers.
The server stores driver data like their full name, team, number of race wins, world championships, and country of origin. When someone visits the server in their browser or sends a request (e.g. using Postman or curl), it returns the driver's stats in JSON format.

💡 Key Features:
Built using the Flask web framework.
Can show detailed information about specific drivers through routes like /driver/senna.
Returns a clean 404 error message if a driver is not found.
Runs locally in the browser at http://127.0.0.1:5000/.

📌 Technologies Used:
Python – Programming language used to build the server.
Flask – Lightweight web framework to handle HTTP requests.
JSON – Format used to send structured data to the user or client.
