"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from flask_cors import CORS
from api.models import db, Traveler, Post
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

from api.utils import generate_sitemap, APIException


api = Blueprint('api', __name__)


CORS(api)

@api.route('/login', methods=['POST'])
def login():
    email,password = request.json.get(
            "email", None
    ), request.json.get(
            "password",None
    )

    if email and password: 
        traveler = Traveler.get_by_email(email)
        if traveler:
            if traveler.validate_password(password): 
                access_token = create_access_token(identity=traveler.to_dict(), expires_delta=timedelta(minutes=100))
                traveler_with_token = traveler.traveler_with_token(access_token)
                return jsonify(traveler_with_token),200
   
    return ({'error':"User and password don't match"}),201


@api.route('/traveler', methods=['POST'])
def create_traveler():
    name,email,password,age,language = request.json.get(
            "name",None
    ), request.json.get(        
            "email", None
    ), request.json.get(
            "password",None
    ), request.json.get(
            "age",None
    ), request.json.get(
            "language",None
    )
    
    if email:
        traveler = Traveler.get_by_email(email)
        if traveler:
            if traveler.validate_email(email):
              return ({'error':"Traveler already exist"}),201
        else:
            new_traveler = Traveler(name=name,email=email, _password=password, language=language, age=age)  
            password = generate_password_hash(password, method='pbkdf2:sha256')
            new_traveler_created= new_traveler.create()
            new_traveler_dic = new_traveler_created.to_dict()

            if new_traveler_dic: 
                return jsonify(new_traveler_dic),201
            else:
                return ({'error':"Missing info"}), 404

 
     

@api.route('/profile/<email>', methods=['GET'])
def get_user_by_email(email):
    traveler = Traveler.get_by_email(email)
    if traveler:
        return jsonify(traveler.to_dict()), 200
    
    return jsonify({'error': "Profile not found"}), 404 


@api.route('/blog', methods=['GET'])
def get_all_posts():
    
    posts = Post.get_all_post()
    print(posts) 
    if posts:
        posts_dict = [post.to_dict() for post in posts]
        return jsonify(posts_dict), 200

    return jsonify({'error': "Posts not found"}), 404

 

