import {RouterModule,Routes } from '@angular/router';
import {EstadosComponent} from './estados/estados.component';
import { PrimeraPagComponent } from "./primera-pag/primera-pag.component";
import { LoginComponent } from "./login/login.component";
import { LoginReComponent } from "./login-re/login-re.component";
import { ContactoComponent } from "./contacto/contacto.component";
import { CrudComponent } from "./crud/crud.component";
import { ActusuarioComponent } from "./actusuario/actusuario.component";
import { UsuarioregComponent } from "./usuarioreg/usuarioreg.component";
import { EliusuarioComponent } from "./eliusuario/eliusuario.component";
import { EspeciesComponent } from './especies/especies.component';



export const routes: Routes = [
    {path:'',redirectTo:'/primera-pag', pathMatch:'full'},
    {path:'primera-pag',component:PrimeraPagComponent},
    {path:'login-re', component:LoginReComponent},
    {path:'login',component:LoginComponent},
    {path:'estados',component:EstadosComponent},
    {path:'contacto',component:ContactoComponent},
    {path:'crud',component:CrudComponent},
    {path:'actusuario',component:ActusuarioComponent},
    {path:'usuarioreg', component:UsuarioregComponent},
    {path:'eliusuario', component:EliusuarioComponent},
    {path:'especies', component:EspeciesComponent}

];

