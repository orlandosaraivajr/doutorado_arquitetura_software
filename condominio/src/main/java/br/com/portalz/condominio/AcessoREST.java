package br.com.portalz.condominio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.com.portalz.condominio.repository.AcessoRepository;
import br.com.portalz.condominio.entity.Acesso;

@RestController
@RequestMapping("/acesso")
public class AcessoREST {
    @Autowired
    private AcessoRepository repositorio;
    
    @GetMapping("/{placa}")
    public java.util.List<Acesso> listar(@PathVariable String placa){

        return repositorio.findByPlaca(placa);
    }

    @GetMapping("/all")
    public java.util.List<Acesso> listar(){

        return repositorio.findAll();
    }

    @PostMapping
    public void salvar(@RequestBody Acesso acesso){
        long millis=System.currentTimeMillis(); 

        java.sql.Date hoje = new java.sql.Date(millis);
        java.sql.Time hora = new java.sql.Time(millis); 

        acesso.setData( hoje );
        acesso.setHora( hora );

        repositorio.save(acesso);
    }
}
