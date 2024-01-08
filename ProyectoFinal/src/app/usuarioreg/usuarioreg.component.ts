import { Component } from '@angular/core';
import { CrudComponent } from "../crud/crud.component";

@Component({
    selector: 'app-usuarioreg',
    standalone: true,
    templateUrl: './usuarioreg.component.html',
    styleUrl: './usuarioreg.component.scss',
    imports: [CrudComponent]
})
export class UsuarioregComponent {

}
