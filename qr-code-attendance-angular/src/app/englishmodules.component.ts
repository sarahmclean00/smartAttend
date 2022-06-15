import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { FormBuilder } from '@angular/forms';



@Component({
  templateUrl: 'englishmodules.component.html'
})


export class EnglishModulesComponent implements OnInit {

  module_list: any;
  postData: any [];
  message: any;
 
  constructor(public webService: WebService,
              public authService: AuthService,
              public formBuilder: FormBuilder) {}


  ngOnInit(){
    
    this.module_list = this.webService.getEnglishModules();
    
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

}
