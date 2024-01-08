import { Component } from '@angular/core';
import { HeaderComponent } from "../Inicio/header/header.component";
import { FooterComponent } from "../Inicio/footer/footer.component";

@Component({
    selector: 'app-login',
    standalone: true,
    templateUrl: './login.component.html',
    styleUrl: './login.component.scss',
    imports: [HeaderComponent, FooterComponent]
})
export class LoginComponent {

}
