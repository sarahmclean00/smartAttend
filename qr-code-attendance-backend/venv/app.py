from flask import Flask, make_response, request, jsonify, make_response, render_template, Response
import string
import json
from bson import ObjectId
from flask_cors import CORS
import pymongo
from pymongo import MongoClient
import datetime
import random
import qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import uuid

app = Flask(__name__)
CORS(app)


client = MongoClient("mongodb://127.0.0.1:27017")
db = client.attendanceDB  # select database
modules = db.modules  # select the collection
users = db.users


def format_datetime():
    date_time = str(datetime.datetime.now())
    return date_time


# --------------------------------------------------------
# DASHBOARD REQUESTS
# --------------------------------------------------------



@app.route("/api/v1.0/dashboard_saved_modules/<string:postData>", methods=["GET"])
def show_dashboard_saved_module(postData):
    page_num, page_size = 1, 10
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    first_name = str(postData.split(",")[1]).split(" ")[0]
    last_name = str(postData.split(",")[1]).split(" ")[1]
    email = str(postData.split(",")[3])

    # set current user_id
    current_id = get_user_id(first_name, last_name, email)

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"saved_by": current_id}).skip(page_start).limit(page_size):
        if module['attendance_count'] != 0:
            module['_id'] = str(module['_id'])
            modules.update_one({"_id": ObjectId(module['_id'])},
                               {"$set": {
                                   "attendance_percentage": add_attendance_percentage_to_modules(module['_id'])}})
            users.update_one({"_id": ObjectId(current_id)},
                             {'$set': {"average_attendance": get_average_attedance(current_id)}})
            for student in module['attendance']:
                student['_id'] = str(student['_id'])
            data_to_return.append(dict(module))
        else:
            print("no module sessions captured yet")
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/dashboard_future_saved_modules/<string:postData>", methods=["GET"])
def show_dashboard_future_saved_module(postData):
    page_num, page_size = 1, 10
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    first_name = str(postData.split(",")[1]).split(" ")[0]
    last_name = str(postData.split(",")[1]).split(" ")[1]
    email = str(postData.split(",")[3])

    # set current user_id
    current_id = get_user_id(first_name, last_name, email)

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"saved_by": current_id}).skip(page_start).limit(page_size):
        if module['attendance_count'] <= 0:
            module['_id'] = str(module['_id'])
            modules.update_one({"_id": ObjectId(module['_id'])},
                               {"$set": {
                                   "attendance_percentage": add_attendance_percentage_to_modules(module['_id'])}})
            users.update_one({"_id": ObjectId(current_id)},
                             {'$set': {"average_attendance": get_average_attedance(current_id)}})
            for student in module['attendance']:
                student['_id'] = str(student['_id'])
            data_to_return.append(dict(module))
        else:
            print("No Future Sessions Yet")
    return make_response(jsonify(data_to_return), 200)  # return success code



@app.route("/api/v1.0/modules_law", methods=["GET"])
def show_law_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Law"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_biological", methods=["GET"])
def show_biological_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Biological and Behavioural Sciences"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_business", methods=["GET"])
def show_business_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Business and Management"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_economics", methods=["GET"])
def show_economics_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Economics and Finance"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_computers", methods=["GET"])
def show_computer_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Electronic Engineering and Computer Science"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_engineering", methods=["GET"])
def show_engineering_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Engineering and Materials Science"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_english", methods=["GET"])
def show_english_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "English and Drama"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules_languages", methods=["GET"])
def show_language_modules():

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"school": "Languages Linguistics and Film"}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/dashboard_modules", methods=["GET"])
def show_dashboard_modules():
    page_num, page_size = 1, 3
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    data_to_return = []
    # returns documents from modules collection
    for module in modules.find().skip(page_start).limit(page_size):
        module['_id'] = str(module['_id'])  # convert the _id value to a string
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(module)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1.0/sidebar_modules_date_ascending/<string:postData>", methods=["GET"])
def show_sidebar_modules_date_ascending(postData):

    first_name = str(postData.split(",")[1]).split(" ")[0]
    last_name = str(postData.split(",")[1]).split(" ")[1]
    email = str(postData.split(",")[3])

    # set current user_id
    current_id = get_user_id(first_name, last_name, email)

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"saved_by": current_id}).sort('date', pymongo.ASCENDING):
        if module['attendance_count'] <= 0:
            module['_id'] = str(module['_id'])
            for student in module['attendance']:
                student['_id'] = str(student['_id'])
            data_to_return.append(dict(module))
        else:
            print("No Future Sessions Yet")
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/users_name_descending", methods=["GET"])
def show_users_name_descending():

    data_to_return = []
    # returns documents from modules collection
    for user in users.find().sort('name', pymongo.DESCENDING):  # returns documents from modules collection
        if user['id_num'][0].upper() == "B":
            user['_id'] = str(user['_id'])  # convert the _id value to a string
            data_to_return.append(user)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1.0/users_name_ascending", methods=["GET"])
