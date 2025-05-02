from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carregar IPs autorizados e texturas do arquivo JSON
with open("ip_autorizados.json", "r") as f:
    IP_AUTORIZADOS = json.load(f)

@app.route('/api/verificar-ip', methods=['GET'])
def verificar_ip():
    ip_cliente = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Se tiver múltiplos IPs no cabeçalho, pega o primeiro
    if ',' in ip_cliente:
        ip_cliente = ip_cliente.split(',')[0].strip()

    if ip_cliente in IP_AUTORIZADOS:
        return jsonify({"status": "autorizado", "textura": IP_AUTORIZADOS[ip_cliente]}), 200
    else:
        return jsonify({"status": "negado"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
