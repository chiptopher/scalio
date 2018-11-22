import {Component, OnInit} from '@angular/core';
import {WeighInService} from '../weigh-in.service';
import {SettingsService} from '../../user/settings/settings.service';

@Component({
    selector: 'app-weigh-in-average',
    templateUrl: './weigh-in-average.component.html',
    styleUrls: ['./weigh-in-average.component.css']
})
export class WeighInAverageComponent implements OnInit {

    average: string;
    rollingAverageDays: number;

    constructor(
        private weighInService: WeighInService,
        private settingsService: SettingsService
    ) {
    }

    ngOnInit() {
        this.weighInService.getUserRollingAverage().subscribe(data => {
            this.average = data.toFixed(2);
        });
        this.settingsService.getUserSettings().subscribe(data => {
            console.log(data);
            this.rollingAverageDays = data.rolling_average_days;
        });
    }

}
