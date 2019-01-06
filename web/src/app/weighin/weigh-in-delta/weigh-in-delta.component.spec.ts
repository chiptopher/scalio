import {WeighInDeltaComponent} from './weigh-in-delta.component';
import {WeighInService} from '../weigh-in.service';
import {Subject} from 'rxjs';

describe('WeighInDeltaComponent', () => {
    let component: WeighInDeltaComponent;
    let mockWeighInService: WeighInService;
    let getSubject: Subject<number>;

    beforeEach(() => {
        getSubject = new Subject();
        mockWeighInService = jasmine.createSpyObj({
            getUserWeighInDelta: getSubject
        });
        component = new WeighInDeltaComponent(mockWeighInService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    describe('getUserWeighInDelta', () => {
        it('should ask the service for the delta over the current number of days', () => {
            component.days = 30;
            component.getUserWeighInDelta();
            expect(mockWeighInService.getUserWeighInDelta).toHaveBeenCalledWith(30);
        });
        it('should save the result on the component', () => {
            component.days = 30;
            component.getUserWeighInDelta();
            getSubject.next(200.0);
            expect(component.delta.calculation).toBe(200.0);
        });
    });
});
