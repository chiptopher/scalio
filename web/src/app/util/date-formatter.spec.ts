import {DateFormatter} from './date-formatter';
import {DateFormat} from './date-formatter-types';

describe('DateFormatter', () => {
    let dateFormatter: DateFormatter;

    beforeEach(() => {
        dateFormatter = new DateFormatter();
    });

    describe('formatDate', () => {
        it('should format yyyy-mm-dd when given that format parameter', () => {
            expect(dateFormatter.formatDate(new Date(1514782800000), DateFormat.YYYYMMDD)).toBe('2018-01-01');
        });
        it('should format MM/DD', () => {
            expect(dateFormatter.formatDate(new Date(1514782800000), DateFormat.MMDD)).toBe('01/01');
        });
        it('should formay yyyy-mm-dd with default', () => {
            expect(dateFormatter.formatDate(new Date(1514782800000))).toBe('2018-01-01');
        });
    });
});
