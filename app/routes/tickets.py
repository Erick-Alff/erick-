from flask import Blueprint, render_template
from flask_login import login_required

tickets_bp = Blueprint('tickets', __name__, url_prefix='/tickets')

@tickets_bp.route('/list')
@login_required
def list():
    return "Lista de chamados (em construção)"
