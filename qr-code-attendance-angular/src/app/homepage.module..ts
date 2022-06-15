// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { HomepageComponent } from './homepage.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Collapse Component
import { CollapseModule } from 'ngx-bootstrap/collapse';
import { CollapsesComponent } from './views/base/collapses.component';

var routes: Routes = [
  {
    path: '',
    component: HomepageComponent,
    data: {
      title: 'Welcome'
    }
  }
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(routes), 
    BsDropdownModule,
    FormsModule,
    ReactiveFormsModule, CollapseModule
  ],
  exports: [
    RouterModule
  ],
  declarations: [
    HomepageComponent
  ]
})

export class HomepageModule { 
  
}
