import { Component, Inject, OnInit } from '@angular/core';
import { WebService } from './web.service';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, Validators } from '@angular/forms';


@Component({
  templateUrl: 'onestudent.component.html'
})
export class OneStudentComponent implements OnInit {

  student: any = [];
  student_reports: any = [];
  student_attendance: any = [];
  editStudentForm: any;
  isCollapsed: boolean = false;
  iconCollapse: string = 'icon-arrow-up';
  studentDetails: any = [];
  moduleDetails: any = [];
  studentInfo: any =[];
  student_id: any;
  module_id: any;
  name: any;
  email: any;
  id_num: any;
  course_year: any;
  course_code: any;



  constructor(public webService: WebService, 
              public route: ActivatedRoute,
              public formBuilder: FormBuilder) {}

  ngOnInit(){

      this.webService.getStudent(this.route.snapshot.params['id']).subscribe(studentDetails=>{

      this.studentDetails = studentDetails[0]
      console.log('Students Details', this.studentDetails)
      this.student_id = this.studentDetails._id
      
      this.name = this.studentDetails.name
      this.email = this.studentDetails.email
      this.id_num = this.studentDetails.id_num
      this.course_year = this.studentDetails.course_year
      this.course_code = this.studentDetails.course_code


      this.editStudentForm = this.formBuilder.group({
        name: this.name,
        email: this.email,
        id_num: this.id_num,
        course_code: this.course_code,
        course_year: this.course_year
      });


      this.student_reports = this.webService.getStudentsAttendedModules(this.id_num);

      this.webService.getStudentsAttendedModules(this.id_num).subscribe(moduleDetails=>{
      this.moduleDetails = moduleDetails[0]
      console.log('Module Details', this.moduleDetails)
      this.module_id = this.moduleDetails._id

      this.student_attendance = this.webService.getOneStudentFromModule(this.module_id, this.id_num)

      })

  })

  this.student = this.webService.getStudent(this.route.snapshot.params['id']);

  } 

  onSubmit(){
    
    console.log('form', this.editStudentForm.value)
    this.webService.putStudent(this.editStudentForm.value)
        .subscribe((response: any) => 
        {
          this.editStudentForm.reset();
          alert('Student Details Updated')
          location.reload();            
        });
  }

  collapsed(event: any): void {
    // console.log(event);
  }

  expanded(event: any): void {
    // console.log(event);
  }

  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed;
    this.iconCollapse = this.isCollapsed ? 'icon-arrow-down' : 'icon-arrow-up';
  }

  
deleteAttendanceUser(id_num: any) {

  this.id_num = id_num
  this.webService.deleteAttendanceUser(id_num)
  .subscribe((response: any) => {

    this.student_reports = this.webService.getStudentsAttendedModules(this.id_num);
  })

}


}
