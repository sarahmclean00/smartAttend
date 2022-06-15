// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { StudentsComponent } from './students.component';
import { OneStudentComponent } from './onestudent.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

// Collapse Component
import { CollapseModule } from 'ngx-bootstrap/collapse';
import { CollapsesComponent } from './views/base/collapses.component';

var routes: Routes = [
  {
    path: '',
    component: StudentsComponent,
    data: {
      title: 'Students'
    }
  },
  {
    path: ':id',
    component: OneStudentComponent,
    data: {
      title: 'Selected Student'
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
    // RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: [
    StudentsComponent, CollapsesComponent,
    OneStudentComponent 
  ]
})

export class StudentsModule { 
  
}
