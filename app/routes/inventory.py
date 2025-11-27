from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app import db
from app.models.device import Device, Port, Connection

inventory = Blueprint("inventory", __name__)

@inventory.route("/inventory")
@login_required
def inventory_home():
    devices = Device.query.all()
    connections = Connection.query.all()
    return render_template("inventory.html", devices=devices, connections=connections)

@inventory.route("/inventory/add_device", methods=["POST"])
@login_required
def add_device():
    name = request.form.get("name")
    type = request.form.get("type")
    location = request.form.get("location")
    ports = int(request.form.get("ports", 0))

    device = Device(name=name, type=type, location=location)
    db.session.add(device)
    db.session.commit()

    # Criar portas automaticamente
    for i in range(1, ports + 1):
        port = Port(port_number=f"{i}", device_id=device.id)
        db.session.add(port)

    db.session.commit()
    return redirect(url_for("inventory.inventory_home"))

@inventory.route("/inventory/connect_ports", methods=["POST"])
@login_required
def connect_ports():
    port_a = request.form.get("port_a")
    port_b = request.form.get("port_b")

    connection = Connection(port_a_id=port_a, port_b_id=port_b)

    db.session.add(connection)
    db.session.commit()

    return redirect(url_for("inventory.inventory_home"))
    