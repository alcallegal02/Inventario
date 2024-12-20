import { Component } from '@angular/core';
import { BuscadorComponent } from './components/buscador/buscador.component';
import { StockComponent } from './components/stock/stock.component';
import { MenuDesplegableComponent } from './components/menu-desplegable/menu-desplegable.component';
import { SelectorNaveComponent } from './components/selector-nave/selector-nave.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-nav',
  imports: [CommonModule, BuscadorComponent, StockComponent, MenuDesplegableComponent, SelectorNaveComponent],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {

}
