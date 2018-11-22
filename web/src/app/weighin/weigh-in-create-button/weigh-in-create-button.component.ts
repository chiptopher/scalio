import {Component, OnInit} from '@angular/core';
import {Router} from '@angular/router';

@Component({
    selector: 'app-weigh-in-create-button',
    templateUrl: './weigh-in-create-button.component.html',
    styleUrls: ['./weigh-in-create-button.component.css']
})
export class WeighInCreateButtonComponent implements OnInit {

    constructor(
        private router: Router
    ) {
    }

    ngOnInit() {
    }

    public navigateToForm() {
        this.router.navigate(['/weigh-in/create']);
    }
}
