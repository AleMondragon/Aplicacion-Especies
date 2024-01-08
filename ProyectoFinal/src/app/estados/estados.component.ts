import { Component } from '@angular/core';
import { HeaderComponent } from "../Inicio/header/header.component";
import { FooterComponent } from "../Inicio/footer/footer.component";

@Component({
    selector: 'app-estados',
    standalone: true,
    templateUrl: './estados.component.html',
    styleUrl: './estados.component.scss',
    imports: [HeaderComponent, FooterComponent]
})
export class EstadosComponent {

}
