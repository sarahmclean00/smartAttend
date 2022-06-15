import {Component, OnInit} from '@angular/core';
import { navItems } from '../../_nav';
import { WebService } from '../../web.service';
import { AuthService } from '@auth0/auth0-angular';

@Component({
  selector: 'app-dashboard',
  templateUrl: './default-layout.component.html'
})
export class DefaultLayoutComponent {

  future_saved_modules_list: any = [];
  page: number = 1;
  userData: any = [];
  userDetails: any = [];
  user_id: any;
  currentUser: any;
  exists: boolean = false;


  constructor(public webService: WebService,
              public authService: AuthService) {}

  public sidebarMinimized = false;
  public navItems = navItems;

  toggleMinimize(e) {
    this.sidebarMinimized = e;
  }

  ngOnInit(){

    this.authService.user$.subscribe(user => {
      this.currentUser = user;
      console.log('sidebar:', this.currentUser)
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

      // this.future_saved_modules_list = this.webService.getDashboardFutureSavedModules(this.userData);
      this.future_saved_modules_list = this.webService.getSidebarModulesDateAscending(this.userData);

    })

  }
  
}
