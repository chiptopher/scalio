import {Injectable} from '@angular/core';
import {AuthService} from '../../auth/auth.service';
import {Settings} from './settings';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class SettingsService {

    constructor(
        private http: HttpClient,
        private authService: AuthService) {
    }


    public getUserSettings(): Observable<Settings> {
        const headers = this.authService.createHeadersWithAuthToken(this.authService.getToken());
        return this.http.get<Settings>('/api/user/settings', headers);
    }
}
