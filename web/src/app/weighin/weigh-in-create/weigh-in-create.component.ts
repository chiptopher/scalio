import {Component, OnInit} from '@angular/core';
import {WeighInService} from '../weigh-in.service';
import {WeighIn} from '../weighin';
import {Router} from '@angular/router';

@Component({
    selector: 'app-weigh-in-create',
    templateUrl: './weigh-in-create.component.html',
    styleUrls: ['./weigh-in-create.component.css']
})
export class WeighInCreateComponent implements OnInit {

    weight: number;

    constructor(
        private weighInService: WeighInService,
        private router: Router
    ) {
    }

    ngOnInit() {
    }

    public handleWeighInCreate() {
        const weighIn = new WeighIn(this.weight, new Date().getTime());
        this.weighInService.createUserWeighIn(weighIn).subscribe(result => {
            this.router.navigateByUrl('/dashboard');
        });
    }
}
