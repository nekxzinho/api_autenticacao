from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carrega IPs autorizados de um arquivo JSON externo
def carregar_ips():
    with open("ip_autorizados.json", "r") as f:
        return set(json.load(f))

IPS_AUTORIZADOS = carregar_ips()

@app.route('/api/verificar-ip', methods=['GET'])
def verificar_ip():
    ip_cliente = request.args.get("ip")
    if ip_cliente in IPS_AUTORIZADOS:
        return jsonify({"status": "autorizado"}), 200
    else:
        return jsonify({"status": "negado"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
