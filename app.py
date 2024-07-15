# app.py

from flask import Flask, request, jsonify
from data import get_contacts, send_message, get_received_messages
from datetime import datetime


app = Flask(__name__)

@app.route('/mensajeria/contactos', methods=['GET'])
def contactos():
    alias = request.args.get('mialias')
    if alias:
        contacts = get_contacts(alias)
        if contacts:
            return jsonify({"contacts": contacts}), 200
        return jsonify({"error": "No contacts found"}), 404
    return jsonify({"error": "Alias is required"}), 400

@app.route('/mensajeria/enviar', methods=['POST'])
def enviar():
    sender = request.args.get('mialias')
    receiver = request.args.get('aliasdestino')
    text = request.args.get('texto')

    if sender and receiver and text:
        if send_message(sender, receiver, text):
            timestamp = datetime.now().strftime("%d/%m/%Y")
            return jsonify({"message": f"Realizado en {timestamp}"}), 200
        return jsonify({"error": "Receiver not in contact list or invalid sender/receiver"}), 400
    return jsonify({"error": "All parameters (mialias, aliasdestino, texto) are required"}), 400

@app.route('/mensajeria/recibidos', methods=['GET'])
def recibidos():
    alias = request.args.get('mialias')
    if alias:
        messages = get_received_messages(alias)
        if messages:
            return jsonify({"messages": messages}), 200
        return jsonify({"error": "No messages found"}), 404
    return jsonify({"error": "Alias is required"}), 400

if __name__ == '__main__':
    app.run(debug=True)
