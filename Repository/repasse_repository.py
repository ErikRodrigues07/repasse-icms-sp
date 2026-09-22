class RepasseRepository:
    
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def inserir_mensal(self, dados):
        self.cursor.execute("""
            INSERT INTO RepasseMensal (
                CodigoMunicipio, Ano, Mes, ICMS, IPVA, FundExp, Comp, Total
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)

    def inserir_detalhe(self, dados):
        self.cursor.execute("""
            INSERT INTO RepasseSemanal (
                CodigoMunicipio, Ano, Mes, Periodo,
                DataCredito, ICMS, FundExp, Comp, IPVA, Total
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)

    def commit(self):
        self.conn.commit()