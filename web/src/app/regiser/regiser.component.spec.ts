import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {RegiserComponent} from './regiser.component';
import {Router} from '@angular/router';
import {LoginService} from '../login/login.service';
import {Observable, Subject} from 'rxjs';

describe('RegiserComponent', () => {
    let mockRouter: Router;
    let mockLoginService: LoginService;
    let component: RegiserComponent;
    let mockRegisterSubject: Subject<any>;

    beforeEach(() => {
        mockRegisterSubject = new Subject();
        mockRouter = jasmine.createSpyObj({
            navigate: new Observable()
        });
        mockLoginService = jasmine.createSpyObj({
            register: mockRegisterSubject
        });
        component = new RegiserComponent(mockRouter, mockLoginService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
        expect(component.registrationFailed).toBeFalsy();
    });

    describe('handleRegistration', () => {
        it('should update when the service returns an error', () => {
            component.handleRegistration();
            mockRegisterSubject.error({});
            expect(component.registrationFailed).toBeTruthy();
        });
    });
});
