import {Injectable} from '@angular/core';
import {HttpClient, HttpEvent} from '@angular/common/http';
import {AuthService} from '../auth/auth.service';
import {Observable} from 'rxjs';
import {WeighIn} from './weighin';
import {Calculation} from './calculation';

@Injectable({
    providedIn: 'root'
})
export class WeighInService {

    constructor(
        private http: HttpClient,
        private authService: AuthService
    ) {
    }

    public getUserWeighins(): Observable<WeighIn[]> {
        const httpOptions = this.authService.createHeadersWithAuthToken(this.authService.getToken());
        return this.http.get<WeighIn[]>('/api/weighin', httpOptions);
    }

    public getUserRollingAverage(): Observable<number> {
        const httpOptions = this.authService.createHeadersWithAuthToken(this.authService.getToken());
        return new Observable(observer => {
            this.http.get<any>('/api/weighin/calculation/average', httpOptions).subscribe(data => {
                observer.next(data.average);
            });
        });
    }

    public createUserWeighIn(weighIn: WeighIn): Observable<any> {
        const httpOptions = this.authService.createHeadersWithAuthToken(this.authService.getToken());
        return this.http.post<any>('/api/weighin', weighIn, httpOptions);
    }

    public getUserWeighInDelta(overDays: number): Observable<Calculation> {
        const httpOption = this.authService.createHeadersWithAuthToken(this.authService.getToken());
        httpOption['params'] = {
            days: overDays
        };
        return this.http.get<Calculation>(`/api/weighin/calculation/delta`, httpOption);
    }
}
