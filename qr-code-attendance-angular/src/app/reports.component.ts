import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { AlertConfig } from 'ngx-bootstrap/alert';



@Component({
  templateUrl: 'reports.component.html'
})


export class ReportsComponent implements OnInit {
    
    saved_modules_list: any = [];
    attended_modules_list: any = [];
    student_reports: any = [];
    student_attendance: any = [];
    moduleDetails: any = [];
    userData: any = [];
    userDetails: any = [];
    id_num: any;
    module_id: any;
    user_id: any;
    currentUser: any;
    exists: boolean = false;


  constructor(public webService: WebService,
              public authService: AuthService,) {}


  ngOnInit(){
    

    this.authService.user$.subscribe(user => {
      this.currentUser = user;
      console.log('Reports User:', this.currentUser)
      this.userData = [
        "fullname", this.currentUser.name,
        "email", this.currentUser.email
      ]
      
      this.webService.getUserDetails(this.userData).subscribe(userDetails=>{

        this.userDetails = userDetails
        console.log(this.userDetails)
        this.id_num = this.userDetails.id_num
        this.user_id = this.userDetails._id
        
        if (this.user_id == null){
          this.exists = false;
        }
        else{
          this.exists = true;
        }


      this.student_reports = this.webService.getStudentsAttendedModules(this.id_num);

    })

      this.attended_modules_list = this.webService.getAttendedModules(this.userData);
      this.saved_modules_list = this.webService.getSavedModules(this.userData);

    })

  }


}
