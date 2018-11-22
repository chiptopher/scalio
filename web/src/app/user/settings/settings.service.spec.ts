import {TestBed, inject} from '@angular/core/testing';

import {SettingsService} from './settings.service';
import {Observable} from 'rxjs';
import {AuthService} from '../../auth/auth.service';
import {HttpClient} from '@angular/common/http';

describe('SettingsService', () => {

    let mockAuthService: AuthService
    let mockHttpClient: HttpClient;
    let service: SettingsService;

    beforeEach(() => {
        mockAuthService = jasmine.createSpyObj({
            createHeadersWithAuthToken: {},
            getToken: 'token'
        });
        mockHttpClient = jasmine.createSpyObj({
            get: new Observable()
        });
        service = new SettingsService(mockHttpClient, mockAuthService)
    });
    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
