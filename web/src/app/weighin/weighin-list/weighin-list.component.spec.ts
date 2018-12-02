import {WeighinListComponent} from './weighin-list.component';
import {WeighIn} from '../weighin';
import {WeighInService} from '../weigh-in.service';
import {Observable} from 'rxjs';

describe('WeighinListComponent', () => {
    let mockWeighInService: WeighInService;
    let component: WeighinListComponent;

    beforeEach(() => {
        mockWeighInService = jasmine.createSpyObj({
            getUserWeighins: new Observable()
        });
        component = new WeighinListComponent(mockWeighInService);
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should sort the list with the most recent weigh ins first', () => {
        const mostRecentTime = 1540778229;
        const mostRecentWeighIn = new WeighIn(191.1, mostRecentTime);
        const secondMostRecentWeighIn = new WeighIn(191.1, mostRecentTime - 100);
        component.weighInList = [secondMostRecentWeighIn, mostRecentWeighIn];
        const sortedList = component.getWeighInListForDisplay();
        expect(sortedList[0].date).toBe(mostRecentTime);
        expect(sortedList[1].date).toBe(mostRecentTime - 100);
    });

    it('should only show the most recent weigh ins according to the maximum amount', () => {
        const mostRecentTime = 15050778229;
        const weighIn = new WeighIn(101.1, mostRecentTime);
        const array = [];
        let i: number;
        for (i = 0; i < 100; i++) {
            array.push(Object.assign({}, weighIn));
        }
        component.weighInList = array;
        const result = component.getWeighInListForDisplay();
        expect(result.length).toBe(25);
    });

    describe('formatWeighIn', () => {
        it('should round weigh ins with long decimals to the first decimal place', () => {
            expect(component.formatWeighInWeight(201.16)).toBe('201.2');
        });
        it('should pad no decimals to the first decimal place with a zero', () => {
            expect(component.formatWeighInWeight(201)).toBe('201.0');
        });
        it('should do nothing to first decimal place number', () => {
            expect(component.formatWeighInWeight(201.1)).toBe('201.1');
        });
    });

    describe('formatTimestamp', () => {
        it('should correctly convert unix timestamp into date', () => {
            expect(component.formatWeighinTimestamp(1543761377688)).toBe('12-02-2018');
        });
    });
});
