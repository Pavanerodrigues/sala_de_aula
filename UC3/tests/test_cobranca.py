def test_avisa_quem_passou_do_prazo():  
    atrasado = Emprestimo(1, "Ana Souza", "51 99999-0001", date(2026, 11, 1))
    repositorio = Mock(spec=RepositorioDeEmprestimo)
    reposito.abertos.return_value = [atrasado]
    
    avisador =Mock()
    cobrador = CobradorDeAtrasos()
    cobrador.cobrar()

    assert cobrador.total_avisados == 1




def test_nao_avisa_quem_ainda_esta_no_prazo():
    ...
    avisador.avisa.assert_not_called()






def test_avisa_cada_atrasado_uma_vez():
    ...  # três empréstimos abertos, dois atrasados
    assert avisador.avisa.call_count == 2 



