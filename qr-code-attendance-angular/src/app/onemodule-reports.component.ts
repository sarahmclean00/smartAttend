import { Component, Inject, OnInit } from '@angular/core';
import { WebService } from './web.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  templateUrl: 'onemodule-reports.component.html'
})
export class OneModuleReportsComponent implements OnInit {

  module: any = []
  student: any = [];
  attendance: any = [];
  page: number = 1;

  constructor(public webService: WebService, public route: ActivatedRoute,) {}

  ngOnInit(){

    this.module = this.webService.getModule(this.route.snapshot.params['id']);
    this.attendance = this.webService.getAttendance(this.route.snapshot.params['id'], this.page)  //  call the WebService to get all reviews

} 

deleteAttendanceUser(s_id: any) {

  this.webService.deleteAttendanceUser(s_id)
  .subscribe((response: any) => {

    this.attendance = this.webService.getAttendance(this.route.snapshot.params["id"], this.page);
    location.reload();
  })

}



}
