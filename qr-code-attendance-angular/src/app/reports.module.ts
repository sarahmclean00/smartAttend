// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { ReportsComponent} from './reports.component';
import { Routes, RouterModule } from '@angular/router';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { OneModuleReportsComponent } from './onemodule-reports.component';




var routes: Routes = [
  {
    path: '',
    component: ReportsComponent,
    data: {
      title: 'Reports'
    }
  },
  {
    path: ':id',
    component: OneModuleReportsComponent,
    data: {
      title: 'Selected Module'
    }
  },
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(routes), BsDropdownModule
    // RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: [
    ReportsComponent, OneModuleReportsComponent
  ]
})
export class ReportsModule { }
