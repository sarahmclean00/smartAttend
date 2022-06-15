import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable()
export class WebService {

    module_list: any;
    savedmodules_list: any;
    attendance_list: any;
    module: any;
    student: any;
    videoRef: any;
    private moduleID: any;
    private studentID: any;

    constructor(public http: HttpClient) {}

    getDashboardSavedModules(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/dashboard_saved_modules/' + userData)
    }

    getDashboardFutureSavedModules(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/dashboard_future_saved_modules/' + userData)
    }

    getDashboardAttendance(id: any, page: number) { 

        return this.http.get('http://localhost:5000/api/v1.0/saved_modules_attendance/'+id+'/attendance?pn='+page); 

    }

    getLawModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_law')
    }

    getBusinessModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_business')
    }

    getEconomicsModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_economics')
    }

    getBiologicalModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_biological')
    }

    getComputerModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_computers')
    }

    getEngineeringModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_engineering')
    }

    getEnglishModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_english')
    }

    getLanguageModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules_languages')
    }

    getStudents() {
        return this.http.get('http://localhost:5000/api/v1.0/students')
    }


    getModules() {
        return this.http.get('http://localhost:5000/api/v1.0/modules')
    }

    getDashboardModules(page: number) {
        return this.http.get('http://localhost:5000/api/v1.0/dashboard_modules?pn='+page)
    }

    getSidebarModulesDateAscending(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/sidebar_modules_date_ascending/' + userData)
    }

    getUsersNameAscending() {
        return this.http.get('http://localhost:5000/api/v1.0/users_name_ascending')
    }

    getUsersNameDescending() {
        return this.http.get('http://localhost:5000/api/v1.0/users_name_descending')
    }

    getUsersCourseYearAscending() {
        return this.http.get('http://localhost:5000/api/v1.0/users_courseyear_ascending')
    }

    getUsersCourseYearDescending() {
        return this.http.get('http://localhost:5000/api/v1.0/users_courseyear_descending')
    }

    getModule(id: any) {
        this.moduleID = id;
        return this.http.get('http://localhost:5000/api/v1.0/modules/'+id)
    }

    getStudent(id: any) {
        this.studentID = id;
        return this.http.get('http://localhost:5000/api/v1.0/students/'+id)
    }

    saveModule(postData: any){
        return this.http.post('http://localhost:5000/api/v1.0/save', postData)
    }

    getSavedModules(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/saved_modules/' + userData)
    }

    getAttendedModules(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/student_reports/' + userData)
    }

    getAttendance(id: any, page: number) { 

        this.moduleID = id;
        return this.http.get('http://localhost:5000/api/v1.0/modules/'+id+'/attendance?pn='+page); 

    }

    postNewUser(user: any){
        let postData = new FormData();
        postData.append("name", user.name);
        postData.append("email", user.email);
        postData.append("course_code", user.course_code);
        postData.append("course_year", user.course_year);
        postData.append("id_num", user.id_num);


        return this.http.post('http://localhost:5000/api/v1.0/users', postData)
    }

    getVideoFeed(id: any){
        this.moduleID = id;
        return this.http.get('http://localhost:5000/api/v1.0/video_feed/' + id);
    }

    getUserDetails(userData: any) {
        return this.http.get('http://localhost:5000/api/v1.0/userdetails/' + userData)
    }

    deleteAttendanceUser(id: any) {

        return this.http.delete('http://localhost:5000/api/v1.0/reports/' + this.moduleID + '/attendance/' + id);

    }

    deleteSavedModule(id: any, user_id: any) {

        this.moduleID = id
        return this.http.delete('http://localhost:5000/api/v1.0/saved_modules/' + id + '/users/' + user_id);

    }

    postModule(module: any) {

        let postData = new FormData();
        postData.append("module_name", module.module_name);
        postData.append("school", module.school);
        postData.append("code", module.code);
        postData.append("length", module.length);
        postData.append("date", module.date);
        postData.append("time", module.time);
        postData.append("room", module.room);
        postData.append("students_enrolled", module.students_enrolled);

        return this.http.post('http://localhost:5000/api/v1.0/modules', postData); 
       
    }

    deleteStudent(id: any) {

        return this.http.delete('http://localhost:5000/api/v1.0/students/' + id);

    }

    putStudent(student: any) {

        let putData = new FormData();
        putData.append("name", student.name);
        putData.append("email", student.email);
        putData.append("id_num", student.id_num);
        putData.append("course_code", student.course_code);
        putData.append("course_year", student.course_year);

        return this.http.put('http://localhost:5000/api/v1.0/students/' + this.studentID, putData); 
       
    }

    getStudentsAttendedModules(id: any) {
        this.studentID = id;
        return this.http.get('http://localhost:5000/api/v1.0/students_report/'+id)
    }

    getOneStudentFromModule(id: any, s_id: any){
        return this.http.get('http://localhost:5000/api/v1.0/students_report/'+ id + '/attendance/' + s_id);
    }

}
