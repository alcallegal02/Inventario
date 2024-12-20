import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs'; 

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private baseUrl = 'http://localhost:8000/app'; // Base URL del backend

  constructor(private http: HttpClient) {}

  getNaves(): Observable<any> {
    return this.http.get(`${this.baseUrl}/naves/`);
  }

  getDepartamentos(naveId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/departamentos/by_nave/?nave=${naveId}`);
  }

  getTrabajadores(departamentoId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/trabajadores/by_departamento/?departamento=${departamentoId}`);
  }

  getEquipos(trabajadorId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/equipos/?trabajador=${trabajadorId}`);
  }

  getImpresoras(departamentoId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/impresoras/by_departamento/?departamento=${departamentoId}`);
  }
}