def show_users_name_ascending():

    data_to_return = []
    # returns documents from modules collection
    for user in users.find().sort('name', pymongo.ASCENDING):  # returns documents from modules collection
        if user['id_num'][0].upper() == "B":
            user['_id'] = str(user['_id'])  # convert the _id value to a string
            data_to_return.append(user)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1.0/users_courseyear_ascending", methods=["GET"])
def show_users_courseyear_ascending():

    data_to_return = []
    # returns documents from modules collection
    for user in users.find().sort('course_year', pymongo.ASCENDING):  # returns documents from modules collection
        if user['id_num'][0].upper() == "B":
            user['_id'] = str(user['_id'])  # convert the _id value to a string
            data_to_return.append(user)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)



@app.route("/api/v1.0/users_courseyear_descending", methods=["GET"])
def show_users_courseyear_descending():

    data_to_return = []
    # returns documents from modules collection
    for user in users.find().sort('course_year', pymongo.DESCENDING):  # returns documents from modules collection
        if user['id_num'][0].upper() == "B":
            user['_id'] = str(user['_id'])  # convert the _id value to a string
            data_to_return.append(user)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)

# --------------------------------------------------------
# MODULE REQUESTS
# --------------------------------------------------------


@app.route("/api/v1.0/modules", methods=["GET"])
def show_all_modules():
    page_num, page_size = 1, 10
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    data_to_return = []
    for module in modules.find().skip(page_start).limit(page_size):  # returns documents from modules collection
        module['_id'] = str(module['_id'])  # convert the _id value to a string
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(module)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1.0/modules/<string:id>", methods=["GET"])
def show_one_module(id):
    if len(id) != 24 or not all(c in string.hexdigits for c in id):  # if length id is not 24 or chars not in id hex
        return make_response(jsonify({"error": "Invalid module ID"}), 404)
    else:
        data = []
        module = modules.find_one({'_id': ObjectId(id)})
        if module is not None:
            module['_id'] = str(module['_id'])
            for student in module['attendance']:
                student['_id'] = str(student['_id'])
            data.append(module)
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({"error": "Invalid module ID"}), 404)


@app.route("/api/v1.0/modules", methods=["POST"])
def add_module():
    if "module_name" in request.form \
            and "school" in request.form \
            and "code" in request.form \
            and "length" in request.form \
            and "date" in request.form \
            and "time" in request.form \
            and "room" in request.form \
            and "students_enrolled" in request.form:
        new_module = {"_id": ObjectId(),
                      "module_name": request.form["module_name"],
                      "school": request.form["school"],
                      "code": request.form["code"],
                      "length": request.form["length"],
                      "date": request.form["date"],
                      "time": request.form["time"],
                      "room": request.form["room"],
                      "students_enrolled": request.form["students_enrolled"],
                      "attendance": [],
                      "attendance_count": 0,
                      "saved_by": [],
                      }
        new_module_id = modules.insert_one(new_module)
        new_module_link = "http://localhost:5000/api/v1.0/modules/" + str(new_module_id.inserted_id)
        return make_response(jsonify({"url": new_module_link}), 201)
    else:
        return make_response(jsonify({"error": "Missing form data"}), 404)


