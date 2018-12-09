import {Component, OnInit} from '@angular/core';
import {LoginService} from '../login/login.service';
import {Router} from '@angular/router';

@Component({
    selector: 'app-regiser',
    templateUrl: './regiser.component.html',
    styleUrls: ['./regiser.component.css']
})
export class RegiserComponent implements OnInit {

    username: string;
    password: string;
    registrationFailed: boolean;

    constructor(
        private router: Router,
        private loginService: LoginService
    ) {
        this.registrationFailed = false;
    }

    ngOnInit() {
    }

    public handleRegistration() {
        this.loginService.register(this.username, this.password).subscribe(
            () => {
                this.router.navigate(['dashboard']);
            }, () => {
                this.registrationFailed = true;
            }
        );
    }

}
