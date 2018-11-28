import {Component, Input, OnInit} from '@angular/core';
import {WeighIn} from '../weighin';
import {WeighInService} from '../weigh-in.service';

@Component({
    selector: 'app-weighin-list',
    templateUrl: './weighin-list.component.html',
    styleUrls: ['./weighin-list.component.css']
})
export class WeighinListComponent implements OnInit {

    MAXIMUM_DISPLAY_COUNT = 25;
    weighInList: WeighIn[];

    constructor(
        private weighInService: WeighInService
    ) {
    }

    ngOnInit() {
        this.weighInService.getUserWeighins().subscribe(data => {
            this.weighInList = data;
        });
    }

    public getWeighInListForDisplay() {
        if (this.weighInList !== undefined) {
            const sorted = this.weighInList.sort((a, b) => a.date > b.date ? -1 : a.date < b.date ? 1 : 0);
            return sorted.slice(0, this.MAXIMUM_DISPLAY_COUNT);
        } else {
            return [];
        }
    }

    formatWeighinTimestamp(timestamp: number) {
        const weighInDate = new Date(timestamp);
        return `${weighInDate.getMonth()}-${weighInDate.getDay()}-${weighInDate.getFullYear()}`;
    }

    formatWeighInWeight(weighInWeight: number): string {
      return weighInWeight.toFixed(1) + '';
    }
}
