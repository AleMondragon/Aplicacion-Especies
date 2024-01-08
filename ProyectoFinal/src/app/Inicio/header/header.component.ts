import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {
  constructor(private router: Router){}
  navegar(){
    this.router.navigate(['/crud'])
  }
  pagina1(){
    this.router.navigate(['/primera-pag'])
  }
  pagina2(){
    this.router.navigate(['/estados'])
  }
  pagina3(){
    this.router.navigate(['/especies'])
  }
  pagina4(){
    this.router.navigate(['/contacto'])
  }

}
