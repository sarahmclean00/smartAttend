import { Component, Inject, OnInit } from '@angular/core';
import { WebService } from './web.service';
import { ActivatedRoute } from '@angular/router';
import { AuthService } from '@auth0/auth0-angular';



@Component({
  templateUrl: 'onemodule-attendance.component.html'
})
export class OneModuleAttendanceComponent implements OnInit {

  module: any = []
  student: any = [];
  attendance: any = [];
  page: number = 1;
  userData: any = [];
  currentUser: any;
  userDetails: any = [];
  user_id: any;
  exists: boolean = false;

  constructor(public webService: WebService, public route: ActivatedRoute,
              public authService: AuthService,) {}

  ngOnInit(){

    this.module = this.webService.getModule(this.route.snapshot.params['id']);
    this.attendance = this.webService.getAttendance(this.route.snapshot.params['id'], this.page)  //  call the WebService to get all reviews

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



}
