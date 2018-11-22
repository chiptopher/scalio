

import { AuthService } from './auth.service';
import {Router} from '@angular/router';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

describe('AuthService', () => {
    let httpClient: HttpClient;
    let service: AuthService;
  beforeEach(() => {
      httpClient = jasmine.createSpyObj({
          get: Observable
      });
      service = new AuthService(httpClient);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