@app.route("/api/v1.0/modules/<string:id>", methods=["PUT"])
def edit_module(id):  # method which takes a parameter
    if "code" in request.form \
            and "module_name" in request.form \
            and "room" in request.form \
            and "date" in request.form \
            and "time" in request.form \
            and "student_enrolled" in request.form:
        result = modules.update_one({"_id": ObjectId(id)},  # object to be updated
                                    {"$set": {"code": request.form["code"],
                                              "module_name": request.form["module_name"],
                                              "room": request.form["room"],
                                              "date": request.form["date"],
                                              "time": request.form["time"],
                                              "student_enrolled": request.form["student_enrolled"]}
                                     })
        if result.matched_count == 1:  # make use of the value returned by the PyMongo method
            edited_module_link = "http://localhost:5000/api/v1.0/modules/" + id
            return make_response(jsonify({"url": edited_module_link}), 200)
        else:
            return make_response(jsonify({"error": "Invalid module ID"}), 404)
    else:
        return make_response(jsonify({"error": "Missing form data"}), 404)


@app.route("/api/v1.0/modules/<string:id>", methods=["DELETE"])
def delete_module(id):
    result = modules.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:  # deleted_count property to determine if search object actually matched a document
        return make_response(jsonify({}), 204)  # completed no data is returned
    else:
        return make_response(jsonify({"error": "Invalid Module ID"}), 404)


# --------------------------------------------------------
# USER SETUP
# --------------------------------------------------------


# hexadecimal checker function
def check_access(id):

    if id[0].upper() == "B":
        student = str("Student")
        return student
    if id[0].upper() == "A":
        admin = str("Admin")
        return admin


# Get the user ID_Num
def get_b_num(first_name, last_name, email):

    # If the email count is greater than 0, therefore, valid
    if users.find({"email": email}).count() > 0:
        # Search each user in the users database for the email
        for user in users.find({"email": email}):
            # Return the user ID
            b_num = str(user['id_num'])
            print(b_num)
            return b_num
    else:
        print("B Number does not exist")

# Get the user ID
def get_user_id(first_name, last_name, email):

    # If the email count is greater than 0, therefore, valid
    if users.find({"email": email}).count() > 0:
        # Search each user in the users database for the email
        for user in users.find({"email": email}):
            # Return the user ID
            userid = str(user['_id'])
            print(userid)
            return userid
    else:
        print("Complete User Details First")


@app.route("/api/v1.0/userdetails/<string:userData>", methods=["GET"])
def get_user_details(userData):
    first_name = str(userData.split(",")[1]).split(" ")[0]
    last_name = str(userData.split(",")[1]).split(" ")[1]
    email = str(userData.split(",")[3])
    user_id = get_user_id(first_name, last_name, email)
    print(user_id)

    for user in users.find():
        if str(user['_id']) == user_id:
            user['_id'] = str(user['_id'])
            users.update_one({"_id": ObjectId(user_id)},
                             {'$set': {"average_attendance": get_average_attedance(user_id)}})
            userInfo = user
            print(userInfo)
    return make_response(jsonify(userInfo), 200)


# --------------------------------------------------------
# SAVED MODULES
# --------------------------------------------------------


