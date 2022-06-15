import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// Import Containers
import { DefaultLayoutComponent } from './containers';
import { HomepageComponent } from './homepage.component';

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  },
  {
    path: 'homepage',
    component: HomepageComponent,
    data: {
      title: 'Welcome'
    }
  },
  {
    path: '',
    component: DefaultLayoutComponent,
    data: {
      title: 'Home'
    },
    children: [
      {
        path: 'modules',
        loadChildren: () => import('./modules.module').then(m => m.ModulesModule)
      },
      {
        path: 'saved_modules',
        loadChildren: () => import('./savedmodules.module').then(m => m.SavedModulesModule)
      },
      {
        path: 'reports',
        loadChildren: () => import('./reports.module').then(m => m.ReportsModule)
      },
      {
        path: 'profile',
        loadChildren: () => import('./profile.module').then(m => m.ProfileModule)
      },
      {
        path: 'students',
        loadChildren: () => import('./students.module').then(m => m.StudentsModule)
      },
      {
        path: 'dashboard',
        loadChildren: () => import('./views/dashboard/dashboard.module').then(m => m.DashboardModule)
      }
    ]
  },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' }) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
