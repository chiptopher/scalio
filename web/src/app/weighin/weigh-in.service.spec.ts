import {TestBed, inject} from '@angular/core/testing';

import {WeighInService} from './weigh-in.service';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {AuthService} from '../auth/auth.service';

describe('WeighInService', () => {
    let mockHttpClient: HttpClient;
    let mockAuthService: AuthService;
    let service: WeighInService;
    beforeEach(() => {
        mockHttpClient = jasmine.createSpyObj({
            get: new Observable()
        });
        mockAuthService = jasmine.createSpyObj({
            createHeadersWithAuthToken: {},
            getToken: 'token'
        });
        service = new WeighInService(mockHttpClient, mockAuthService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });

    describe('getUserRollingAverageList', () => {
        it('should make an api request', () => {
            service.getUserRollingAverageList().subscribe(() => {
                expect(mockHttpClient.get).toHaveBeenCalledWith('/api/weighin/calculation/list', jasmine.anything());
            });
        });
    });
});
