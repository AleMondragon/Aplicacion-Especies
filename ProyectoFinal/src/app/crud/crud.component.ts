import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FooterComponent } from "../Inicio/footer/footer.component";

@Component({
    selector: 'app-crud',
    standalone: true,
    templateUrl: './crud.component.html',
    styleUrl: './crud.component.scss',
    imports: [FooterComponent]
})
export class CrudComponent {
  constructor(private router: Router){}
  pagina1(){
    this.router.navigate(['/primera-pag'])
  }
  info(){
    this.router.navigate(['/usuarioreg'])
  }
  actualizar(){
    this.router.navigate(['/actusuario'])
  }
  eliminar(){
    this.router.navigate(['/eliusuario'])
  }

}
