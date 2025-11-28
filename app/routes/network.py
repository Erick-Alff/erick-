from flask import Blueprint, render_template
from flask_login import login_required

network_bp = Blueprint('network', __name__, url_prefix='/network')

@network_bp.route('/racks')
@login_required
def racks():
    return "Página de Racks (em construção)"

@network_bp.route('/rooms')
@login_required
def rooms():
    return "Página de Salas (em construção)"

@network_bp.route('/cables')
@login_required
def cables():
    return "Página de Cabos (em construção)"

@network_bp.route('/map')
@login_required
def map():
    return "Mapa da Rede (em construção)"
