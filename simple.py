

from flask import Flask, jsonify
from flask_cors import CORS
from demo import get_db_connection


app = Flask(__name__)
CORS(app)

@app.route('/tickets',methods=['GET'])

def get_tickets():
    connection = get_db_connection()
    
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute(
        """
        SELECT t.*, c.name, c.email from tickets t join customers c on t.customer_id = c.customer_id
        """
    )
    
    tickets = cursor.fetchall()
    
    
    cursor.close()
    connection.close()
    
    return jsonify(tickets)
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    