import { INavData } from '@coreui/angular';
import { AuthService } from '@auth0/auth0-angular';
import { Component, Inject, OnInit, SecurityContext, ViewEncapsulation } from '@angular/core';


export const navItems: INavData[] = [

  {
    title: true,
    name: 'Home'
  },
  {
    name: 'Dashboard',
    url: '/dashboard',
    icon: 'icon-speedometer'
  },
  {
    title: true,
    name: 'Modules'
  },
  {
    name: 'All Modules',
    url: '/modules',
    icon: 'icon-calendar'
  },
  {
    name: 'Saved Modules',
    url: '/saved_modules',
    icon: 'icon-menu'
  },
  {
    title: true,
    name: 'Attendance'
  },
  {
    name: 'Reports',
    url: '/reports',
    icon: 'icon-chart'
  },
  {
    title: true,
    name: 'Profile'
  },
  {
    name: 'Profile Details',
    url: '/profile',
    icon: 'icon-user'
  },
  {
    title: true,
    name: 'Student Records'
  },
  {
    name: 'All Students',
    url: '/students',
    icon: 'icon-people'
  },
  
  {
    title: true,
    name: 'Exit',
  },
  {
    name: 'Exit SmartAttend',
    url: '/homepage',
    icon: 'icon-logout',
  }

];