@app.route("/api/v1.0/save", methods=["POST"])
def save_module():
    data_to_return = []
    data = request.get_json()
    # print(data)
    module = data[:-4]
    # print("this is the module: ", module)
    first_name = str(data[21]).split(" ")[0]
    last_name = str(data[21]).split(" ")[1]
    email = str(data[23])
    # print(first_name, last_name, email)
    user_id = get_user_id(first_name, last_name, email)
    # print(user_id)

    keys = []
    values = []

    for i in range(0, len(data) - 4, 2):
        keys.append(data[i])
    for i in range(1, len(data) - 4, 2):
        values.append(data[i])

    module = dict(zip(keys, values))
    # print(module)

    if users.find({"email": email}).count() > 0:
        # search modules collection for matching module details
        for module in modules.find({"module_name": module["module_name"]}):
            if modules.find({"module_name": module["module_name"]}).count() > 0:
                if str(module['saved_by']).__contains__(str(user_id)):
                    print(user_id)
                    print('You have already saved this module')
                    new_module_link = "http://localhost:5000/api/v1.0/modules/" + str(module['_id'])
                    return make_response(jsonify({"url": new_module_link}), 201)
                else:
                    db.modules.update_one(
                        {"module_name": module["module_name"]},
                        {'$push': {"saved_by": user_id}}
                    )
                    users.update_one({"_id": ObjectId(user_id)},
                                      {'$inc': {"module_count": 1}})

        return make_response(jsonify(data_to_return), 200)
    else:
        return make_response(jsonify("Complete User Details First"), 200)


@app.route("/api/v1.0/saved_modules/<string:postData>", methods=["GET"])
def show_saved_module(postData):
    first_name = str(postData.split(",")[1]).split(" ")[0]
    last_name = str(postData.split(",")[1]).split(" ")[1]
    email = str(postData.split(",")[3])

    # set current user_id
    current_id = get_user_id(first_name, last_name, email)

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"saved_by": current_id}):
        module['_id'] = str(module['_id'])
        modules.update_one({"_id": ObjectId(module['_id'])},
                           {"$set": {
                               "attendance_percentage": add_attendance_percentage_to_modules(module['_id'])}})
        users.update_one({"_id": ObjectId(current_id)},
                         {'$set': {"average_attendance": get_average_attedance(current_id)}})
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/saved_modules/<string:id>/users/<string:user_id>", methods=["DELETE"])
def delete_saved_module(id, user_id):

    # search collection for modules saved by user
    module = modules.find_one({"_id": ObjectId(id)})
    modules.update_one({"_id": ObjectId(id)}, {"$pull": {"saved_by": user_id}})  # remove entry with specified student ID

    if users.find_one({"_id": ObjectId(user_id)}):
        users.update_one({"_id": ObjectId(user_id)}, {'$inc': {"module_count": -1}})
        users.update_one({"_id": ObjectId(user_id)},
                         {'$set': {
                             "attendance_percentage": add_user_attendance_percentage_id(user_id)}})
    else:
        print("Doesn't exist in users DB")
    return make_response(jsonify({}), 204)


# hexadecimal checker function
def is_hex(s):
    hex_digits = set("0123456789abcdef")
    for char in s:
        if not (char in hex_digits):
            return False
    return True


# --------------------------------------------------------
# STUDENT ATTENDANCE REQUESTS
# --------------------------------------------------------


@app.route("/api/v1.0/students_report/<string:id_num>", methods=["GET"])
def one_students_modules(id_num):

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"attendance.b_num": id_num}):
        module['_id'] = str(module['_id'])
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/student_reports/<string:postData>", methods=["GET"])
def show_attended_modules(postData):
    first_name = str(postData.split(",")[1]).split(" ")[0]
    last_name = str(postData.split(",")[1]).split(" ")[1]
    email = str(postData.split(",")[3])

    # set current user_id
    current_b_num = get_b_num(first_name, last_name, email)

    data_to_return = []

    # search collection for modules saved by user
    for module in modules.find({"attendance.b_num": current_b_num}):
        module['_id'] = str(module['_id'])
        users.update_one({"id_num": current_b_num},
                         {'$set': {"attendance_percentage": add_student_attendance_percentage(current_b_num)}})
        for student in module['attendance']:
            student['_id'] = str(student['_id'])
        data_to_return.append(dict(module))
    return make_response(jsonify(data_to_return), 200)  # return success code


