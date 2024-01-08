import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UsuarioregComponent } from './usuarioreg.component';

describe('UsuarioregComponent', () => {
  let component: UsuarioregComponent;
  let fixture: ComponentFixture<UsuarioregComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UsuarioregComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(UsuarioregComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
