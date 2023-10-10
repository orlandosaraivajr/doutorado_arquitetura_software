package br.com.portalz.condominio.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import br.com.portalz.condominio.entity.Acesso;

public interface AcessoRepository extends JpaRepository<Acesso, Long> {

    java.util.List<Acesso> findByPlaca(String placa);
}