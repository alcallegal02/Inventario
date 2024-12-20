import { Component } from '@angular/core';
import { DataService } from '../../services/data/data.service';
import { CommonModule } from '@angular/common';
import { TablaDepartamentoComponent } from '../../components/tabla-departamento/tabla-departamento.component';
import { NavComponent } from '../../components/nav/nav.component';

@Component({
  selector: 'app-main',
  imports: [CommonModule, NavComponent, TablaDepartamentoComponent],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  departamentos: any[] = [];

  constructor(private dataService: DataService) {}

  cargarDepartamentos(naveId: number): void {
    // Limpiar los departamentos previos antes de cargar los nuevos
    this.departamentos = [];

    // Llamada al backend para obtener los departamentos
    this.dataService.getDepartamentos(naveId).subscribe((data) => {
      // Asignar los departamentos y verificar si tienen datos
      this.departamentos = data.map((departamento: any) => ({
        ...departamento,
        tieneDatos: false // Inicialmente, asumimos que no tiene datos
      }));

      // Verificar si los departamentos tienen trabajadores o impresoras
      this.departamentos.forEach((departamento) => {
        this.dataService.getTrabajadores(departamento.id).subscribe((trabajadores) => {
          if (trabajadores.length > 0) {
            departamento.tieneDatos = true;
          }
        });

        this.dataService.getImpresoras(departamento.id).subscribe((impresoras) => {
          if (impresoras.length > 0) {
            departamento.tieneDatos = true;
          }
        });
      });
    });
  }
}