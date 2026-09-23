class RepasseRepository:
    
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def inserir_municipio(self, codigo, nome, uf="SP"):
        self.cursor.execute("""
            IF NOT EXISTS (
                SELECT 1 FROM Municipios WHERE Codigo = ?
            )
            BEGIN
                INSERT INTO Municipios (Codigo, Nome, UF)
                VALUES (?, ?, ?)
            END
        """, (codigo, codigo, nome, uf))

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

    def municipio_existe(self, codigo):
        self.cursor.execute("""
            SELECT 1
            FROM Municipios
            WHERE Codigo = ?
        """, (codigo,))

        return self.cursor.fetchone() is not None
