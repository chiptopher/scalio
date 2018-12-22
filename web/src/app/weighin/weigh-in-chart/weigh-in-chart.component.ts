import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {WeighIn} from '../weighin';
import {WeighInService} from '../weigh-in.service';
import {DateFormatter} from '../../util/date-formatter';

@Component({
    selector: 'app-weugh-in-chart',
    templateUrl: './weigh-in-chart.component.html',
    styleUrls: ['./weigh-in-chart.component.css']
})
export class WeighInChartComponent implements OnInit {

    @Input()
    weighIn: WeighIn[];

    multi: any[] = [
        {
            name: 'User Weight',
            series: []
        }
    ];
    showXAxis = true;
    showYAxis = true;
    gradient = false;
    showXAxisLabel = true;
    xAxisLabel = 'Weight';
    showYAxisLabel = true;
    yAxisLabel = 'Date';
    colorScheme = {
        domain: ['#5AA454']
    };
    autoScale = true;

    private dateFormatter: DateFormatter;

    constructor(private weighInService: WeighInService) {
        this.dateFormatter = new DateFormatter();
    }

    ngOnInit() {
        this.weighInService.getUserRollingAverageList().subscribe((rollingAverages) => {
            rollingAverages.forEach((rollingAverage) => {
                const date = this.dateFormatter.formatDate(new Date(rollingAverage.date));
                this.multi[0].series.push({name: date, value: rollingAverage.weight});
            });
            this.multi[0].series.reverse();
            console.log(this.multi[0].series);
        });
    }

}
