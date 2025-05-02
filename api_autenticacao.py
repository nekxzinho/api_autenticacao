
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de IPs autorizados
IPS_AUTORIZADOS = {"158.47.224.164"}

@app.route('/api/verificar-ip', methods=['GET'])
def verificar_ip():
    ip_cliente = request.remote_addr
    if ip_cliente in IPS_AUTORIZADOS:
        return jsonify({"status": "autorizado"}), 200
    else:
        return jsonify({"status": "negado"}), 403

# Instrução para rodar localmente (ou pelo Render, Gunicorn, etc.)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
