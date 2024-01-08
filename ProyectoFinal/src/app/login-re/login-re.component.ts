import { Component } from '@angular/core';
import { FooterComponent } from "../Inicio/footer/footer.component";
import { HeaderComponent } from "../Inicio/header/header.component";

@Component({
    selector: 'app-login-re',
    standalone: true,
    templateUrl: './login-re.component.html',
    styleUrl: './login-re.component.scss',
    imports: [FooterComponent, HeaderComponent]
})
export class LoginReComponent {

}