@app.route("/api/v1.0/modules/<string:id>/attendance", methods=["GET"])
def get_all_attendance_from_module(id):
    page_num, page_size = 0, 10
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    if len(id) != 24 or not is_hex(id):
        return make_response(jsonify({"error": "Invalid format for module ID"}), 404)
    else:
        if modules.find_one({"_id": ObjectId(id)}):
            data_to_return = []
            module = modules.find_one({"_id": ObjectId(id)},
                                      {"attendance": 1, "_id": 0})  # only the attendance element is requested

            for student in module["attendance"]:  # iterates across the attendance
                student["_id"] = str(student["_id"])  # _id value to a string so that it can be expressed in JSON
            attendance = list(module['attendance'])
            count = 0

            for i in range(0, page_size):
                if i == 0:
                    data_to_return.append(attendance[page_start])
                    count = page_start + 1
                else:
                    if count < len(attendance):
                        data_to_return.append(attendance[count])
                        count += 1

            return make_response(jsonify(data_to_return), 200)
        else:
            return make_response(jsonify({"error": "module ID does not exist"}), 404)


@app.route("/api/v1.0/students_report/<string:id>/attendance/<string:s_id>", methods=["GET"])
def get_one_student_from_attendance(id, s_id):
    if len(id) != 24 or not is_hex(id):
        return make_response(jsonify({"error": "Invalid format for module ID"}), 404)
    else:
        # for module in modules.find({"attendance.b_num": s_id}):
        data = []
        for module in modules.find({"_id": ObjectId(id)}, {"attendance.b_num": s_id}):
            attendance = modules.find_one({"attendance.b_num": s_id}, {"_id": 0, "attendance.$": 1})
            if attendance is None:
                return make_response(jsonify({"error": "Invalid module ID or student ID"}), 404)
            else:
                attendance['attendance'][0]['_id'] = str(attendance['attendance'][0]['_id'])
                data.append(attendance['attendance'][0])
        print(data)
        return make_response(jsonify(data), 200)


@app.route("/api/v1.0/modules/<string:id>/attendance/<string:s_id>", methods=["PUT"])
def edit_student_from_module(id, s_id):
    if len(id) != 24 or not is_hex(id):
        return make_response(jsonify({"error": "Invalid format for module ID"}), 404)
    else:
        if modules.find_one({"_id": ObjectId(id)}):
            module = dict(modules.find_one({"_id": ObjectId(id)}))
            for student in module['attendance']:
                if str(student['_id']) == s_id:
                    student["time_in"] = format_datetime()
                    student["b_num"] = request.form["b_num"]
                    student["first_name"] = request.form["first_name"]
                    student["last_name"] = request.form["last_name"]
            modules.update_one({"_id": ObjectId(id), "attendance._id": ObjectId(s_id)},
                               {"$set": {"attendance.$": student}})
            edit_student_url = "http://127.0.0.1:5000/api/v1.0/modules/" + id + "/attendance/" + s_id
            return make_response(jsonify({"url": edit_student_url}), 200)
        else:
            return make_response(jsonify({"error": "module ID does not exist"}), 404)


@app.route("/api/v1.0/reports/<string:id>/attendance/<string:s_id>", methods=["DELETE"])
def delete_student_from_module(id, s_id):

    existing_id_in_users = db.users.distinct("id_num", {"id_num": s_id})

    if len(id) != 24 or not is_hex(id):
        return make_response(jsonify({"error": "Invalid format for module ID"}), 404)  # error handling
    else:
        module = modules.find_one({"_id": ObjectId(id)})
        attendance_count = module['attendance_count'] - 1  # decrease attendance_count by 1
        modules.update_one({"_id": ObjectId(id)}, {"$pull": {"attendance": {"b_num": s_id}}})
        # remove entry with specified student ID
        modules.update_one({"_id": ObjectId(id)}, {"$set": {"attendance_count": attendance_count}})
        modules.update_one({"_id": ObjectId(id)},
                          {"$set": {
                              "attendance_percentage": add_attendance_percentage_to_modules(id)}})
        if s_id in existing_id_in_users:
            users.update_one({"id_num": s_id}, {'$inc': {"attendance_count": -1}})
            users.update_one({"id_num": s_id},
                             {'$set': {
                                 "attendance_percentage": add_student_attendance_percentage(s_id)}})
        else:
            print("Doesn't exist in users DB")

        return make_response(jsonify({}), 204)



