import { Component } from '@angular/core';
import { HeaderComponent } from "../Inicio/header/header.component";
import { FooterComponent } from "../Inicio/footer/footer.component";

@Component({
    selector: 'app-contacto',
    standalone: true,
    templateUrl: './contacto.component.html',
    styleUrl: './contacto.component.scss',
    imports: [HeaderComponent, FooterComponent]
})
export class ContactoComponent {

}
