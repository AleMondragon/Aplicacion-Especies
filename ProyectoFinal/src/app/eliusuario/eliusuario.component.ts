import { Component } from '@angular/core';
import { CrudComponent } from "../crud/crud.component";

@Component({
    selector: 'app-eliusuario',
    standalone: true,
    templateUrl: './eliusuario.component.html',
    styleUrl: './eliusuario.component.scss',
    imports: [CrudComponent]
})
export class EliusuarioComponent {

}
