import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';
import { WebService } from './web.service';
import { AuthService } from '@auth0/auth0-angular';
import { FormBuilder } from '@angular/forms';


@Component({
  templateUrl: 'homepage.component.html',
  styleUrls: ['./homepage.component.css']
})


export class HomepageComponent implements OnInit {

  constructor(public webService: WebService,
              public authService: AuthService,
              public formBuilder: FormBuilder) {}


  ngOnInit(){}
    

}