# --------------------------------------------------------
# STUDENT PROFILE REQUESTS
# --------------------------------------------------------


@app.route("/api/v1.0/users", methods=["POST"])
def add_new_user():
    # If the email count is greater than 0, therefore, valid
    if users.find({"email": request.form["email"]}).count() > 0:
        return make_response(jsonify({"error": "User Already Exists"}), 404)
    else:
        if "name" in request.form and "email" in request.form and "course_code" in request.form and \
                "course_year" in request.form and "id_num" in request.form:
            # Creating a new ID for the user being created
            # Create the user with the following information from the front end form
            new_user = {"name": request.form["name"],
                        "email": request.form["email"],
                        "course_code": request.form["course_code"],
                        "course_year": request.form["course_year"],
                        "id_num": request.form["id_num"],
                        "qr_code": generate_qrcode(request.form["id_num"]),
                        "access": check_access(request.form["id_num"]),
                        "module_count": 0,
                        "attendance_count": 0,
                        "attendance_percentage": 0
                        }

            # Inserting the new product into the database
            new_user_id = users.insert_one(new_user)
            # Creating the link to view the product with the new ID
            new_user_link = "http://127.0.0.1:5000/api/v1.0/users/" + str(new_user_id.inserted_id)
            return make_response(jsonify({"url": new_user_link}), 201)
        else:
            # Error catching
            return make_response(jsonify({"error": "Missing form data"}), 404)


@app.route("/api/v1.0/students", methods=["GET"])
def show_all_students():
    page_num, page_size = 1, 100
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    data_to_return = []
    for user in users.find().skip(page_start).limit(page_size):  # returns documents from modules collection
        if user['id_num'][0].upper() == "B":
            user['_id'] = str(user['_id'])  # convert the _id value to a string
            data_to_return.append(user)  # retrieve each module object and append it to the list
    return make_response(jsonify(data_to_return), 200)


@app.route("/api/v1.0/students/<string:id>", methods=["GET"])
def show_one_student(id):
    if len(id) != 24 or not all(c in string.hexdigits for c in id):  # if length id is not 24 or chars not in id hex
        return make_response(jsonify({"error": "Invalid Student ID"}), 404)
    else:
        data = []
        user = users.find_one({'_id': ObjectId(id)})
        if user is not None:
            user['_id'] = str(user['_id'])
            users.update_one({"_id": ObjectId(id)},
                             {'$set': {"attendance_percentage": add_user_attendance_percentage_id(id)}})
            data.append(user)
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify({"error": "Invalid Student ID"}), 404)


@app.route("/api/v1.0/students/<string:id>", methods=["PUT"])
def edit_student(id):
    # validate input is not null
    if "name" in request.form and \
        "email" in request.form and \
        "course_code" in request.form and \
        "course_year" in request.form and \
        "id_num" in request.form:
        if users.find_one({"id_num": id}):
            print("User ID Found")
            # update document in mongo where ObjectId = user_id with new values
            result = users.update_one({
                "id_num": id}, {
                "$set": {"name": request.form["name"],
                        "email": request.form["email"],
                        "course_code": request.form["course_code"],
                        "course_year": request.form["course_year"],
                        "id_num": request.form["id_num"],
                        "qr_code": generate_qrcode(request.form["id_num"]),
                        "access": check_access(request.form["id_num"]),
                        "module_count": get_module_count(request.form["id_num"]),
                        "attendance_count": get_attendance_count(request.form["id_num"]),
                        "attendance_percentage": add_student_attendance_percentage(request.form["id_num"])
                        }
            })
            print(result)
            if result.matched_count == 1:
                edited_user_link = "http://localhost:5000/api/v1.0/users/" + id
                return make_response(jsonify({"url": edited_user_link}), 200)   # return valid status code with new link
            else:
                return make_response(jsonify(
                    {"error": "User details could not be updated"}), 404)      # return 404 status code if no match
        else:
            print("could not find user")
            return make_response(jsonify({"error": "User details could not be updated"}), 404)
    else:
        print("missing form data")
        return make_response(jsonify({"error": "Missing form data"}), 404)  # return 404 status code if data missing


