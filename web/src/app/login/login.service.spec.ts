import {TestBed, inject} from '@angular/core/testing';

import {LoginService} from './login.service';
import {HttpClient} from '@angular/common/http';
import {AuthService} from '../auth/auth.service';
import {Observable} from 'rxjs';

describe('LoginService', () => {
    let service: LoginService;
    let mockHttpClient: HttpClient;
    let mockAuthService: AuthService;

    beforeEach(() => {
        mockHttpClient = jasmine.createSpyObj({
            post: new Observable()
        });
        mockAuthService = jasmine.createSpyObj({
            setToken: null
        });
        service = new LoginService(mockHttpClient, mockAuthService);
    });

    it('should be truthy', () => {
        expect(service).toBeTruthy();
    });
});
