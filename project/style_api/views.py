from flask import Blueprint, request, jsonify, make_response, abort
from .decorators import no_cache, etag
from project import auth, auth_token, app, images, mongo
from gridfs import GridFS
from gridfs.errors import NoFile
from bson.objectid import ObjectId

style_api_blueprint = Blueprint('style_api', __name__)


#  @auth.verify_password
# def verify_password(email, password):
#     g.user = User.query.filter_by(email=email).first()
#     if g.user.role != 'admin':
#         return False
#     if g.user is None:
#         return False
#     return g.user.is_correct_password(password)


# @auth_token.verify_password
# def verify_authentication_token(token, unused):
#     g.user = User.verify_auth_token(token)
#     return g.user is not None


@style_api_blueprint.errorhandler(404)
def api_error(e):
    response = jsonify({'status': 404, 'error': 'not found (API!)',
                        'message': 'invalid resource URI'})
    response.status_code = 404
    return response


@style_api_blueprint.errorhandler(405)
def api_error(e):
    response = jsonify({'status': 405, 'error': 'method not supported (API!)',
                        'message': 'method is not supported'})
    response.status_code = 405
    return response


@style_api_blueprint.errorhandler(500)
def api_error(e):
    response = jsonify({'status': 500, 'error': 'internal server error (API!)',
                        'message': 'internal server error occurred'})
    response.status_code = 500
    return response


@auth.error_handler
def unauthorized():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please authenticate'})
    response.status_code = 401
    return response


@auth_token.error_handler
def unauthorized_token():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    response.status_code = 401
    return response


# @style_api_blueprint.before_request
# @auth_token.login_required
# def before_request():
#     """All routes in this blueprint require authentication."""
#     pass


# @style_api_blueprint.after_request
# @etag
# def after_request(rv):
#     """Generate an ETag header for all routes in this blueprint."""
#     return rv


# @app.route('/get-auth-token')
# @auth.login_required
# @no_cache
# def get_auth_token():
#     return jsonify({'token': g.user.generate_auth_token()})


@style_api_blueprint.route('/api/v1_2/style/<string:filename>', methods=['GET'])
def api1_2_get_style(filename):
    # try:
    #     # Convert the string to an ObjectId instance
    #     FS = GridFS(mongo.db.style_transfer)
    #     file_object = FS.get(ObjectId(style_id))
    #     response = make_response(file_object.read())
    #     response.mimetype = file_object.content_type
    #     return response
    # except NoFile:
    #     abort(404)
    return mongo.send_file(filename, base='style_transfer')


@style_api_blueprint.route('/api/v1_2/style', methods=['POST'])
def api1_2_create_style():
    
    f = request.files['style_image']
    mongo.save_file(f.filename, f, base='style_transfer', content_type=f.content_type)

    return jsonify({'filename': str(f.filename)})
