import { Component } from '@angular/core';
import { HeaderComponent } from "../Inicio/header/header.component";
import { FooterComponent } from "../Inicio/footer/footer.component";
import { Router } from '@angular/router';

@Component({
    selector: 'app-estados',
    standalone: true,
    templateUrl: './estados.component.html',
    styleUrl: './estados.component.scss',
    imports: [HeaderComponent, FooterComponent]
})
export class EstadosComponent {
    constructor(private router: Router){}
  inicio(){
    this.router.navigate(['/primera-pag'])
  }

}
