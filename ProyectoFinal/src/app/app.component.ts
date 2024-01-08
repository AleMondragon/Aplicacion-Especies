import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from "./Inicio/header/header.component";
import { FooterComponent } from "./Inicio/footer/footer.component";
import { PrimeraPagComponent } from "./primera-pag/primera-pag.component";
import { LoginComponent } from "./login/login.component";
import { LoginReComponent } from "./login-re/login-re.component";
import { EstadosComponent } from "./estados/estados.component";
import { ActusuarioComponent } from "./actusuario/actusuario.component";
import { ContactoComponent } from "./contacto/contacto.component";
import { CrudComponent } from "./crud/crud.component";
import { UsuarioregComponent } from "./usuarioreg/usuarioreg.component";
import { EliusuarioComponent } from "./eliusuario/eliusuario.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
    imports: [CommonModule, RouterOutlet, HeaderComponent, FooterComponent, PrimeraPagComponent, LoginComponent, LoginReComponent, EstadosComponent, ActusuarioComponent, ContactoComponent, CrudComponent, UsuarioregComponent, EliusuarioComponent]
})
export class AppComponent {
  title = 'ProyectoFinal';
}
