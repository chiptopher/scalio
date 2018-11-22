import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {LoginComponent} from './login.component';
import {LoginService} from './login.service';
import {Observable} from 'rxjs';
import {Router} from '@angular/router';

describe('LoginComponent', () => {
    let mockLoginService: LoginService;
    let mockRouter: Router;
    let component: LoginComponent;

    beforeEach(async(() => {
        mockLoginService = jasmine.createSpyObj({
            login: new Observable()
        });
        mockRouter = jasmine.createSpyObj({
            navigate: new Observable()
        });
        component = new LoginComponent(mockRouter, mockLoginService);
    }));

    it('should be truthy', () => {
        expect(component).toBeTruthy();
    });
});
