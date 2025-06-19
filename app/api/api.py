from flask import Blueprint, jsonify, request

main_bp = Blueprint('', __name__, url_prefix='')

@main_bp.route('/', methods=[''])
def some_function:
    return
