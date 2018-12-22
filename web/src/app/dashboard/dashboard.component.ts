import {Component, OnInit} from '@angular/core';
import {WeighIn} from '../weighin/weighin';
import {WeighInService} from '../weighin/weigh-in.service';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

    constructor() {
    }

    ngOnInit() {
    }

}
