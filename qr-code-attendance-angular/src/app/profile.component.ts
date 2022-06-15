import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { AlertConfig } from 'ngx-bootstrap/alert';
import { FormBuilder } from '@angular/forms';


export function getAlertConfig(): AlertConfig {
  return Object.assign(new AlertConfig(), { type: 'success' });
}


@Component({
  templateUrl: 'profile.component.html'
})


export class ProfileComponent implements OnInit {

  postData: any [];
  newUserForm: any;
  currentUser: any;
  userDetails: any = [];
  userData: any = [];
  name: any;
  email: any;
  user_id: any;
  alertVisible: boolean;
  exists: boolean = false;

  constructor(public webService: WebService,
              public authService: AuthService,
              public formBuilder: FormBuilder) {}


  ngOnInit(){

      this.alertVisible = true;

      this.authService.user$.subscribe(user => {
      this.currentUser = user;
      console.log(this.currentUser)
      this.name = this.currentUser.name
      this.email = this.currentUser.email
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

      this.newUserForm = this.formBuilder.group({
        name: this.name,
        email: this.email, 
        course_code: '',
        course_year: '',
        id_num: ''
    })
    console.log(this.name)
    })

  }

  onSubmit(){
    
    this.webService.postNewUser(this.newUserForm.value)
        .subscribe((response: any, ) => {
            alert('User details completed!')
            this.alertVisible = false;
        });
  }

}