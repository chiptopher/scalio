import {DateFormat} from './date-formatter-types';

export class DateFormatter {

    constructor() {}

    public formatDate(date: Date, format?: DateFormat): string {
        const month = this.padStrings(date.getMonth() + 1);
        const day = this.padStrings(date.getDate());
        const year = date.getFullYear();
        let result;
        if (format === DateFormat.YYYYMMDD || !format) {
            result = `${year}-${month}-${day}`;
        } else if (format === DateFormat.MMDD) {
            result = `${month}/${day}`;
        }
        return result;
    }

    private padStrings(num: number): string {
        if (num < 10) {
            return '0' + num;
        } else {
            return `${num}`;
        }
    }
}
