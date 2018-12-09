import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {LoginComponent} from './login.component';
import {LoginService} from './login.service';
import {Observable, Subject} from 'rxjs';
import {Router} from '@angular/router';

describe('LoginComponent', () => {
    let mockLoginService: LoginService;
    let mockRouter: Router;
    let component: LoginComponent;
    let mockLoginSubject: Subject<any>;

    beforeEach(async(() => {
        mockLoginSubject = new Subject();
        mockLoginService = jasmine.createSpyObj({
            login: mockLoginSubject
        });
        mockRouter = jasmine.createSpyObj({
            navigate: new Observable()
        });
        component = new LoginComponent(mockRouter, mockLoginService);
    }));

    it('should be truthy', () => {
        expect(component).toBeTruthy();
        expect(component.loginFailed).toBeFalsy();
    });

    describe('handleLogin', () => {
        it('should call navigate on success', () => {
            component.handleLogin();
            mockLoginSubject.next({});
            expect(mockRouter.navigate).toHaveBeenCalledWith(['/dashboard']);
        });
        it('should update when login fails', () => {
            component.handleLogin();
            mockLoginSubject.error({});
            expect(component.loginFailed).toBeTruthy();
        });
    });
});
