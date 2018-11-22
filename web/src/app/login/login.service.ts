import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {AuthService} from '../auth/auth.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class LoginService {

    constructor(
        private http: HttpClient,
        private authService: AuthService
    ) {
    }

    public login(username: string, password: string): Observable<any> {
        return this.handleUserAuth('/api/user/login', username, password);
    }

    public register(username: string, password: string): Observable<any> {
        return this.handleUserAuth('/api/user/register', username, password);
    }

    private handleUserAuth(url: string, username: string, password: string): Observable<any> {
        return new Observable(observer => {
            const httpOptions = {
                headers: new HttpHeaders({
                    'Content-Type': 'application/json'
                })
            };
            this.http.post<string>(url, {username: username, password: password}, httpOptions).subscribe(response => {
                if (response) {
                    this.authService.setToken(`Bearer ${response['token']}`);
                }
                observer.next(response);
            });
        });
    }
}
