

from flask import Flask, jsonify, request
from flask_cors import CORS
from demo import get_db_connection


app = Flask(__name__)
CORS(app)

@app.route('/create_ticket',methods=['POST'])

def create_ticket():
    data = request.json
    
    connection = get_db_connection()
    
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("""
                   INSERT INTO customers (name, email) values (%s,%s)
                   """,(data['name'],data['email']))
    customer_id = cursor.lastrowid
    
    cursor.execute("""
                   INSERT INTO tickets (customer_id, subject, description, priority, status) VALUES (%s,%s,%s,%s,%s)
                   
                   """,(customer_id,data['subject'],data['description'],data['priority'],data['status']))

    
    connection.commit()
    cursor.close()
    connection.close()
    
    return jsonify({"message": "Ticket created successfully"})
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    