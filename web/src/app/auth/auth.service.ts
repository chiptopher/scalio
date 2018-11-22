import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class AuthService {

    constructor(
        private http: HttpClient
    ) {
    }

    public createHeadersWithAuthToken(token: string) {
        return {
            headers: new HttpHeaders({
                'Content-Type': 'application/json',
                'Authorization': token
            })
        };
    }

    public getToken(): string {
        return localStorage.getItem('token');
    }

    public validToken(token: string): Observable<boolean> {
        return new Observable<boolean>(next => {
            this.http.get('/api/user/authenticated', this.createHeadersWithAuthToken(token)).subscribe((response) => {
                next.next(true);
            }, (error) => {
                next.next(false);
            });
        });
    }

    public setToken(token: string) {
        localStorage.setItem('token', token);
    }
}
