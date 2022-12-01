from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('http://treino.gigalink.net.br/entrar')
    page.locator('xpath=//*[@id="funcionario_email"]').click()
    page.fill('xpath=//*[@id="funcionario_email"]', '******')
    page.locator('xpath=//*[@id="funcionario_password"]').click()
    page.fill('xpath=//*[@id="funcionario_password"]', '******')
    page.get_by_role("button").click()
    page.goto('http://treino.gigalink.net.br/relatorios/vendas/contratos?funcionario_logado_id=1189&data_inicio=29%2F11%2F2022&data_fim=29%2F11%2F2022&categoria_id%5B%5D=7&canal_venda=&status=&commit=Consultar')

    
