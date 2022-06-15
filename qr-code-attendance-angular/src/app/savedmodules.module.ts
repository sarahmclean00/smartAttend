// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { SavedModulesComponent} from './savedmodules.component';
import { Routes, RouterModule } from '@angular/router';
import { OneModuleAttendanceComponent } from './onemodule-attendance.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';



var routes: Routes = [
  {
    path: '',
    component: SavedModulesComponent,
    data: {
      title: 'Saved Modules'
    }
  },
  {
    path: ':id',
    component: OneModuleAttendanceComponent,
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
    SavedModulesComponent, OneModuleAttendanceComponent
  ]
})
export class SavedModulesModule { }