@app.route("/api/v1.0/students/<string:id>", methods=["DELETE"])
def delete_student(id):
    result = users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:  # deleted_count property to determine if search object actually matched a document
        return make_response(jsonify({}), 204)  # completed no data is returned
    else:
        return make_response(jsonify({"error": "Invalid Student ID"}), 404)


# --------------------------------------------------------
# QR CODE FUNCTIONS
# --------------------------------------------------------


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


def get_attendance_count(id_num):
    attended_list = db.users.distinct("attendance_count", {"id_num": id_num})
    attended = attended_list[0]
    return attended


def get_module_count(id_num):
    enrolled_list = db.users.distinct("module_count", {"id_num": id_num})
    enrolled = enrolled_list[0]
    return enrolled


def add_student_attendance_percentage(id_num):
    enrolled_list = db.users.distinct("module_count", {"id_num": id_num})
    attended_list = db.users.distinct("attendance_count", {"id_num": id_num})

    enrolled = enrolled_list[0]
    attended = attended_list[0]
    if enrolled != 0:
        value = (int(attended) / int(enrolled)) * 100
        student_attendance_percentage = round(value, 1)
        return student_attendance_percentage
    else:
        return 0


def add_user_attendance_percentage_id(user_id):
    enrolled_list = db.users.distinct("module_count", {"_id": ObjectId(user_id)})
    attended_list = db.users.distinct("attendance_count", {"_id": ObjectId(user_id)})

    enrolled = enrolled_list[0]
    attended = attended_list[0]
    if enrolled != 0:
        value = (int(attended) / int(enrolled)) * 100
        user_attendance_percentage = round(value, 1)
        return user_attendance_percentage
    else:
        return 0


def add_attendance_percentage_to_modules(id):
    enrolled_list = db.modules.distinct("students_enrolled", {"_id": ObjectId(id)})
    attended_list = db.modules.distinct("attendance_count", {"_id": ObjectId(id)})

    enrolled = enrolled_list[0]
    attended = attended_list[0]

    if enrolled != 0:
        value = (int(attended) / int(enrolled)) * 100
        attendance_percentage = round(value, 1)
        return attendance_percentage
    else:
        return 0


def get_average_attedance(id):

    # fields = modules.find({"saved_by": id}, {"attendance_percentage": {'$gt': 0}})
    all_percentages = db.modules.distinct("attendance_percentage", {"saved_by": id, "attendance_percentage": {'$gt': 0}})
    total_percentage = sum(all_percentages)
    number_percentages = len(all_percentages)

    if total_percentage != 0:
        value = total_percentage/number_percentages
        average_attendance = round(value, 1)
        print(total_percentage, number_percentages, average_attendance)
        return average_attendance
    else:
        return 0

