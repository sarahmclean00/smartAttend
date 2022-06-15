// Angular
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ProfileComponent} from './profile.component';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';



var routes: Routes = [
  {
    path: '',
    component: ProfileComponent,
    data: {
      title: 'Profile'
    }
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forChild(routes)
    // RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: [
    ProfileComponent
  ]
})
export class ProfileModule { }
