// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { ModulesComponent } from './modules.component';
import { OneModuleComponent } from './onemodule.component';
import { AddAttendanceComponent } from './addattendance.component';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LawModulesComponent } from './lawmodules.component';
import { CollapseModule } from 'ngx-bootstrap/collapse';
import { CollapsesComponent } from './views/base/collapses.component';
import { BiologicalModulesComponent } from './biologicalmodules.component';
import { BusinessModulesComponent } from './economicsmodules.component';
import { EconomicsModulesComponent } from './businessmodules.component';
import { ComputerModulesComponent } from './computermodules.component';
import { EngineeringModulesComponent } from './engineeringmodules.component';
import { EnglishModulesComponent } from './englishmodules.component';
import { LanguagesModulesComponent } from './languagesmodules.component';

var routes: Routes = [
  {
    path: '',
    component: ModulesComponent,
    data: {
      title: 'Modules'
    }
  },
  {
    path: 'law',
    component: LawModulesComponent,
    data: {
      title: 'Law'
    }
  },
  {
    path: 'biological',
    component: BiologicalModulesComponent,
    data: {
      title: 'Biological and Behavioural Sciences'
    }
  },
  {
    path: 'business',
    component: BusinessModulesComponent,
    data: {
      title: 'Business and Management'
    }
  },
  {
    path: 'economics',
    component: EconomicsModulesComponent,
    data: {
      title: 'Economics and Finance'
    }
  },
  {
    path: 'computers',
    component: ComputerModulesComponent,
    data: {
      title: 'Electronic Engineering and Computer Science'
    }
  },
  {
    path: 'engineering',
    component: EngineeringModulesComponent,
    data: {
      title: 'Engineering and Materials Science'
    }
  },
  {
    path: 'english',
    component: EnglishModulesComponent,
    data: {
      title: 'English and Drama'
    }
  },
  {
    path: 'languages',
    component: LanguagesModulesComponent,
    data: {
      title: 'Languages Linguistics and Film'
    }
  },
  {
    path: ':id',
    component: OneModuleComponent,
    data: {
      title: 'Selected Module'
    }
  },
  {
    path: ':id/attendance',
    component: AddAttendanceComponent,
    data: {
      title: 'New Attendance Session'
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
    ModulesComponent, OneModuleComponent, AddAttendanceComponent, CollapsesComponent, 
    LawModulesComponent,
    BiologicalModulesComponent,
    BusinessModulesComponent,
    EconomicsModulesComponent,
    ComputerModulesComponent,
    EngineeringModulesComponent,
    EnglishModulesComponent,
    LanguagesModulesComponent
  ]
})
export class ModulesModule { 
  
}
