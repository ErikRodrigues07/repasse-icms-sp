class RepasseService:
    
    def __init__(self, repository):
        self.repository = repository

    def salvar_mensal(self, codigo, ano, mes, icms, ipva, fundexp, comp, total):
        dados = (codigo, ano, mes, icms, ipva, fundexp, comp, total)
        self.repository.inserir_mensal(dados)

    def salvar_detalhe(self, codigo, ano, mes, periodo, data, icms, fundexp, comp, ipva, total):
        dados = (codigo, ano, mes, periodo, data, icms, fundexp, comp, ipva, total)
        self.repository.inserir_detalhe(dados)