import {Observable, of} from 'rxjs';
import {ActivatedRouteSnapshot, CanActivate, Router} from '@angular/router';
import {Injectable} from '@angular/core';
import {catchError, map} from 'rxjs/operators';
import {AuthService} from './auth.service';

@Injectable()
export class AccessGuardService implements CanActivate {

    constructor(
        private router: Router,
        private authService: AuthService
    ) {
    }

    canActivate(route: ActivatedRouteSnapshot): Observable<boolean> | Promise<boolean> | boolean {
        return this.authService.validToken(this.authService.getToken())
            .pipe(
                map(e => {
                    if (e) {
                        return true;
                    } else {
                        this.router.navigate(['/login']);
                        return false;
                    }
                }), catchError((err) => {
                    this.router.navigate(['/login']);
                    return of(false);
                })
            );
    }
}
