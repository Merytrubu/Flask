from flask import Flask, jsonify
import json
import os

ruta_json = os.path.join(os.path.dirname(__file__), "API.json")

with open(ruta_json, "r", encoding="utf-8") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)

IPS = ["192.168.1.10", "192.168.1.20", "192.168.1.30", "192.168.1.40", "192.168.1.50"]

dispositivos = {}


def generar_id():
    return str(len(dispositivos) + 1).zfill(4)


def agregar_dispositivo(ip, device_name, policy, status):
    dispositivos[generar_id()] = {
        "ip": ip,
        "device_name": device_name,
        "policy": policy,
        "status": status
    }


agregar_dispositivo(IPS[0], "Router Principal", "ALLOW_ALL", "Activo")
agregar_dispositivo(IPS[1], "Switch Capa 3", "BLOCK_IP", "Activo")
agregar_dispositivo(IPS[2], "Access Point", "REQUIRED_IP", "Inactivo")
agregar_dispositivo(IPS[3], "Firewall", "ALLOW_ALL", "Activo")
agregar_dispositivo(IPS[4], "Servidor DNS", "REQUIRED_IP", "Inactivo")


@app.route('/')
def inicio():
    return """
    <html>
    <body>
    <h1>Hola mundo </h1>
    <a href="http://127.0.0.1:5000/api/saludo">Buscar datos </a>
    </body>
    </html>
    """


@app.route('/json/<mac>')
def jason_data(mac):
    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["VLANs"])
    print(datos_json[mac]["Status"])
    return datos_json[mac]["Name"]


@app.route('/api/saludo')
def saludo():
    return jsonify(dispositivos)


@app.route('/api/dispositivo/0001')
def obtener_router():
    return jsonify(dispositivos["0001"])


@app.route('/api/dispositivo/0002')
def obtener_switch():
    return jsonify(dispositivos["0002"])


@app.route('/api/dispositivo/0003')
def obtener_access_point():
    return jsonify(dispositivos["0003"])


@app.route('/api/dispositivo/0004')
def obtener_firewall():
    return jsonify(dispositivos["0004"])


@app.route('/api/dispositivo/0005')
def obtener_servidor_dns():
    return jsonify(dispositivos["0005"])


@app.route('/api/dispositivo/0006')
def obtener_servidor_dhcp():
    dispositivo_inventado = {
        "ip": "192.168.1.60",
        "device_name": "Servidor DHCP",
        "policy": "BLOCK_IP",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/0007')
def obtener_balanceador():
    dispositivo_inventado = {
        "ip": "192.168.1.70",
        "device_name": "Balanceador de carga",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/0008')
def obtener_modem():
    dispositivo_inventado = {
        "ip": "192.168.1.80",
        "device_name": "Modem de fibra óptica",
        "policy": "REQUIRED_IP",
        "status": "Inactivo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/0009')
def obtener_switch_poe():
    dispositivo_inventado = {
        "ip": "192.168.1.90",
        "device_name": "Switch PoE",
        "policy": "BLOCK_IP",
        "status": "Inactivo"
    }
    return jsonify(dispositivo_inventado)


@app.route('/api/dispositivo/0010')
def obtener_proxy():
    dispositivo_inventado = {
        "ip": "192.168.1.100",
        "device_name": "Servidor Proxy",
        "policy": "ALLOW_ALL",
        "status": "Activo"
    }
    return jsonify(dispositivo_inventado)


def diccionarios():
    return jsonify(dispositivos)


if __name__ == '__main__':
    app.run(debug=True)