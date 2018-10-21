from flask import Blueprint
# Register blueprint application
version_1 = Blueprint('api', __name__, url_prefix=".api/v1")
# api = Api(version_1)