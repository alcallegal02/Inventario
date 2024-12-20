import { Component, Input, OnInit } from '@angular/core';
import { DataService } from '../../services/data/data.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-tabla-departamento',
  imports: [CommonModule],
  templateUrl: './tabla-departamento.component.html',
  styleUrl: './tabla-departamento.component.css'
})

export class TablaDepartamentoComponent implements OnInit {
  @Input() departamentoId!: number;
  trabajadores: any[] = [];
  equipos: any[] = [];
  impresoras: any[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit(): void {
    this.cargarTrabajadores();
    this.cargarImpresoras();
  }

  cargarTrabajadores(): void {
    this.dataService.getTrabajadores(this.departamentoId).subscribe((data) => {
      this.trabajadores = data;
  
      this.trabajadores.forEach((trabajador: any) => {
        this.dataService.getEquipos(trabajador.id).subscribe((equipos) => {
          trabajador.equipos = equipos;
        });
      });
    });
  }

  cargarImpresoras(): void {
    this.dataService.getImpresoras(this.departamentoId).subscribe((data) => {
      this.impresoras = data;
    });
  }

  // Método para verificar si un trabajador tiene impresoras asociadas
  tieneImpresoras(trabajador: any): boolean {
    return trabajador.equipos.some((equipo: any) => equipo.impresoras && equipo.impresoras.length > 0);
  }

  
}