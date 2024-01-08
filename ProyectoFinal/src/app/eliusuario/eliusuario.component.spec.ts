import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EliusuarioComponent } from './eliusuario.component';

describe('EliusuarioComponent', () => {
  let component: EliusuarioComponent;
  let fixture: ComponentFixture<EliusuarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EliusuarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EliusuarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
