import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { DataService } from '../../../../services/data/data.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-selector-nave',
  imports: [CommonModule],
  templateUrl: './selector-nave.component.html',
  styleUrl: './selector-nave.component.css'
})

export class SelectorNaveComponent implements OnInit {
  @Output() naveSeleccionada = new EventEmitter<number>();
  naves: any[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.dataService.getNaves().subscribe((data) => {
      this.naves = data;
    });
  }

  seleccionarNave(naveId: number): void {
    this.naveSeleccionada.emit(naveId);
  }
}