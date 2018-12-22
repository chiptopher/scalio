import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {LoginComponent} from './login/login.component';
import {RouterModule} from '@angular/router';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {DashboardComponent} from './dashboard/dashboard.component';
import {AccessGuardService} from './auth/access-guard.service';
import {FormsModule} from '@angular/forms';
import { RegiserComponent } from './regiser/regiser.component';
import { WeighinListComponent } from './weighin/weighin-list/weighin-list.component';
import { WeighInAverageComponent } from './weighin/weigh-in-average/weigh-in-average.component';
import { WeighInCreateButtonComponent } from './weighin/weigh-in-create-button/weigh-in-create-button.component';
import { WeighInCreateComponent } from './weighin/weigh-in-create/weigh-in-create.component';
import {UrlInterceptor} from './util/http-interceptor.interceptor';
import { RequestComponent } from './request/request.component';
import { WeighInChartComponent } from './weighin/weigh-in-chart/weigh-in-chart.component';
import {NgxChartsModule} from '@swimlane/ngx-charts';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';

@NgModule({
    declarations: [
        AppComponent,
        LoginComponent,
        DashboardComponent,
        RegiserComponent,
        WeighinListComponent,
        WeighInAverageComponent,
        WeighInCreateButtonComponent,
        WeighInCreateComponent,
        RequestComponent,
        WeighInChartComponent
    ],
    imports: [
        HttpClientModule,
        BrowserModule,
        NgxChartsModule,
        FormsModule,
        BrowserAnimationsModule,
        RouterModule.forRoot([
            {path: 'dashboard', component: DashboardComponent, canActivate: [AccessGuardService]},
            {path: 'login', component: LoginComponent},
            {path: 'register', component: RegiserComponent},
            {path: 'weigh-in/create', component: WeighInCreateComponent},
            {path: '', redirectTo: 'dashboard', pathMatch: 'full'}
        ])
    ],
    providers: [
        AccessGuardService,
        {
            provide: HTTP_INTERCEPTORS,
            useClass: UrlInterceptor,
            multi: true
        }
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
}
