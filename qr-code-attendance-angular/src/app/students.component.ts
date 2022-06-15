import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { FormBuilder } from '@angular/forms';


@Component({
  templateUrl: 'students.component.html'
})


export class StudentsComponent implements OnInit {

  student_list: any;
  page: number = 1;
  moduleForm: any;
  isCollapsed: boolean = false;
  iconCollapse: string = 'icon-arrow-up';
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
    
    this.student_list = this.webService.getStudents();

    this.moduleForm = this.formBuilder.group({
      module_name: '',
      school: '',
      code: '',
      length: '',
      date: '',
      time: '',
      room: '',
      students_enrolled: ''
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


  deleteUser(id: any) {

    this.webService.deleteStudent(id)
    .subscribe((response: any) => {
  
      this.student_list = this.webService.getStudents();
    })
  
  }


  usersNameDescend(){

    this.student_list = this.webService.getUsersNameDescending();  //  call the WebService

  }

  usersNameAscend(){

    this.student_list = this.webService.getUsersNameAscending();  //  call the WebService

  }

  usersCourseYearDescend(){

    this.student_list = this.webService.getUsersCourseYearDescending();  //  call the WebService

  }

  usersCourseYearAscend(){

    this.student_list = this.webService.getUsersCourseYearAscending();  //  call the WebService

  }

}