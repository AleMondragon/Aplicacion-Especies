import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrimeraPagComponent } from './primera-pag.component';

describe('PrimeraPagComponent', () => {
  let component: PrimeraPagComponent;
  let fixture: ComponentFixture<PrimeraPagComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PrimeraPagComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PrimeraPagComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
