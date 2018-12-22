import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {WeighInChartComponent} from './weigh-in-chart.component';
import {Subject} from 'rxjs';
import {WeighInService} from '../weigh-in.service';
import {WeighIn} from '../weighin';

describe('WeughInChartComponent', () => {
    let component: WeighInChartComponent;
    let mockWeighInServiceSubject: Subject<{weight: number, date: number}[]>;
    let mockWeighInService: WeighInService;

    beforeEach(() => {
        mockWeighInServiceSubject = new Subject();
        mockWeighInService = jasmine.createSpyObj({
            getUserRollingAverageList: mockWeighInServiceSubject
        });
        component = new WeighInChartComponent(mockWeighInService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    describe('ngOnChanges', () => {
        it('should get the users rolling average list', () => {
            component.ngOnInit();
            expect(mockWeighInService.getUserRollingAverageList).toHaveBeenCalled();
        });
        it('should convert the data into the graph format', () => {
            component.ngOnInit();
            mockWeighInServiceSubject.next([
                {weight: 200.0, date: 1514869200000},
                {weight: 150.0, date: 1514782800000},
            ]);
            expect(component.multi).toEqual(
                [
                    {
                        name: 'User Weight',
                        series: [
                            {
                                name: '2018-01-01',
                                value: 150.0
                            },
                            {
                                name: '2018-01-02',
                                value: 200.0
                            }
                        ]
                    }
                ]
            );
        });
    });
});
