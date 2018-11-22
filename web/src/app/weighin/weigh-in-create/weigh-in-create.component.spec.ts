import {WeighInCreateComponent} from './weigh-in-create.component';
import {WeighInService} from '../weigh-in.service';
import {Observable} from 'rxjs';
import {Router} from '@angular/router';

describe('WeighInCreateComponent', () => {
    let component: WeighInCreateComponent;
    let mockWeighInService: WeighInService;
    let mockRouter: Router;

    beforeEach(() => {
        mockWeighInService = jasmine.createSpyObj({
            createUserWeighIn: new Observable()
        });
        mockRouter = jasmine.createSpyObj({
            navigateByUrl: new Observable()
        });
        component = new WeighInCreateComponent(mockWeighInService, mockRouter);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
