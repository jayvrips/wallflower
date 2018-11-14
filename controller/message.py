
import json

from flask import Blueprint, jsonify, Response, request
from model import db
from model.message import DbMessage

message_bp = Blueprint('message', __name__)
