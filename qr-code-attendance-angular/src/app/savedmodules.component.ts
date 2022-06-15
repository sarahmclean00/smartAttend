import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { AlertConfig } from 'ngx-bootstrap/alert';


export function getAlertConfig(): AlertConfig {
  return Object.assign(new AlertConfig(), { type: 'success' });
}


@Component({
  templateUrl: 'savedmodules.component.html'
})


export class SavedModulesComponent implements OnInit {
    
    modules_list: any = [];
    userData: any = [];
    currentUser: any;
    userDetails: any = [];
    name: any;
    email: any;
    user_id: any;
    exists: boolean = false;

  constructor(public webService: WebService,
              public authService: AuthService,) {}


  ngOnInit(){

    this.authService.user$.subscribe(user => {
      this.currentUser = user;
      console.log(this.currentUser)
      this.userData = [
        "fullname", this.currentUser.name,
        "email", this.currentUser.email
      ]
      
      this.modules_list = this.webService.getSavedModules(this.userData);

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

  deleteModule(id: any, user_id: any) {

    this.webService.deleteSavedModule(id, user_id)
    .subscribe((response: any) => {
  
      this.modules_list = this.webService.getSavedModules(this.userData);
    })
  
  }

}
