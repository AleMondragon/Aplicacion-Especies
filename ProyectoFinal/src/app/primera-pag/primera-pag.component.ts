import { Component } from '@angular/core';
import { HeaderComponent } from "../Inicio/header/header.component";
import { FooterComponent } from "../Inicio/footer/footer.component";
import { Router } from '@angular/router';

@Component({
    selector: 'app-primera-pag',
    standalone: true,
    templateUrl: './primera-pag.component.html',
    styleUrl: './primera-pag.component.scss',
    imports: [HeaderComponent, FooterComponent]
})
export class PrimeraPagComponent {
    constructor(private router: Router){}
    registrar(){
      this.router.navigate(['/login-re'])
    }
    isesion(){
      this.router.navigate(['/login'])
    }
}
