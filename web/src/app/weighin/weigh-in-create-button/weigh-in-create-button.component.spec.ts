import {WeighInCreateButtonComponent} from './weigh-in-create-button.component';
import {Router} from '@angular/router';
import {Observable} from 'rxjs';

describe('WeighInCreateButtonComponent', () => {
    let mockRouter: Router;
    let component: WeighInCreateButtonComponent;

    beforeEach(() => {
        mockRouter = jasmine.createSpyObj({
            navigate: new Observable()
        });
        component = new WeighInCreateButtonComponent(mockRouter);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
