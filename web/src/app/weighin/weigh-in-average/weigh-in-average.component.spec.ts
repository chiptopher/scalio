
import {WeighInAverageComponent} from './weigh-in-average.component';
import {WeighInService} from '../weigh-in.service';
import {Observable} from 'rxjs';
import {SettingsService} from '../../user/settings/settings.service';

describe('WeighInAverageComponent', () => {
    let component: WeighInAverageComponent;
    let mockWeighInService: WeighInService;
    let mockSettingsService: SettingsService

    beforeEach(() => {
        mockWeighInService = jasmine.createSpyObj({
            getUserRollingAverage: new Observable()
        });
        mockWeighInService = jasmine.createSpyObj({
            getUserSettings: new Observable()
        });
        component = new WeighInAverageComponent(mockWeighInService, mockSettingsService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
