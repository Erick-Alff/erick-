from app import db
from datetime import datetime

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # switch, router, ap...
    location = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    ports = db.relationship("Port", backref="device", cascade="all,delete")

class Port(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    port_number = db.Column(db.String(20), nullable=False)

    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))

    # Conexão bidirecional com outras portas
    connected_to = db.relationship(
        "Connection",
        foreign_keys="Connection.port_a_id",
        backref="port_a",
        cascade="all,delete"
    )
    connected_by = db.relationship(
        "Connection",
        foreign_keys="Connection.port_b_id",
        backref="port_b",
        cascade="all,delete"
    )

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    port_a_id = db.Column(db.Integer, db.ForeignKey("port.id"))
    port_b_id = db.Column(db.Integer, db.ForeignKey("port.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
