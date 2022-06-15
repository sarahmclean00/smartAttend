import { Component, Inject, OnInit } from '@angular/core';
import { DOCUMENT, PathLocationStrategy } from '@angular/common';
import { getStyle, rgbToHex } from '@coreui/coreui/dist/js/coreui-utilities';
import { WebService } from './web.service';
import { ActivatedRoute } from '@angular/router';


// declare function qrScan(): void;


@Component({
  templateUrl: 'addattendance.component.html'
})
export class AddAttendanceComponent implements OnInit {

  module: any = []
  student: any = [];
  attendance: any = [];
  page: number = 1;

  constructor(public webService: WebService, public route: ActivatedRoute,) {}

  videoRef: any;

  ngOnInit(): void {
    this.videoRef = document.getElementById('scanner');
    this.setUpCamera();

    this.module = this.webService.getModule(this.route.snapshot.params['id']);
    this.attendance = this.webService.getAttendance(this.route.snapshot.params['id'], this.page)  //  call the WebService to get all reviews
  }

  setUpCamera(){
    navigator.mediaDevices.getUserMedia({video: true, audio: false
    }).then(stream => {
      this.videoRef.srcObject = stream
    })
  }

  getAttendanceTable(){
  location.reload()  
  }

}
