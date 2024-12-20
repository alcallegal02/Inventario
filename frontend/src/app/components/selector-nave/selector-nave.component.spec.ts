import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectorNaveComponent } from './selector-nave.component';

describe('SelectorNaveComponent', () => {
  let component: SelectorNaveComponent;
  let fixture: ComponentFixture<SelectorNaveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SelectorNaveComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelectorNaveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
