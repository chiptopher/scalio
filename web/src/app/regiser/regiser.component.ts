import {Component, OnInit} from '@angular/core';
import {LoginService} from '../login/login.service';
import {Router} from '@angular/router';

@Component({
    selector: 'app-regiser',
    templateUrl: './regiser.component.html',
    styleUrls: ['./regiser.component.css']
})
export class RegiserComponent implements OnInit {

    constructor(
        private router: Router,
        private loginService: LoginService
    ) {
    }

    username: string;
    password: string;

    ngOnInit() {
    }

    public handleRegistration() {
        this.loginService.register(this.username, this.password).subscribe(
            (res) => {
                this.router.navigate(['dashboard']);
            }, (err) => {

            }
        );
    }

}
