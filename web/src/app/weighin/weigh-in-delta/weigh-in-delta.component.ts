import {Component, OnInit} from '@angular/core';
import {WeighInService} from '../weigh-in.service';
import {Calculation} from '../calculation';

@Component({
    selector: 'app-weigh-in-delta',
    templateUrl: './weigh-in-delta.component.html',
    styleUrls: ['./weigh-in-delta.component.css']
})
export class WeighInDeltaComponent implements OnInit {

    days: number;
    delta: Calculation;

    constructor(private weighInService: WeighInService) {
    }

    ngOnInit() {
    }

    getUserWeighInDelta() {
        this.weighInService.getUserWeighInDelta(this.days).subscribe((delta) => {
            this.delta = delta;
        });
    }
}
