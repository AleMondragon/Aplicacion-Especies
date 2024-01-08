import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActusuarioComponent } from './actusuario.component';

describe('ActusuarioComponent', () => {
  let component: ActusuarioComponent;
  let fixture: ComponentFixture<ActusuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ActusuarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ActusuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
