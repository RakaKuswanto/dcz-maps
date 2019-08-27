#/src/views/UserView

from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel

user_api = Blueprint('user_api', __name__)

@user_api.route('/create_user', methods=['POST'])
def create():
  """
  Create User Function
  """
  req_data = request.get_json()
  data, error = user_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = UserModel.get_user_by_username(data.get('username'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  
  user = UserModel(data)
  user.save()
  ser_data = user_schema.dump(user).data
  token = Auth.generate_token(ser_data.get('user_id'))
  return custom_response({'jwt_token': token}, 201)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
@user_api.route('/master_user', methods=['GET'])
def get_all():
  """
  Get all users
  """
  data = UserModel.get_all_users()
  return custom_response({'status': 'succes','message':'data found',"data":data}, 200)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(mimetype="application/json",response=json.dumps(res),status=status_code)
#-------------------------------------------------------------------------