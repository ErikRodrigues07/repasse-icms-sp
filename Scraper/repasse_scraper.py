from playwright.sync_api import sync_playwright
from config import URL, HEADLESS
from Util.conversor import converter_valor
import time

class RepasseScraper:

    def __init__(self, service):
        self.service = service

    def executar(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS)
            page = browser.new_page()

            page.goto(URL)
            page.wait_for_selector("#ConteudoPagina_ddlMuni")

            municipios = [
                (opt.get_attribute("value"), opt.inner_text().strip())
                for opt in page.query_selector_all("#ConteudoPagina_ddlMuni option")
                if opt.get_attribute("value") != "---"
            ]

            for codigo_mun, nome_mun in municipios:

                print(f"\nMunicípio: {nome_mun}")

                for ano in range(2020, 2026):

                    print(f"  Ano: {ano}")

                    page.select_option("#ConteudoPagina_ddlMuni", codigo_mun)
                    page.select_option("#ConteudoPagina_ddlAno", str(ano))
                    page.check("#ConteudoPagina_rblTipo_0")

                    with page.expect_navigation():
                        page.click("#ConteudoPagina_btnConfirmar")

                    page.wait_for_selector("#ConteudoPagina_gdvRepasse")

                    rows = page.query_selector_all("#ConteudoPagina_gdvRepasse tr")

                    for i in range(1, len(rows)):

                        row = page.query_selector_all("#ConteudoPagina_gdvRepasse tr")[i]
                        cols = row.query_selector_all("td")

                        if len(cols) < 6:
                            continue

                        mes = cols[0].inner_text().strip()

                        if mes.lower() == "total":
                            continue

                        icms = converter_valor(cols[1].inner_text())
                        ipva = converter_valor(cols[2].inner_text())
                        fundexp = converter_valor(cols[3].inner_text())
                        comp = converter_valor(cols[4].inner_text())
                        total = converter_valor(cols[5].inner_text())

                        print(f"    {mes} | {total}")

                        self.service.salvar_mensal(
                            int(codigo_mun), int(ano), mes,
                            icms, ipva, fundexp, comp, total
                        )

                        link = row.query_selector("td a")

                        if link:
                            with page.expect_navigation():
                                link.click()

                            page.wait_for_selector("#ConteudoPagina_tbDetalhes")

                            colunas = page.query_selector_all("#ConteudoPagina_tbDetalhes > tbody > tr > td")

                            for col in colunas:
                                linhas = col.query_selector_all("table tr")

                                if len(linhas) < 7:
                                    continue

                                periodo = linhas[0].inner_text().strip()

                                if "Período" in periodo or periodo == "":
                                    continue

                                if "Total" in periodo:
                                    continue

                                data = linhas[1].inner_text().strip()

                                icms_s = converter_valor(linhas[2].inner_text())
                                fundexp_s = converter_valor(linhas[3].inner_text())
                                comp_s = converter_valor(linhas[4].inner_text())
                                ipva_s = converter_valor(linhas[5].inner_text())
                                total_s = converter_valor(linhas[6].inner_text())

                                print(f"       -> {periodo} | {total_s}")

                                self.service.salvar_detalhe(
                                    int(codigo_mun), int(ano), mes,
                                    periodo, data,
                                    icms_s, fundexp_s, comp_s, ipva_s, total_s
                                )

                            page.go_back()
                            page.wait_for_selector("#ConteudoPagina_gdvRepasse")

                    self.service.repository.commit()
                    time.sleep(1)

            browser.close()