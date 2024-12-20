import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TablaDepartamentoComponent } from './tabla-departamento.component';

describe('TablaDepartamentoComponent', () => {
  let component: TablaDepartamentoComponent;
  let fixture: ComponentFixture<TablaDepartamentoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TablaDepartamentoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TablaDepartamentoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
