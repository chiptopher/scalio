import {TestBed, inject} from '@angular/core/testing';

import {LoginService} from './login.service';
import {HttpClient} from '@angular/common/http';
import {AuthService} from '../auth/auth.service';
import {Observable, Subject} from 'rxjs';

describe('LoginService', () => {
    let service: LoginService;
    let mockHttpClient: HttpClient;
    let mockAuthService: AuthService;
    let mockHttpSubject: Subject<any>;

    beforeEach(() => {
        mockHttpSubject = new Subject();
        mockHttpClient = jasmine.createSpyObj({
            post: mockHttpSubject
        });
        mockAuthService = jasmine.createSpyObj({
            setToken: null
        });
        service = new LoginService(mockHttpClient, mockAuthService);
    });

    it('should be truthy', () => {
        expect(service).toBeTruthy();
    });

    describe('login', () => {
        it('should be able to pass on errors', () => {
            let result = true;
            service.login('username', 'password').subscribe(() => {
                result = true;
            }, () => {
                result = false;
            });
            mockHttpSubject.error({});
            expect(result).toBeFalsy();
        });
    });
});
