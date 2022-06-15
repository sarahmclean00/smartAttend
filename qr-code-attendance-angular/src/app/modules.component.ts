import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { FormBuilder, Validators } from '@angular/forms';



@Component({
  templateUrl: 'modules.component.html'
})


export class ModulesComponent implements OnInit {

  module_list: any;
  postData: any [];
  page: number = 1;
  moduleForm: any;
  isCollapsed: boolean = false;
  iconCollapse: string = 'icon-arrow-up';
  message: any;
  userData: any = [];
  currentUser: any;
  userDetails: any = [];
  name: any;
  email: any;
  user_id: any;
  exists: boolean = false;


  constructor(public webService: WebService,
              public authService: AuthService,
              public formBuilder: FormBuilder) {}


  ngOnInit(){
    
    this.module_list = this.webService.getModules();
    
    this.moduleForm = this.formBuilder.group({
      module_name: ['', Validators.required],
      school: ['', Validators.required],
      code: ['', Validators.required],
      length: ['', Validators.required],
      date: ['', Validators.required],
      time: ['', Validators.required],
      room: ['', Validators.required],
      students_enrolled: ['', Validators.required]
    })
    
    this.authService.user$.subscribe(user => {
      this.currentUser = user;
      console.log(this.currentUser)
      this.userData = [
        "fullname", this.currentUser.name,
        "email", this.currentUser.email
      ]
      
      this.webService.getUserDetails(this.userData).subscribe(userDetails=>{

        this.userDetails = userDetails
        console.log(this.userDetails)
        this.user_id = this.userDetails._id
        if (this.user_id == null){
          this.exists = false;
        }
        else{
          this.exists = true;
        }

      })

    })

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

  onClickSave(module_name: any, school: any, code: any, length: any, date: any, time: any, room: any, student_enrolled: any, 
    attendance_count: any, attendance: any, name: any, email: any){
      this.postData = [
      "module_name", module_name,
      "school", school,
      "code", code,
      "length", length,
      "date", date,
      "time", time,
      "room", room,
      "student_enrolled", student_enrolled,
      "attendance_count", attendance_count,
      "attendance", attendance,
      "name", name,
      "email", email];
      console.log(this.postData);

      this.webService.saveModule(this.postData).subscribe(data => {
        this.message = data;
        console.log(this.message)
        if (this.message === "Complete User Details First"){
          alert(this.message);
        }
        else {
          alert('Module Saved')
        }

      });
      
  }

  onSubmit(){
    
    this.webService.postModule(this.moduleForm.value)
        .subscribe((response: any, ) => {
            alert('New Module Added')
        });
  }

  isInvalid(control: any) {
    
    return this.moduleForm.controls[control].invalid &&
           this.moduleForm.controls[control].touched;
  
  }

  isUntouched() {

    return this.moduleForm.controls.module_name.pristine ||
           this.moduleForm.controls.school.pristine ||
           this.moduleForm.controls.code.pristine ||
           this.moduleForm.controls.length.pristine ||
           this.moduleForm.controls.date.pristine ||
           this.moduleForm.controls.time.pristine ||
           this.moduleForm.controls.room.pristine ||
           this.moduleForm.controls.students_enrolled.pristine;
        
  }

  isIncomplete() {

    return this.isInvalid('module_name') ||
           this.isInvalid('school') ||
           this.isInvalid('code') ||
           this.isInvalid('length') ||
           this.isInvalid('date') ||
           this.isInvalid('time') ||
           this.isInvalid('room') ||
           this.isInvalid('students_enrolled') ||
           this.isUntouched();
  
  }

}
