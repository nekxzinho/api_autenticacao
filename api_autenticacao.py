from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Carrega IPs e texturas autorizadas
def carregar_configuracoes():
    with open("ip_autorizados.json", "r") as f:
        return json.load(f)

CONFIGS = carregar_configuracoes()

@app.route('/api/verificar-ip', methods=['GET'])
def verificar_ip():
    ip_cliente = request.args.get("ip")
    if ip_cliente in CONFIGS:
        return jsonify({
            "status": "autorizado",
            "textura": CONFIGS[ip_cliente]
        }), 200
    else:
        return jsonify({"status": "negado"}), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
