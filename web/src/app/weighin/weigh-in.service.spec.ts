import {TestBed, inject} from '@angular/core/testing';

import {WeighInService} from './weigh-in.service';
import {HttpClient} from '@angular/common/http';
import {Observable, Subject} from 'rxjs';
import {AuthService} from '../auth/auth.service';

describe('WeighInService', () => {
    let mockHttpClient: HttpClient;
    let mockAuthService: AuthService;
    let service: WeighInService;
    let getSubject: Subject<any>;

    beforeEach(() => {
        getSubject = new Subject();
        mockHttpClient = jasmine.createSpyObj({
            get: getSubject
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

    describe('getUserWeightDelta', () => {
        it('should make an api with the given days as the time delta', () => {
            service.getUserWeighInDelta(8);
            const expectedParams = {};
            expectedParams['params'] = {
                days: 8
            };
            expect(mockHttpClient.get).toHaveBeenCalledWith('/api/weighin/calculation/delta', expectedParams);
        });
        it('should return the data from the api call', () => {
            service.getUserWeighInDelta(8);
            service.getUserWeighInDelta(8).subscribe((result) => {
                expect(result.calculation).toEqual(200.0);
            });
            getSubject.next({calculation: 200.0});
        });
    });
});
