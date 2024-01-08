import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginReComponent } from './login-re.component';

describe('LoginReComponent', () => {
  let component: LoginReComponent;
  let fixture: ComponentFixture<LoginReComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LoginReComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LoginReComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
