import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {RegiserComponent} from './regiser.component';
import {Router} from '@angular/router';
import {LoginService} from '../login/login.service';
import {Observable} from 'rxjs';

describe('RegiserComponent', () => {
    let mockRouter: Router;
    let mockLoginService: LoginService;
    let component: RegiserComponent;

    beforeEach(() => {
        mockRouter = jasmine.createSpyObj({
            navigate: new Observable()
        });
        mockLoginService = jasmine.createSpyObj({
            register: new Observable()
        });
        component = new RegiserComponent(mockRouter, mockLoginService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
