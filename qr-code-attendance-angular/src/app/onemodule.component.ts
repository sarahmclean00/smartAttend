import { Component, Inject, OnInit } from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { getStyle, rgbToHex } from '@coreui/coreui/dist/js/coreui-utilities';
import { WebService } from './web.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  templateUrl: 'onemodule.component.html'
})
export class OneModuleComponent implements OnInit {

  module: any = []
  student: any = [];
  attendance: any = [];
  page: number = 1;

  constructor(public webService: WebService, public route: ActivatedRoute,) {}

  ngOnInit(){

    this.module = this.webService.getModule(this.route.snapshot.params['id']);
    this.attendance = this.webService.getAttendance(this.route.snapshot.params['id'], this.page)  //  call the WebService to get all reviews

} 



}
