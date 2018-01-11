from flask import render_template, Blueprint, request, redirect, url_for, abort, jsonify, g
from .decorators import no_cache, etag
from project import db, auth, auth_token, app, images
from werkzeug.utils import secure_filename
import os

################
#### config ####
################

style_api_blueprint = Blueprint('style_api', __name__)


##########################
#### helper functions ####
##########################

# @auth.verify_password
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


########################
#### error handlers ####
########################

@style_api_blueprint.errorhandler(404)
def api_error(e):
    response = jsonify({'status': 404, 'error': 'not found (API!)', 'message': 'invalid resource URI'})
    response.status_code = 404
    return response


@style_api_blueprint.errorhandler(405)
def api_error(e):
    response = jsonify({'status': 405, 'error': 'method not supported (API!)', 'message': 'method is not supported'})
    response.status_code = 405
    return response


@style_api_blueprint.errorhandler(500)
def api_error(e):
    response = jsonify({'status': 500, 'error': 'internal server error (API!)', 'message': 'internal server error occurred'})
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


################
#### routes ####
################

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


@style_api_blueprint.route('/api/v1_2/recipes', methods=['GET'])
def api1_2_get_all_recipes():
    # return jsonify({'recipes': [recipe.get_url() for recipe in Recipe.query.all()]})
    pass


@style_api_blueprint.route('/api/v1_2/recipes/<int:recipe_id>', methods=['GET'])
def api1_2_get_recipe(recipe_id):
    # return jsonify(Recipe.query.get_or_404(recipe_id).export_data())
    return jsonify({'result': 'True'})


@style_api_blueprint.route('/api/v1_2/recipes', methods=['POST'])
def api1_2_create_recipe():
    # new_recipe = Recipe()
    # new_recipe.import_data(request)
    # db.session.add(new_recipe)
    # db.session.commit()
    # return jsonify({}), 201, {'Location': new_recipe.get_url()}
    # f = request.files['recipe_image']
    # filename = secure_filename(f.filename)
    # f.save(os.path.join(app.config['UPLOADS_DEFAULT_DEST'], filename))
    filename = images.save(request.files['recipe_image'])
    image_url = images.url(filename)
    print(image_url)

    return jsonify({'result': 'True'})


@style_api_blueprint.route('/api/v1_2/recipes/<int:recipe_id>', methods=['PUT'])
def api1_2_update_recipe(recipe_id):
    # recipe = Recipe.query.get_or_404(recipe_id)
    # recipe.import_data(request)
    # db.session.add(recipe)
    # db.session.commit()
    filename = images.save(request.files['recipe_image'])
    image_url = images.url(filename)
    print(image_url)

    return jsonify({'result': 'True'})



@style_api_blueprint.route('/api/v1_2/recipes/<int:recipe_id>', methods=['DELETE'])
def api1_2_delete_recipe(recipe_id):
    # recipe = Recipe.query.get_or_404(recipe_id)
    # db.session.delete(recipe)
    # db.session.commit()
    # return jsonify({'result': True})
    pass