@app.route("/api/v1.0/modules/<string:id>/attendance", methods=["POST"])
def qr_scanner(id):

    webcam_capture = cv2.VideoCapture(0)
    webcam_capture.set(6, 640)
    webcam_capture.set(4, 480)

    while True:
        success, img = webcam_capture.read()
        imgDecoded = decode(img)
        if len(id) != 24 or not is_hex(id):  # if length id not 24 / chars not in id hexdigits
            return make_response(jsonify({"error": "Invalid format for module ID"}), 404)
        else:
            for barcode in imgDecoded:
                existing_student_ids = db.modules.distinct("attendance.b_num", {"_id": ObjectId(id)})
                codeData = barcode.data.decode('utf-8')
                points = np.array([barcode.polygon], np.int32)
                points = points.reshape((-1, 1, 2))
                cv2.polylines(img, [points], True, (255, 186, 0), 3)
                points2 = barcode.rect
                cv2.putText(img, codeData, (points2[0], points2[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 186, 0), 1)
                # print(codeData)
                if modules.find_one({"_id": ObjectId(id)}):
                    if codeData not in existing_student_ids:
                        new_student = {"_id": ObjectId(),
                                       "time_in": format_datetime(),
                                       "b_num": codeData,
                                       }
                        # if modules.find_one({"_id": ObjectId(id), "attendance.b_num": 1, "_id": 0}) != codeData:
                        module = modules.find_one({"_id": ObjectId(id)})
                        attendance_count = module['attendance_count'] + 1  # increase attendance_count by 1
                        modules.update_one({"_id": ObjectId(id)}, {"$push": {"attendance": new_student}})
                        modules.update_one({"_id": ObjectId(id)},
                                           {"$set": {"attendance_count": attendance_count}})  # update count
                        modules.update_one({"_id": ObjectId(id)},
                                           {"$set": {
                                               "attendance_percentage": add_attendance_percentage_to_modules(id)}})  # update count
                        users.update_one({"id_num": codeData},
                                         {'$inc': {"attendance_count": 1}})
                        users.update_one({"id_num": codeData},
                                         {'$set': {
                                             "attendance_percentage": add_student_attendance_percentage(codeData)}})
                    else:
                        print("student already signed in")
                else:
                    return make_response(jsonify({"error": "Module ID does not exist"}), 404)

        cv2.imshow('QR Code Scanner: ', img)
        cv2.waitKey(1)


camera = cv2.VideoCapture(0)


def gen_frames(id):
    while True:
        success, frame = camera.read()  # read the camera frame

        if not success:
            break
        else:
            for barcode in decode(frame):
                existing_student_ids = db.modules.distinct("attendance.b_num", {"_id": ObjectId(id)})
                codeData = barcode.data.decode('utf-8')
                existing_id_in_users = db.users.distinct("id_num", {"id_num": codeData})
                points = np.array([barcode.polygon], np.int32)
                points = points.reshape((-1, 1, 2))
                cv2.polylines(frame, [points], True, (255, 186, 0), 3)
                points2 = barcode.rect
                cv2.putText(frame, codeData, (points2[0], points2[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 186, 0), 1)
                print(codeData)
                if modules.find_one({"_id": ObjectId(id)}):
                    if codeData not in existing_student_ids:
                        new_student = {"_id": ObjectId(),
                                       "time_in": format_datetime(),
                                       "b_num": codeData,
                                       }
                        module = modules.find_one({"_id": ObjectId(id)})
                        attendance_count = module['attendance_count'] + 1  # increase attendance_count by 1
                        modules.update_one({"_id": ObjectId(id)}, {"$push": {"attendance": new_student}})
                        modules.update_one({"_id": ObjectId(id)},
                                           {"$set": {"attendance_count": attendance_count}})  # update count
                        modules.update_one({"_id": ObjectId(id)},
                                           {"$set": {
                                               "attendance_percentage": add_attendance_percentage_to_modules(id)}})  # update count
                        if codeData in existing_id_in_users:
                            users.update_one({"id_num": codeData}, {'$inc': {"attendance_count": 1}})
                            users.update_one({"id_num": codeData},
                                             {'$set': {
                                                 "attendance_percentage": add_student_attendance_percentage(codeData)}})
                        else:
                            print("Doesnt exist in users DB")
                    else:
                        print("student already signed in")
                else:
                    return make_response(jsonify({"error": "Module ID does not exist"}), 404)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed/<string:id>')
def video_feed(id):
    return Response(gen_frames(id), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
