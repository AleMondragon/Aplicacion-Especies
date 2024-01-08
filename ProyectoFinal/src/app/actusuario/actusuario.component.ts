import { Component } from '@angular/core';
import { CrudComponent } from "../crud/crud.component";

@Component({
    selector: 'app-actusuario',
    standalone: true,
    templateUrl: './actusuario.component.html',
    styleUrl: './actusuario.component.scss',
    imports: [CrudComponent]
})
export class ActusuarioComponent {

}
