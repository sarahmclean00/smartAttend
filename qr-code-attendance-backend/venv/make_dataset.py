from pymongo import MongoClient
import json
from pathlib import Path
from bson import ObjectId
import random
from flask import Flask, make_response, jsonify
from flask_cors import CORS
import qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.attendanceDB  # select database
modules = db.modules  # select the collection
users = db.users
attendance = db.attendance


def create_database():
    with open('modules_dataset.json') as f:
        for line in f:
            modules.insert_one(json.loads(line))
    print("Modules loaded")

    with open('users_dataset.json') as f:
        for line in f:
            users.insert_one(json.loads(line))
    print("Users loaded")


def random_course_year():
    fout = open("course_years.txt").read().splitlines()
    random_year = random.choice(fout)
    return random_year


def add_course_year_to_user():
    for user in users.find():
        users.update_one({"_id": user["_id"]}, {"$set": {"course_year": random_course_year()}})
        # new course code is pushed up to the database


def random_course_code():
    fout = open("course_codes.txt").read().splitlines()
    random_code = random.choice(fout)
    return random_code


def add_course_code_to_user():
    for user in users.find():
        users.update_one({"_id": user["_id"]}, {"$set": {"course_code": random_course_code()}})
        # new course code is pushed up to the database


def random_module_date():
    fout = open("dates.txt").read().splitlines()
    random_date = random.choice(fout)
    return random_date


def add_date_to_module():
    for module in modules.find():
        modules.update_one({"module_name": module["module_name"]}, {"$set": {"date": random_module_date()}})
        # new course code is pushed up to the database


def add_attendance_to_modules():
    for module in modules.find():
        modules.update_one({"module_name": module["module_name"]}, {"$set": {"attendance": []}})
        # attendance {} is pushed up to the database


def add_saved_by_to_modules():
    for module in modules.find():
        modules.update_one({"module_name": module["module_name"]}, {"$set": {"saved_by": []}})
        # saved by {} is pushed up to the database


def add_module_count_to_users():
    for user in users.find():
        users.update_one({"name": user["name"]}, {"$set": {"module_count": 0}})
        # module_count is pushed up to the database


def add_attendance_count_to_users():
    for user in users.find():
        users.update_one({"name": user["name"]}, {"$set": {"attendance_count": 0}})
        # module_count is pushed up to the database


def set_students_enrolled(id):
    for module in modules.find_one({"_id": ObjectId(id)}):
        modules.update_one({"_id": ObjectId(id)},
                           {"$set": {"students_enrolled": 10}})
        # attendance_count is pushed up to the database


def add_attendance_count_to_modules():
    for module in modules.find():
        modules.update_one({"module_name": module["module_name"]}, {"$set": {"attendance_count": 0}})
        # attendance_count is pushed up to the database


def generate_qrcode(id):
    image_path = "C:/Users/sarah/Documents/uni/final-year-project/qr-code-attendance-angular/src/assets/img/users"
    src_path = "../assets/img/users"

    # Generating QR code
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M,
                            box_size=10, border=4)  # create class and specify parameters

    # Add QR Code Data
    qr_code.add_data(id)
    qr_code.make(fit=True)

    # Wrap QR Code in Image
    qr_image = qr_code.make_image(fill_color='black', back_color='white')
    # qr_image.save(f"{image_path}/{id}.png")
    qr_image.save(f"{image_path}/{id}.png")
    filepath = f"{src_path}/{id}.png"
    return filepath


def add_qrcodes_to_users():
    for user in users.find():
        users.update_one({"id_num": user["id_num"]}, {"$set": {"qr_code": generate_qrcode(user["id_num"])}})
        # module_count is pushed up to the database

# --------------------------------------------------------
# RUN FUNCTIONS
# --------------------------------------------------------

# create_database()
# add_course_year_to_user()
# add_course_code_to_user()
# add_attendance_to_modules()
# add_saved_by_to_modules()
# add_module_count_to_users()
# add_attendance_count_to_modules()
# add_attendance_count_to_users()
# set_students_enrolled("623729602e1d4a9ed0d9f037")
# add_date_to_module()
# add_qrcodes_to_users()